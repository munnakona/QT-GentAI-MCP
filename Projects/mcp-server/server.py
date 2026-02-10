import sqlite3
from fastmcp import FastMCP
from typing import List,Dict,Any

mcp = FastMCP("ats-tools-mcp")

DB_PATH = "mcp_database.db"

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.execute('''CREATE TABLE IF NOT EXISTS ats_scores
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     job_id TEXT not NULL,
                     candidate_id TEXT not NULL,
                    ats_score REAL not null,
                    decision TEXT,
                    reason TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP''')
    conn.commit()
    return conn

@mcp.tool()

def store_ats_score(job_id: str, candidate_id: str, ats_score: float