
import sys
from pathlib import Path

from langchain_mcp_adapters.client import MultiServerMCPClient

SERVER_SCRIPT = Path(__file__).parent / "servers.py"
PROJECT_ROOT = Path(__file__).parent.parent

client = MultiServerMCPClient(
    {
        "servers": {
            "command": sys.executable,
            "args": [str(SERVER_SCRIPT)],
            "transport": "stdio",
        },
        "filesystem": {
            "command": "npx",
            "args": [
                "-y",
                "@modelcontextprotocol/server-filesystem",
                str(PROJECT_ROOT),
            ],
            "transport": "stdio",
        },
    }
)


async def get_tools():
    return await client.get_tools()

