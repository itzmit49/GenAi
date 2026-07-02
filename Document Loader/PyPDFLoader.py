from langchain_community.document_loaders import PyPDFLoader

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda

load_dotenv()
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)
loader = PyPDFLoader('address of pdf file')

docs =loader.load()
print(docs)

promt=PromptTemplate(
    template='Write a summary about {topic}',
    input_variables=['topic']
)
parser=StrOutputParser()
chain = promt | model | parser

print(chain.invoke({'topic':docs[0].page_content}))

#  PyPDFLoader → Simple text PDF extraction
# PDFPlumberLoader → Best for tables and structured PDFs
# UnstructuredPDFLoader → Best for scanned/image PDFs and OCR
# PyMuPDFLoader → Best for layout, formatting, and image-aware extraction
# TextLoader → Loads .txt files
# CSVLoader → Loads CSV files
# WebBaseLoader → Loads website content
# DirectoryLoader → Loads multiple files from a folder