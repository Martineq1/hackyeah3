import openai
import requests
import json

API_KEY = "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" 
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"

# Initialize the OpenAI API client
#openai.api_key = api_key

# Function to send a message to GPT-3.5 and get a responsektor

    # Extract and return the generated message from the response


#def get_chat_response(prompt, messages):
#    # Send a message to GPT-4 and get a response
#    response = openai.Completion.create(
#        engine="text-davinci-004",
#        prompt=prompt,
#        max_tokens=1024,
#        n=1,
#        stop=None,
#        temperature=0.5,
#        messages=messages
#    )
#
#    # Extract and return the generated message from the response
#    message = response.choices[0].text.strip()
#    return message
#
## Example usage
#prompt = "What is the meaning of life?"
#messages = [
#    {"text": "I don't know, what do you think?", "user": True},
#    {"text": "I think the meaning of life is to be happy.", "user": False},
#]
#
#response = get_chat_response(prompt, messages)
#print(response)


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

skillset =     [[1 ,"Cierpliwość", "testujące cierpliwość"],
                [2 ,"Myślenie Analityczne",  "sprawdzające myślenie analityczne"],
                [3 ,"Ciągłe Uczenie się", "sprawdzające ciągłe uczenie się"],
                [4 ,"Umiejętności Komunikacyjne", "sprawdzające umiejętności komunikacyjne"],
                [5 ,"Kreatywność", "sprawdzające kreatywność"],
                [6 ,"Dostosowawczość", "sprawdzające dostosowawczość"],
                [7 ,"Zarządzanie Czasem", "umiejętność zarządzania czasem"],
                [8 ,"Współpraca", "sprawdzające umiejętność współpracy"],
                [9,"Odporność", "sprawdzające odporność psychiczną"],
                [10 ,"Umiejętności Organizacyjne", "sprawdzające umiejętności organizacyjne"],
                [11 ,"Ciekawość", "sprawdzające ciekawość"],
                [12 ,"Empatia", "sprawdzające empatię"]
                ]
for skill in skillset:
    messages = [

        {"role": "user", "content": f"\n Stwórz pytanie {skill[2]} dla nastolatka'"}
    ]
    response_text = generate_chat_completion(messages)
    print(response_text)
    odpowiedz = input()
    messages = [
        {"role": "user", "content": "\n Jak w skali 1-5 oceniasz cechę osoby, która na pytanie : " + response_text + " odpowiada: " + odpowiedz + "Odpowiedz podając jedynie liczbę"}
    ]

    print(messages[0])
    response_text = generate_chat_completion(messages)
    with open(f"{skill[1]}.json", "w") as f:
        json.dump(response_text, f)
#save response_text to json file with name skill[0]
    print(response_text)

