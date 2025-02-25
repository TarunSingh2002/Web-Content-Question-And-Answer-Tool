import os
import requests
import streamlit as st
from bs4 import BeautifulSoup
from langchain_openai import ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_core.documents import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

my_openai_key = os.getenv("OPENAI")

# --- Web Scraping Functions ---
def fetch_and_extract(url: str) -> str:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
    except requests.RequestException as e:
        st.error(f"Error fetching {url}: {e}")
        return ""
    
    soup = BeautifulSoup(response.text, "html.parser")
    for element in soup(["script", "style", "header", "footer", "nav", "aside"]):
        element.decompose()
    return soup.get_text(separator=" ", strip=True)

@st.cache_resource
def load_embeddings():
    return HuggingFaceEmbeddings(
        model_name= "sentence-transformers/all-MiniLM-L6-v2",
        # model_kwargs={'device': 'cpu'}
    )

@st.cache_resource
def load_llm():
    return ChatOpenAI(model='gpt-4o', temperature=0.7, max_completion_tokens=100, api_key=my_openai_key)

def setup_qa_pipeline(text: str):
    text_splitter = CharacterTextSplitter(
         separator=".",
         chunk_size=500,
         chunk_overlap=100,
         )
    texts = text_splitter.split_text(text)
    docs = [Document(page_content=t) for t in texts]
    
    vectorstore = FAISS.from_documents(
        docs, 
        embedding=load_embeddings()
    )
    
    return RetrievalQA.from_chain_type(
        llm=load_llm(),
        chain_type="stuff",
        retriever=vectorstore.as_retriever()
    )

st.title("Web Content Q&A Tool")

with st.form("qa_form"):
    urls = st.text_area("Enter URLs (one per line):", height=100)
    question = st.text_input("Question:")
    submitted = st.form_submit_button("Get Answer")

if submitted:
    if not (urls and question):
        st.warning("Please provide both URLs and a question")
    else:
        url_list = [url.strip() for url in urls.splitlines() if url.strip()]
        with st.spinner("Analyzing content..."):
            content = "\n".join(fetch_and_extract(url) for url in url_list)
            if not content:
                st.error("Failed to retrieve content from URLs")
                st.stop()
            
            qa_chain = setup_qa_pipeline(content)
            answer = qa_chain.invoke("Answer this question in minimum words"+question)
            # st.subheader()
            st.write(answer['result'])
