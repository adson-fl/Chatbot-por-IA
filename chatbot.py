# Import 
import openai 
import os
from dotenv import load_dotenv 

# carregando as variaveis de ambinete do arquivo .env
load_dotenv()
# Chave
openai_api_key = os.getenv("OPENAI_API_KEY")

# teste
if openai_api_key:
   print("carregada com suecesso")
else:
    print("não foi carregada")

# Função para gera texto apartir do modelo da linguagem
def gera_texto(texto):
    
    # Obeter a resposta do modelo da linguagem 
    response = openai.completions.create(
    
      # modelo usado
      engine = "text-davinci-003",

      # Texto inicial da conversa com Chatbot
      prompt = texto,

      # Comprimento da resposta gerada pelo modelo 
      max_tokens= 150,

      # Quantas colunas gera para cada prompt.
      n = 5,

      # O texto retornado não conterá a senquicaoa de parada.
      stop= None,

      # Uma medida aleatoria gerada pelo modelo. Seu valor esta entre 0 e 1 
      # Valores mais procimo de 1 significa que a saida é mais aleatória,
      # emquanto valores mais procimo de 0 significam que a saida é muito indentificavel
      temperature=0.8
    )
    return response.choices[0].text.sprip()

