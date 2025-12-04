# QT-GenAI MCP Tools Repository

This repository contains **two experimental MCP (Model Context Protocol) servers** built in Python for use with Claude Desktop or any MCP-compatible environment.  
It is designed as a learning and testing platform for AI-agent tool creation.

---

## 📁 Repository Structure

QT-GenAI/
├── hello_mcp/ # First MCP server demonstrating a simple addition tool
│ ├── hello.py
│ └── README.md
├── calc_mcp/ # Calculator MCP server with multiple arithmetic operations
│ ├── calc_server.py
│ ├── operations.py
│ └── README.md
├── .gitignore
└── README.md # This top-level README


---

## 🔹 hello_mcp

**Purpose:** A minimal MCP tool that demonstrates creating a single callable tool in Python.  

**Features:**
- `add(a, b)` — Adds two numbers and returns the result.
- Uses `FastMCPServer` for MCP integration.
- Compatible with Claude Desktop or any MCP client using JSON-RPC over `stdio`.

**Run the Server:**
```bash
cd hello_mcp
uv run hello.py


Test with MCP Inspector:

mcp dev hello.py

🔹 calc_mcp

Purpose: A simple calculator MCP server providing multiple arithmetic operations.

Features:

add(a, b) — Adds two numbers.

subtract(a, b) — Subtracts b from a.

multiply(a, b) — Multiplies two numbers.

divide(a, b) — Divides a by b with zero-division handling.

Uses FastMCPServer for MCP integration.

Run the Server:

cd calc_mcp
uv run calc_server.py


Test with MCP Inspector:

mcp dev calc_server.py

🛠 Requirements

Python 3.10+

mcp-server package

uv for running scripts (optional, recommended)

Claude Desktop (optional, for testing)

Install Dependencies:

uv add mcp-server

🚀 Usage Example

Call the tools using a compatible MCP client or JSON-RPC interface.

hello_mcp Example:

{ "tool": "add", "params": { "a": 2, "b": 3 } }


Returns:

{ "result": 5 }


calc_mcp Example:

{ "tool": "multiply", "params": { "a": 4, "b": 6 } }


Returns:

{ "result": 24 }

📚 Contributing

Feel free to fork this repository and create your own MCP tools.

Add new functions decorated with @mcp.tool() in each server file.

Make pull requests to share improvements.

⚠ Notes

Do not commit .venv/ — add it to .gitignore.

Each MCP server is independent and can be run separately.

Designed primarily for learning and experimentation.


---

If you want, I can also **make this README “GitHub-ready with badges, folder diagrams, and nice formatting”** so it looks very professional on your main repo page.  

Do you want me to do tha
