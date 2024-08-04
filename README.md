
# RAG Chatbot 🤖

## Overview

Welcome to the RAG Chatbot project! This application allows you to upload PDF files and ask questions based on their content. It uses an open-resource LLM model to generate answers from the PDFs you upload.

### Important Note

🔍 **Model Efficiency**: This application uses the `distilbert-base-uncased` model, which is suitable for the current system configuration. Be aware that there might be some noise in the text generation or chunk matching. For improved performance, consider using higher-end models like `bert-base-uncased` or `roberta-base`. Ensure you adjust the vector index dimensions accordingly if you upgrade the model.

**Model Choices**:

-   `bert-base-uncased`
-   `roberta-base`

## How It Works

1. **Upload PDF Files** 📄
   - Use the file uploader to upload multiple PDF files. The content of these PDFs will be processed and stored for querying.
   
### Sample Documents

You can find sample PDFs related to data science in the `docs` folder of this project. Upload these sample documents to test the functionality of the app.

2. **Ask Questions** ❓
   - Once the PDFs are uploaded, enter your questions into the input box. The app will query the content of the uploaded PDFs and provide relevant answers.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Pip (Python package installer)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <project-folder>

2. **Set Up Environment**:

-   **Install Dependencies**:
    
    `pip install -r requirements.txt`

3. **Configure Environment Variables**:

-   Create a `.env` file in the root directory of your project.
-   Add your Pinecone API credentials to the `.env` file:
    
    `PINECONE_API_KEY=your-pinecone-api-key
    PINECONE_ENV=your-pinecone-environment
    PINECONE_INDEX_NAME=your-index-name`

4. **Run the App**:

`streamlit run app.py`