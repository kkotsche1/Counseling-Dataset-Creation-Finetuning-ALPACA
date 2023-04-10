import requests
from bs4 import BeautifulSoup
import json
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

def extract_conversation_pairs(url):
    time.sleep(1)
    request = requests.get(url)

    soup = BeautifulSoup(request.text, 'html.parser')

    conversation_pairs = []
    utterances = soup.find_all('td', {'width': '328', 'valign': 'top'})

    client_utterance = None
    for utterance in utterances:
        if utterance.find_previous('b'):
            speaker = utterance.find_previous('b').text.strip()
            if not speaker.lower().startswith('dr'):
                client_utterance = utterance.text.strip()
            elif speaker.lower().startswith('dr'):
                therapist_response = utterance.text.strip()
                if client_utterance:
                    conversation_pairs.append([client_utterance, therapist_response])
                    client_utterance = None
        else:
            if client_utterance:
                client_utterance += ' ' + utterance.text.strip()

    return conversation_pairs

url = 'http://www.thetherapist.com/Patient_Summaries.html'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

transcript_links = []

for link in soup.find_all('a'):
    if link.text == 'Transcripts':
        transcript_links.append(f"http://www.thetherapist.com/{link.get('href')}")

for index, link in enumerate(transcript_links):
  # Send a GET request to the webpage you want to extract links from
  url = link
  response = requests.get(url)
  # Parse the HTML content of the page using BeautifulSoup
  soup = BeautifulSoup(response.content, 'html.parser')
  # Find all links on the page that have "Sessions" as part of their link text

  ##CHECK LINK IF NO CONVERFSATION FOUND ##
  session_links = [f"http://www.thetherapist.com/{link['href']}" for link in soup.find_all('a') if 'Session' in link.text]
  print(session_links)
  filename = f"company_therapist_free.json"
  conversation_list = []
  # Print out the links that were found
  for link_ in session_links:
    conversation_pairs = extract_conversation_pairs(link_)

    for element in conversation_pairs:
        client = element[0]
        response = element[1]

        conversation_list.append(
            {
                "instruction": client,
                "input": "",
                "output": response
            }
        )
  if len(conversation_list) == 0:
      print(link)
  if len(conversation_list) > 0:
      print(len(conversation_list))
      with open(filename, "w") as json_file:
        json.dump(conversation_list, json_file)

