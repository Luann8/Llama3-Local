<h1>🧠 Llama 3 + LLaVA + SQLite Integration Guide</h1>

<p>
This guide shows how to connect a locally running <strong>Llama 3 model (via Ollama)</strong> to a SQLite database, including support for <strong>image understanding using LLaVA</strong>, enabling natural language queries (NL → SQL + Vision).
</p>

<hr>

<h2>⚙️ 1. Install and Configure Ollama</h2>

<h3>📥 Install (Linux - works on all distros: Ubuntu, Pop!_OS, Arch, etc.)</h3>

<pre><code>curl -fsSL https://ollama.com/install.sh | sh</code></pre>

<p>Verify installation:</p>

<pre><code>ollama --version</code></pre>

<h3>▶️ Start the service</h3>

<pre><code>ollama serve</code></pre>

<div class="note">
⚠️ This command must remain running in the background.
</div>

<hr>

<h2>📦 2. Download AI Models</h2>

<h3>🧠 Llama 3 (Text Model)</h3>

<pre><code>ollama pull llama3</code></pre>

<h3>👁️ LLaVA (Vision Model - Image Understanding)</h3>

<pre><code>ollama pull llava</code></pre>

<p>You can run them directly:</p>

<pre><code>ollama run llama3
ollama run llava</code></pre>

<hr>

<h2>🧪 3. Installation Test (CRITICAL STEP)</h2>

<h3>📄 teste_ia.py</h3>

<pre><code>from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")

try:
    resposta = llm.invoke("Hello, are you ready to work with SQL?")
    print("✅ CONNECTION TEST: SUCCESS!")
    print("AI Response:", resposta)
except Exception as e:
    print("❌ CONNECTION ERROR")
    print(e)
</code></pre>

<hr>

<h2>📸 4. Image Test (LLaVA)</h2>

<h3>📄 teste_imagem.py</h3>

<pre><code>from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llava")

response = llm.invoke("Describe this image: /path/to/image.jpg")

print(response)
</code></pre>

<hr>

<h2>📦 5. Install Python Dependencies</h2>

<pre><code>pip install langchain langchain-ollama sqlalchemy langchain-experimental</code></pre>

<hr>

<h2>🔗 6. SQLite + LLM Integration</h2>

<h3>📄 main.py</h3>

<pre><code>from langchain_ollama import OllamaLLM
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

db = SQLDatabase.from_uri("sqlite:///dados.db")
llm = OllamaLLM(model="llama3")

db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

response = db_chain.run("What is the most expensive product in the sales table?")

print("Answer:", response)
</code></pre>

<hr>

<h2>🧠 Example Questions</h2>

<ul>
    <li>What is the most expensive product?</li>
    <li>List all products</li>
    <li>What is the average price?</li>
    <li>How many products are there?</li>
</ul>

<hr>

<h2>⚠️ Common Issues</h2>

<h3>❌ Cannot connect to Ollama</h3>

<pre><code>ollama serve</code></pre>

<p>Check endpoint:</p>

<pre><code>http://localhost:11434</code></pre>

<h3>🔥 Firewall issues (Linux)</h3>

<pre><code>sudo ufw allow 11434</code></pre>

<p>Works on all Linux distributions including Ubuntu, Pop!_OS and Arch Linux.</p>

<hr>

<h2>🚀 Conclusion</h2>

<p>You now have a full local AI system capable of:</p>

<ul>
    <li>🧠 Running LLMs locally (Llama 3)</li>
    <li>👁️ Understanding images (LLaVA)</li>
    <li>🗄️ Querying SQLite using natural language</li>
    <li>🔒 Fully offline AI workflow (no external APIs)</li>
    <li>🐧 Compatible with all major Linux distributions</li>
</ul>
