# Chatbot com Inteligência Artificial

Este projeto faz parte da conclusão do curso **Fundamentos de Linguagem Python Para Análise de Dados e Data Science** da Data Science Academy. Inicialmente, o chatbot seria desenvolvido com a API da OpenAI, porém, devido a questões de custo e necessidade, foi adaptado para utilizar a API **Google Gemini**.

## Descrição do Projeto

O Chatbot desenvolvido utiliza a API **Google Gemini** para gerar respostas inteligentes a partir das mensagens enviadas pelo usuário. O código implementa um loop de interação que permite a conversa contínua, mantendo o histórico do chat para um contexto mais fluido.

## Funcionalidades

- Inicializa um chatbot baseado na API **Google Gemini**.
- Mantém um histórico de conversa para melhorar a coerência das respostas.
- Permite que o usuário encerre a conversa digitando `sair`.
- Formata a saída de maneira clara e organizada.

## Tecnologias Utilizadas

- **Python**
- **Google Gemini API**
- **Biblioteca dotenv** (para carregamento seguro da chave da API)

## Como Executar o Projeto

1. Clone este repositório:
   ```sh
   git clone https://github.com/seu-usuario/chatbot-gemini.git
   ```
2. Acesse a pasta do projeto:
   ```sh
   cd chatbot-gemini
   ```
3. Crie um ambiente virtual (opcional, mas recomendado):
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```
4. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
5. Crie um arquivo `.env` e adicione sua chave de API:
   ```
   GEMINI_API_KEY=suachaveaqui
   ```
6. Execute o chatbot:
   ```sh
   python chatbot.py
   ```

## Possíveis Melhorias Futuras

- Implementar uma interface gráfica para tornar o chatbot mais interativo.
- Melhorar o tratamento de erros e respostas inválidas.
- Adicionar suporte para múltiplos modelos de IA.
- Criar uma versão que utilize APIs de voz.

## Conclusão

Este projeto demonstrou o uso prático da API **Google Gemini** para construir um chatbot interativo e funcional. Ele pode ser expandido e adaptado para diversas aplicações, incluindo assistentes virtuais, suporte automatizado e muito mais.

