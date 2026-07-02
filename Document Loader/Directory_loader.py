# DirectoryLoader
# Used to load multiple files from a folder at once

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path="folder_path",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs = loader.load()

print(docs)

# Problem:
# load() is slow for large directories
# because all documents are loaded into RAM at once

# Better Solution:
# Use lazy_load()
# It loads documents one by one (memory efficient)