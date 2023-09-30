import openai
import requests
import json

API_KEY = "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" 
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"



# Write data to the file


def generate_chat_completion(messages, model="gpt-4", temperature=1, max_tokens=None):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }

    data = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
    }

    if max_tokens is not None:
        data["max_tokens"] = max_tokens

    response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

skillset = """{"Cierpliwosc": "5"
,"Umiejętnosci Komunikacyjne":   "3"
,"Ciagle Uczenie sie": "2"
,"Kreatywnosc": "4"
,"Myslenie Analityczne": "3"  
,"Dostosowawczosc":  "2"
,"Zarzadzanie Czasem": "2"
,"Wspolpraca":  "3"
,"Odpornosc": "4"
,"Umiejętnosci Organizacyjne" : "4"
,"Ciekawosc": "5"}"""
                

messages = [

        {"role": "user", "content": f"To jest opis jak dobre muszą być wskazabe umiejętności potrzebne dla prawnika. {skillset} Wygeneruj podobny zestaw dla zawodu informatyka zachowując te umiejętności , ale nie ich wagę którę są wskazane"}
]

print("\n")
response_text = generate_chat_completion(messages)
print(response_text)
odpowiedz = input()



#save response_text to json file with name skill[0]
print(response_text)
print("\n")


