from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="microsoft/Phi-3-mini-4k-instruct",
    task="text-generation",
)

chat = ChatHuggingFace(llm=llm)

result = chat.invoke("What is the capital of France?")
print(result.content)