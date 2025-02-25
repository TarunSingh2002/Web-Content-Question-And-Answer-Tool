# Web Content Question And Answer Tool 🔍

**[Check out the live project here!](https://tarun-singh-web-content-question-and-answer-tool.hf.space/)**

The Web Content Question And Answer Tool is a powerful Python-based application that leverages web scraping, vector embeddings, and large language models (LLMs) to answer questions based on content extracted from one or more URLs. With an intuitive Streamlit interface and the robust capabilities of LangChain and FAISS, this tool provides concise, context-aware responses to your queries by analyzing the text from any web page you specify.

<table border="2" style="width:100%; border-collapse: collapse;">
  <tr>
    <td><img src="https://github.com/user-attachments/assets/49784cb7-1d4d-4648-b168-53838202fecf" alt="Project Image 1" style="width:100%;"></td>
  </tr>
</table>

## Table of Contents

1. [Features](#features)
2. [Tech Stack](#tech-stack)
3. [Project Structure](#project-structure)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Deployment](#deployment)
7. [Configuration](#configuration)
8. [License](#license)
9. [Acknowledgments](#acknowledgments)

## Features ✨

- **Web Content Extraction**: Automatically scrapes and cleans content from multiple URLs.
- **AI-Powered Q&A**: Answers questions using GPT-4o model with RAG architecture.
- **Document Processing**:
  - Text splitting with overlap for context preservation.
  - Vector embeddings using Hugging Face models.
- **Efficient Retrieval**:
  - FAISS vector store for fast similarity search.
  - Context-aware answer generation.
- **User-Friendly Interface**:
  - Streamlit web interface.
  - Real-time processing indicators.
  - Error handling for invalid URLs.

## Tech Stack 🛠️

| Component               | Technology Used          |
|-------------------------|--------------------------|
| Frontend                | Streamlit                |
| Language Model          | OpenAI GPT-4o            |
| Embeddings              | HuggingFace Embeddings   |
| Vector Store            | FAISS                    |
| Web Scraping            | BeautifulSoup4           |
| Text Processing         | LangChain                |
| Deployment              | Hugging Face Spaces      |

## Project Structure 📁

```bash
├── app.py                 <- Main Streamlit application file.
├── requirements.txt       <- The requirements file for reproducing the environment.
├── README.md              <- The top-level README for developers using this project.
├── .gitattributes         <- Configuration files.       
└── .gitignore             <- Specifies which files to ignore in the version control.            

```
## Installation 💻

To set up and run the Web Content Question And Answer Tool on your local machine, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/TarunSingh2002/Web-Content-Question-And-Answer-Tool
    cd Web-Content-Question-And-Answer-Tool
    ```

2. **Set up a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/MacOS
    venv\Scripts\activate     # Windows
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set environment variables:**
    ```bash
    export OPENAI_API_KEY="your-openai-key"
    ```

## Usage 🚀

1. **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

2. **Open your browser and go to:**
    ```
    http://localhost:8501
    ```

3. **Interact with the Tool:**

   - Input URLs: Enter one or more URLs (each on a new line) in the provided text area.
   - Ask a Question: Type your query in the designated input field.
   - Submit: Start the analysis by clicking the "Get Answer" button.
   - View the Answer: The tool will display a succinct answer generated from the content of the provided URLs.
    ```bash
    URLs:
    https://en.wikipedia.org/wiki/Large_language_model
    https://aws.amazon.com/what-is/llm/

    Question:
    What are the main applications of LLMs?
    ```


## Deployment 🌐

### Deploying to Hugging Face Spaces

1. **Create new Space:**
   - Select Streamlit template.
   - Choose appropriate hardware (CPU Basic for testing).

2. **Add secrets:**
   - OPENAI → Your OpenAI API key

3. **Deploy from repository:**
   - Connect your Git repository.
   - Push changes to trigger automatic deployment.



## Configuration ⚙️

### Environment Variables

| Variable                | Description              | Required                 |                        
|-------------------------|--------------------------|--------------------------|
| OPENAI                  | OpenAI API key           | Yes                      |

### Model Parameters
```markdown
    # LLM Settings
     ChatOpenAI(
        model='gpt-4o',
        temperature=0.7,  # Creativity control (0-1)
        max_tokens=100    # Response length limit
    )

    # Text Processing
    CharacterTextSplitter(
        chunk_size=500,    # Character limit per chunk
        chunk_overlap=100  # Context preservation overlap
    )
```

## License 📜
```markdown
MIT License

Copyright (c) 2024 Tarun Singh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Acknowledgments 🙏

- **OpenAI** for the GPT-4o language model
- **Hugging Face** for embeddings and hosting
- **LangChain** team for the RAG framework
- **Streamlit** for the web interface framework
- **Beautiful Soup** for web scraping capabilities
