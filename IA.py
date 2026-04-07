from langchain_ollama import OllamaLLM
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

# 1. Aponta para o arquivo que criamos
db = SQLDatabase.from_uri("sqlite:///meu_negocio.db")

# 2. Conecta ao Llama 3 que está rodando no seu terminal (ollama serve)
llm = OllamaLLM(model="llama3", temperature=0)

# 3. Cria a corrente de execução
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

# 4. Interação
print("\n--- IA Pronta. Pode perguntar sobre seus produtos! ---")
while True:
    pergunta = input("\nPergunta: ")
    if pergunta.lower() in ['sair', 'exit']: break
    try:
        db_chain.run(pergunta)
    except Exception as e:
        print(f"Erro: {e}")
