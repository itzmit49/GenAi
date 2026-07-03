# Meaning based text splitter

from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

text_splitter = SemanticChunker(
    OpenAIEmbeddings(),
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1
)

sample = """
The SemanticChunker is a class that allows for splitting text into smaller chunks based on semantic meaning. It is particularly useful for processing large documents or texts that need to be divided into manageable pieces for analysis or further processing.
"""

result = text_splitter.split_text(sample)

print(result[0])