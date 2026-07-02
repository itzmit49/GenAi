# WebBaseLoader
# Used to extract and load content from a webpage (URL)

from langchain_community.document_loaders import WebBaseLoader

url = "https://unstop.com/hackathons/crp-amazon-ml-summer-school-2026-amazon-1688859/online-assessment/439416"

loader = WebBaseLoader(url)

docs = loader.load()

print(docs[0].page_content)

# WebBaseLoader
# Used to extract and load content from webpages (URLs)

# Useful for:
# - Web scraping
# - RAG applications
# - Website summarization
# - Chatting with website data

# Limitation:
# - Works mainly with static HTML websites
# - Cannot properly handle JavaScript-rendered websites

# Better Alternative:
# - Use Selenium or Playwright for JS-heavy websites
# - They can render JavaScript and dynamic content