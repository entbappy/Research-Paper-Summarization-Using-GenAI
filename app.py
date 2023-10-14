import streamlit as st
from langchain.chat_models import ChatOpenAI
from paperSummarizer.components.load_docs import load_documents
from paperSummarizer.components.custom_summarizer import custom_summary
from paperSummarizer.constants import *
from paperSummarizer.utils import read_yaml


def main():
    st.set_page_config(layout="wide")
    st.title("Research Paper Summarization App")
    llm = st.sidebar.selectbox("LLM",["ChatGPT", "GPT4", "Other (open source in the future)"])
    chain_type = st.sidebar.selectbox("Chain Type", ["map_reduce", "stuff", "refine"])
    chunk_size = st.sidebar.slider("Chunk Size", min_value=20, max_value = 10000,
                                   step=10, value=2000)
    
    

    user_prompt = st.text_input("Enter the custom summary prompt")

    config = read_yaml(CONFIG_FILE_PATH)
    
    pdf_file_path = ""

    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None:
        pdf_file_path = config.paper_path
        print(pdf_file_path)
        bytes_data = uploaded_file.getvalue()
        with open(pdf_file_path, 'wb') as f: 
            f.write(bytes_data)
    
    temperature = st.sidebar.number_input("Set the Model Temperature",
                                            min_value = 0.0,
                                            max_value=1.0,
                                            step=0.1,
                                            value=0.5)
    num_summaries = st.sidebar.number_input("Number of summaries",
                                            min_value = 1, 
                                            max_value = 10,
                                            step = 1,
                                            value=1)
    if pdf_file_path != "":
        docs = load_documents(pdf_file_path, chunk_size)
        st.write("PDF loaded successfully")
    
        if llm=="ChatGPT":
            llm = ChatOpenAI(temperature=temperature)
        elif llm=="GPT4":
            llm = ChatOpenAI(model_name="gpt-4",temperature=temperature)
        else:
            st.write("Using ChatGPT while open source models are not implemented!")
            llm = ChatOpenAI(temperature=temperature)
        
        if st.button("Summarize"):
            result = custom_summary(docs, llm, user_prompt, chain_type, num_summaries)
            st.write("Summary:")
            for summary in result:
                st.write(summary)
            
    
if __name__=="__main__":
    main()