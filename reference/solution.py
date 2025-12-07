#!/usr/bin/env python3
"""Hello World agent with prompt and voice - Functional Pattern.

Lab 1.2 Deliverable: Demonstrates the functional approach to creating
a SignalWire AI agent with basic prompt and voice configuration.
"""

from signalwire_agents import AgentBase

agent = AgentBase(name="hello-agent")

# Add prompt configuration
agent.prompt_add_section(
    "Role",
    "You are a friendly assistant. When someone calls, "
    "greet them warmly and ask how you can help today."
)

# Add voice configuration
agent.add_language("English", "en-US", "rime.spore")

if __name__ == "__main__":
    agent.run()
