import requests
from bs4 import BeautifulSoup
from langchain.embeddings import OpenAIEmbeddings
from openai import OpenAI


openai.api_key =''
# URL of the website to scrape

url = "https://www.adilqadri.com/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Extract all the text from the website
text = soup.get_text()
# Remove all newline characters
text = text.replace("\n", "")

# Remove all tabs
text = text.replace("\t", "")

# Remove multiple consecutive spaces
text = " ".join(text.split())

# Print the processed text
print(text)
