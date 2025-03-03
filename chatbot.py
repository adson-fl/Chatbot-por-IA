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

def apresentacao():
  print("Bem-Vindo ao projeto Chatbot")
  print("Digite 'sair' a qualquer momento para encerra o Chat")

def main():

  apresentacao()

  # Lista de Historico de Chats
  chat = model.start_chat(history=[])

  while True:

    # Pergunta digitada
    user_pergunta = input("\nVocê:")

    # Condição de finalização 
    if user_pergunta.lower() == "sair":
      break

    # Formatação de Saida
    gemini_bot = f"\nUsuário: {user_pergunta}\nChatbot:"

    # Enviando pergunta e guardando na lista
    response = chat.send_message(gemini_bot)

    print(f"\nChatbot:{response.text}")

if __name__ == "__main__":
  main()

    
