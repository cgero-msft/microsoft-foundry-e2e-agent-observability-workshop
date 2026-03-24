"""Contoso Travel Agent — Microsoft Agent Framework implementation.

This agent serves as a travel concierge, helping customers search flights,
hotels, and car rentals across Contoso Travel's inventory.

Run locally:  python agent.py
Deploy:       azd agent deploy
"""
import os
from dotenv import load_dotenv
from agent_framework import Agent
from agent_framework.azure import AzureAIAgentClient
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.agentserver.agentframework import from_agent_framework

from tools import search_flights, search_hotels, search_car_rentals

load_dotenv()

INSTRUCTIONS = """You are the Contoso Travel concierge agent. You help customers plan trips by:
- Searching real flight, hotel, and car rental inventory
- Providing specific options with prices, dates, and details
- Suggesting complete trip itineraries when asked
- Being friendly, professional, and knowledgeable

Contoso Travel operates routes between:
  Seattle ↔ Paris, NYC ↔ London, SF ↔ Tokyo, Chicago ↔ Rome, Denver ↔ Cancún

Always use the search tools to look up real data — never make up prices or availability.
When a customer asks about a destination, proactively search for relevant options."""


def create_agent():
    """Initialize and return the Contoso Travel agent."""
    endpoint = os.environ["AZURE_AI_PROJECT_ENDPOINT"]
    model = os.environ.get("AZURE_AI_MODEL_DEPLOYMENT_NAME", "gpt-4.1-mini")

    credential = DefaultAzureCredential()
    project_client = AIProjectClient(endpoint=endpoint, credential=credential)
    agent_client = AzureAIAgentClient(project_client=project_client)

    return Agent(
        client=agent_client,
        name="contoso-travel-agent",
        model=model,
        instructions=INSTRUCTIONS,
        tools=[search_flights, search_hotels, search_car_rentals],
    )


if __name__ == "__main__":
    agent = create_agent()
    # Serve via Foundry hosting adapter on port 8088
    from_agent_framework(agent).run()
