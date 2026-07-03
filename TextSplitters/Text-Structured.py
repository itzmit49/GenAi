from  langchain_text_splitters import RecursiveCharacterTextSplitter

text="""
The RecursiveCharacterTextSplitter is a class that allows for splitting text into smaller chunks based on character count. It is particularly useful for processing large documents or texts that need to be divided into manageable pieces for analysis or further processing."""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
   
)

result = splitter.split_text(text)

print(result[0])