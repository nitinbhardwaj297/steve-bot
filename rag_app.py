import logging
import sys
from llama_index.core import VectorStoreIndex,SimpleDirectoryReader,ServiceContext,PromptTemplate
from llama_index.llms.openai import OpenAI
import llama_index 
from llama_index.core import Settings
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.readers.web import SimpleWebPageReader
from bs4 import BeautifulSoup
import requests
import re

import requests
from bs4 import BeautifulSoup


logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


# # Your HTML link
# html_link = 'https://realintelligence.com/customers/expos/00D5f000000Kf85/index-Speakerlist-mobile-iframe1.php?eventId=a0q5f0000044zma'

# # Make an HTTP request to fetch the HTML content
# response = requests.get(html_link)

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Parse the HTML content using BeautifulSoup
#     soup = BeautifulSoup(response.text, 'html.parser')
     
#     # Find all <td> elements
#     td_elements = soup.find_all('td')

#     # Extract the text content from each <td> element
#     text_content = [td.get_text(strip=True) for td in td_elements]
#     text_content_str = ' '.join(text_content)

#     # Remove extra spaces and newlines using regular expressions
#     text_content_str = re.sub(r'\s+', ' ', text_content_str).strip()

#     # Convert the list to a string
#     # text_content_str = '\n'.join(text_content)

#     # Write the text content to a text file
#     with open('output.txt', 'w', encoding='utf-8') as file:
#         file.write(text_content_str)

#     print("Text content has been written to 'output.txt'")
# else:
#     print(f"Failed to fetch HTML content. Status code: {response.status_code}")



Settings.llm = OpenAI(temperature=0.7, model="gpt-4")

documents = SimpleDirectoryReader("data").load_data()
index1 = VectorStoreIndex.from_documents(documents)

# documents1 = SimpleWebPageReader(html_to_text=True).load_data(
#     ['output.txt']
# )
# index1 = VectorStoreIndex.from_documents(documents1)
def index(query):
    query_engine = index1.as_query_engine()
    response = query_engine.query(query)
    return response










