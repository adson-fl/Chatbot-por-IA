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

response = model.generate_content("quem criou os modelos de IA GEMINI ?")

 # Verificando a resposta
if response:
  print(response.text)
else:
  print("Erro: Não houve resposta do modelo.")