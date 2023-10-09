
import openai
import os
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


load_dotenv()
openai.api_key = os.getenv("OpenAI_API_KEY")  


def load_documents(pdf_file_path,chunk_size):
    loader = PyPDFLoader(pdf_file_path)
    docs_raw = loader.load()
    docs_raw_text = [doc.page_content for doc in docs_raw]
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size)
    docs = text_splitter.create_documents(docs_raw_text)
    
    return docs