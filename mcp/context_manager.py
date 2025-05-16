# mcp/context_manager.py
from typing import List
from mcp.message import MCPMessage

class ContextManager:
    def __init__(self):
        self.message_queue: List[MCPMessage] = []

    def send_message(self, message: MCPMessage):
        """Send a message to the queue."""
        self.message_queue.append(message)

    def get_messages_for(self, receiver: str) -> List[MCPMessage]:
        """Retrieve messages for a specific agent."""
        msgs = [m for m in self.message_queue if m.receiver == receiver]
        self.message_queue = [m for m in self.message_queue if m.receiver != receiver]
        return msgs
    
    def debug_print_messages(self):
        print("\n=== Current Messages in Queue ===")
        for msg in self.message_queue:
            print(f"{msg.sender} ➜ {msg.receiver} | {msg.task_type}")

