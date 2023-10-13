import openai
import os
from dotenv import load_dotenv
from langchain import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from paperSummarizer import logger

load_dotenv()
openai.api_key = os.getenv("OpenAI_API_KEY")  

logger.info("OpenAI_API_KEY loaded Successfully!") 


def custom_summary(docs, llm, custom_prompt, chain_type, num_summaries):
    custom_prompt = custom_prompt + """:\n {text}"""
    COMBINE_PROMPT = PromptTemplate(template=custom_prompt, input_variables = ["text"])
    MAP_PROMPT = PromptTemplate(template="Summarize:\n{text}", input_variables=["text"])

    if chain_type == "map_reduce":
        chain = load_summarize_chain(llm,chain_type=chain_type,
                                     map_prompt=MAP_PROMPT,
                                     combine_prompt=COMBINE_PROMPT)
    else:
        chain = load_summarize_chain(llm,chain_type=chain_type)
    
    summaries = []
    for i in range(num_summaries):
        summary_output = chain({"input_documents": docs}, return_only_outputs=True)["output_text"]
        summaries.append(summary_output)
    
    return summaries