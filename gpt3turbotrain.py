import openai
import requests
import json
import os

API_KEY = "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" 
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"
FolderPath = "F:\Git\hackyeah3\zawody"

Zawody = ["prawnik" , "informatyk" , "kierowca"]

for zawod in Zawody:
   for filename in os.scandir(FolderPath):
         with open(filename.json", "r") as f:
            data = json.load(f) 
                   
                
             mesage = {"messages": [{"role": "system", "content": "Misio is a factual chatbot that focus on giving advice regarding profession decisions"}, {"role": "user", "content": "data"}, {"role": "assistant", "content": f"{zawod}"}]}
             print mesage

