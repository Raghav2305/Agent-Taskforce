# mcp/message.py
from pydantic import BaseModel
from typing import Optional, Dict

class MCPMessage(BaseModel):
    sender: str
    receiver: str
    task_type: str
    payload: Dict
    memory_refs: Optional[Dict] = None
