
import sys
from pathlib import Path

from langchain_mcp_adapters.client import MultiServerMCPClient

SERVER_SCRIPT = Path(__file__).parent / "servers.py"

client = MultiServerMCPClient(
    {
        "servers": {
            "command": sys.executable,
            "args": [str(SERVER_SCRIPT)],
            "transport": "stdio",
        }
    }
)


async def get_tools():
    print(await client.get_tools())
    return await client.get_tools()

