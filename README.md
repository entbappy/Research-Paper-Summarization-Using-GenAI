# Research-Paper-Summarization-Using-GenAI


During research fellowship, Everyone learn how to read papers rapidly and efficiently. But just reading a paper with a minimum of 30 pages is time-consuming and it’s hard to stay on top of research with this explosion of papers released every day. To boost research productivity, wouldn’t it be better to summarize the information from academic papers? These is the following use cases that can be helpful for your career in the data science field.


# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/entbappy/Research-Paper-Summarization-Using-GenAI
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n summarizer python=3.8 -y
```

```bash
conda activate summarizer
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

### Create a `.env` file in the root directory and add your OpenAI API key as follows:

```ini
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```


```bash
# Finally run the following command
streamlit run app.py
```

Now,
```bash
open up : http://localhost:8501
```


### Techstack Used:

- Python
- LangChain
- Streamlit 
- OpenAI



### Some Promts:

```bash
summarize this paper in short

what is the main objective of this paper

summarize the paper in 3 bullet points
```

