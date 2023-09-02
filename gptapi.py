import requests

def chatgpt(query):
    url = "https://chatgpt-gpt4-ai-chatbot.p.rapidapi.com/ask"

    payload = { "query": query }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "9c96efd56fmshc06b9a904abc023p12819ajsn89381a54c65a",
        "X-RapidAPI-Host": "chatgpt-gpt4-ai-chatbot.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.json())
    return response.json()

c=chatgpt('how to beocme rich?')
print(c['response'])
