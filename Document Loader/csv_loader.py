# CSVLoader
# Used to load data from CSV files

from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path="path_to_csv_file.csv"
)

data = loader.load()

print(data[0].page_content)

# Pros:
# - Simple and easy to use
# - Converts CSV rows into documents
# - Useful for RAG with tabular data
# - Good for datasets, analytics, and structured records

# Cons:
# - Not ideal for very large CSV files
# - Complex table relationships are not preserved well
# - No advanced data analysis
# - Mostly treats rows as text documents