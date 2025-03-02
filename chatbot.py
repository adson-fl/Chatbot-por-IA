# Import 
import google.generativeai as genai
import os
from dotenv import load_dotenv 

# carregando as variaveis de ambinete do arquivo .env
load_dotenv()
# Chave
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash-latest")

