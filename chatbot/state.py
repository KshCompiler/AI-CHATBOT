from typing import Annotated, List

from langgraph.graph.message import add_messages
from pydantic import BaseModel


class State(BaseModel):
    messages: Annotated[List, add_messages]
