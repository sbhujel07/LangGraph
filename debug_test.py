#!/usr/bin/env python3
"""Debug script to test the ReAct graph"""

import sys
sys.path.insert(0, r"d:\Transformer_All\LangGraph_Tutorial")

from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

@tool
def Duck_Search(query: str) -> str:
    '''Search using DuckDuckGo'''
    duck_search = DuckDuckGoSearchRun()
    return duck_search.invoke(query)

# Test the conditional function logic
ai_msg = AIMessage(content="Let me search for that information. \nDuck_Search: latest AI news")

content = ai_msg.content.lower()
print(f"Content: {repr(ai_msg.content)}")
print(f"Content (lowered): {repr(content)}")

tool_names = ["duck_search", "wikipedia_search", "custom_tool"]

# Check each pattern
for tool in tool_names:
    pattern = f"{tool}:"
    found = pattern in content
    print(f"Looking for '{pattern}': {found}")

# Check full condition
has_tool_call = (
    any(f"{tool}:" in content for tool in tool_names) or
    "<tool_use>" in content or
    any(f"{tool}(" in content for tool in tool_names)
)

print(f"\nFinal has_tool_call: {has_tool_call}")
print(f"Should route to: {'tool_node' if has_tool_call else 'end'}")
