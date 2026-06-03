from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()

st.header("Research Paper Explainer")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)"
    ]
)

template = PromptTemplate(
    input_variables=["paper_name", "style", "length"],
    template="""
You are an expert AI researcher and teacher.

Research Paper: {paper_name}

Explanation Style: {style}

Explanation Length: {length}

Explain the paper with the following structure:

1. Overview
2. Problem the paper solves
3. Key ideas
4. Methodology
5. Results and impact
6. Conclusion

Adapt your explanation according to the selected style and length.
"""
)

if st.button("Submit"):

    prompt = template.format(
        paper_name=paper_input,
        style=style_input,
        length=length_input
    )

    result = llm.invoke(prompt)

    st.write(result.content)