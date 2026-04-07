<h1>🧠 Llama 3 + SQLite Integration Guide</h1>

<p>This guide shows how to connect a locally running <strong>Llama 3 model (via Ollama)</strong> to a SQLite database, enabling natural language queries (NL → SQL).</p>

<hr>

<h2>⚙️ 1. Install and Configure Ollama</h2>

<h3>📥 Install (Linux - Pop!_OS / Ubuntu)</h3>
<pre><code>curl -fsSL https://ollama.com/install.sh | sh</code></pre>

<p>Verify installation:</p>
<pre><code>ollama --version</code></pre>

<h3>▶️ Start the service</h3>
<pre><code>ollama serve</code></pre>

<div class="note">
⚠️ This command must remain running in the background.
</div>

<h3>📦 Download the Llama 3 model</h3>
<pre><code>ollama pull llama3</code></pre>

<p>Or run directly:</p>
<pre><code>ollama run llama3</code></pre>

<hr>

<h2>🧪 2. Installation Test (CRITICAL STEP)</h2>

<p>Create a test file to ensure Python can communicate with Ollama.</p>

<h3>📄 teste_ia.py</h3>

<pre><code>from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")

try:
    resposta = llm.invoke("Hello, are you ready to work with SQL?")
    print("✅ CONNECTION TEST: SUCCESS!")
    print("AI Response:", resposta)
except Exception as e:
    print("❌ CONNECTION ERROR")
    print("Make sure 'ollama serve' is running.")
    print(e)
</code></pre>

<hr>


<p>Run:</p>
<pre><code>python setup_db.py</code></pre>

<hr>

<h2>📦 3. Install Python Dependencies</h2>

<pre><code>pip install langchain langchain-ollama sqlalchemy langchain-experimental</code></pre>

<hr>

<h2>🔗 4. Final Integration</h2>

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

<p>Run:</p>
<pre><code>python main.py</code></pre>

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

<p>Check default endpoint:</p>
<pre><code>http://localhost:11434</code></pre>

<h3>🔥 Firewall issues</h3>
<pre><code>sudo ufw allow 11434</code></pre>

<hr>

<h2>✅ Conclusion</h2>

<p>You now have a system capable of:</p>

<ul>
    <li>Running AI locally (no external APIs)</li>
    <li>Querying databases using natural language</li>
    <li>Automatically generating SQL queries</li>
</ul>
