<h1>Guia: Llama 3 + SQL Integration</h1>


</head>
<body>

<header>
    <h1>Guia de Integração: Llama 3 & SQL</h1>
    <p>Como transformar linguagem natural em consultas de banco de dados locais.</p>
</header>

<section class="step">
    <h2>1. Instalação e Servidor</h2>
    <p>Primeiro, garanta que o Ollama está rodando no seu terminal Linux:</p>
    <pre># Iniciar o servidor
ollama serve

# Em outro terminal, baixar o modelo
ollama run llama3</pre>
</section>



<section class="step">
    <h2>2. A API do Ollama</h2>
    <p>O Ollama expõe automaticamente uma API REST na porta <code>11434</code>. Você pode testar a comunicação com este comando:</p>
    <pre>curl http://localhost:11434/api/generate -d '{
  "model": "llama3",
  "prompt": "Por que o céu é azul?",
  "stream": false
}'</pre>
</section>

<section class="step">
    <h2>3. Integração com Banco de Dados (Python)</h2>
    <p>A integração utiliza a biblioteca <strong>LangChain</strong> para conectar a API da IA ao driver do <strong>SQLite</strong>.</p>
    <pre>pip install langchain-ollama sqlalchemy</pre>
    <p>O fluxo de dados funciona assim:</p>
    <ul>
        <li>O usuário faz uma pergunta em texto.</li>
        <li>O script envia o <strong>Schema</strong> do SQL para a API.</li>
        <li>O Llama 3 retorna uma Query SQL válida.</li>
        <li>O Python executa no banco e devolve o resultado.</li>
    </ul>
</section>

<div class="warning">
    <strong>Dica de Segurança:</strong> Ao integrar APIs de IA com bancos de dados, use sempre usuários com permissão de "Apenas Leitura" (Read-Only) para evitar deleções acidentais via prompt.
</div>

<footer>
    <p style="text-align: center; color: #888;">Documentação gerada para uso local no Pop!_OS</p>
</footer>

</body>
</html>
