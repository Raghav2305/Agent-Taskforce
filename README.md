# 🧠 MEMAT: MCP-Enabled Multi-Agent Taskforce

MEMAT (MCP-Enabled Multi-Agent Taskforce) is a powerful agentic AI framework built using LangChain, designed to demonstrate how autonomous agents can coordinate, communicate, and complete tasks collaboratively. It leverages a structured message-passing protocol (MCP), search and summarization capabilities, and weekly scheduling to simulate a real-world multi-agent system solving complex information tasks.

---

## 🚀 Features

### 🧠 Multi-Agent Architecture

* Modular agent system built with LangChain
* Role-specific agents (SearchAgent, ReaderAgent, EmailAgent, etc.)
* Each agent has clear responsibilities and communicates using a shared memory protocol (MCP)

### 📡 Message Context Protocol (MCP)

* Custom protocol for agent-to-agent communication
* Context manager stores, retrieves, and routes messages between agents
* Enables asynchronous and autonomous agent workflows

### 🔍 Search Agent

* Uses LangChain’s tools to perform web searches
* Retrieves up-to-date results for queries like "Top GenAI research papers this week"
* Integrates with search APIs via `web_search_tool`

### 🧾 Reader Agent

* Summarizes search results into coherent, concise summaries
* Tailored for email readability and information distillation

### 📬 Email Agent

* Sends the summarized output to your email address
* Uses SMTP protocol securely via environment variables

### ⏰ Weekly Scheduler (CI/CD with GitHub Actions)

* Automatically triggers the workflow every Monday at **10:00 AM IST**
* Uses GitHub Actions and a CRON job: `'30 4 * * 1'` (UTC)

### 🛠️ Fully Testable Locally

* Each agent can be run/tested independently
* Main workflow (`app.py`) orchestrates the end-to-end agent loop

---

## 🧪 Theory Behind It

This project applies key principles from:

* **Agentic AI**: Building autonomous systems where multiple specialized agents work together to complete tasks.
* **Tool-Augmented LLMs**: Agents use external tools like web search to expand the LLM’s capabilities.
* **Memory and Context Protocols**: Inspired by biological and software-based systems where agents coordinate via structured communication.

The goal is to simulate a taskforce-like collaboration between AI agents that mirrors how real human teams operate asynchronously but in sync toward a shared objective.

---

## 🔧 Installation

```bash
git clone https://github.com/yourusername/MEMAT.git
cd MEMAT
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🧪 Local Testing

You can run the main script manually with:

```bash
python app.py
```

---

## ☁️ Deployment: GitHub Actions Scheduler

This project is integrated with GitHub Actions to run automatically every week.

`.github/workflows/memat.yml`:

```yaml
schedule:
  - cron: '30 4 * * 1'  # Every Monday at 10 AM IST (4:30 UTC)
```

It will install dependencies and execute `app.py`, triggering the full agentic loop from query to email.

---

## 🔐 Environment Variables

Create a `.env` file or set in GitHub Secrets:

```env
OPENAI_API_KEY=your_openai_api_key
EMAIL_PASSWORD=your_app_password
SERPAPI_API_KEY=your_serp_api_key
```

---

## 📬 Example Output

> You’ll receive an email like:
>
> **Subject**: “Top Research Papers in Generative AI – Week of May 13”
> **Body**: Summary of top papers, links, and highlights – automatically retrieved and summarized by MEMAT.

---

## 🧩 Project Structure

```
.
├── app.py                # Main orchestrator
├── agents/
│   ├── search_agent.py
│   ├── reader_agent.py
│   └── email_agent.py
├── mcp/
│   ├── context_manager.py
│   └── message.py
├── tools/
│   └── web_tools.py
├── .github/
│   └── workflows/
│       └── memat.yml
├── requirements.txt
└── README.md
```

---

## 💡 Future Ideas

* Add RAG pipeline for document retrieval
* Simulate product teams (PM, CTO, Researcher, Investor agents)
* Add user interface (web/mobile)
* Persistent memory and logging

---

## 💼 Use Cases

- Weekly AI news summaries for researchers
- Email digests of trending papers for busy professionals
- Template for building agentic systems with autonomous tools
- Demonstration project for LangChain + MCP-style coordination

---

## 👥 Community & Contribution

Found this project interesting?  
Feel free to fork it, modify the agents, or add new tools.

Pull requests, bug reports, and new ideas are welcome!

