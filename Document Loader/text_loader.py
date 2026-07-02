from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda

load_dotenv()
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

loader = TextLoader(
    r"C:\Users\mit\OneDrive\Desktop\Langchain Models\Document Loader\cricket.txt"
)

docs = loader.load()

Prompt = PromptTemplate(
    template='Write a summary about {topic}',
    input_variables=['topic']
)


resultchain = RunnableSequence(Prompt, model, StrOutputParser())



print(resultchain.invoke({'topic': docs[0].page_content}))

