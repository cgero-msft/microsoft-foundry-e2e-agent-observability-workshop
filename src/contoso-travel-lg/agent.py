"""Contoso Travel Agent — LangGraph implementation.

This agent uses a declarative state graph with tool-calling loop:
  START → llm_call → should_continue? → tools → llm_call (loop)
                                       → END

Run locally:  python agent.py
Deploy:       azd agent deploy
"""
import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from azure.ai.agentserver.langgraph import from_langgraph
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import SystemMessage
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode

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
    """Build and compile the Contoso Travel LangGraph agent."""
    endpoint = os.environ["AZURE_AI_PROJECT_ENDPOINT"]
    model = os.environ.get("AZURE_AI_MODEL_DEPLOYMENT_NAME", "gpt-4.1-mini")

    # Azure AD auth for the LLM
    credential = DefaultAzureCredential()
    token_provider = get_bearer_token_provider(
        credential, "https://cognitiveservices.azure.com/.default"
    )

    # Extract base endpoint from project endpoint
    base_endpoint = endpoint.split("/api/projects")[0]

    llm = AzureChatOpenAI(
        azure_deployment=model,
        azure_endpoint=base_endpoint,
        azure_ad_token_provider=token_provider,
        api_version="2025-01-01",
    )

    # Bind tools to the LLM
    tools = [search_flights, search_hotels, search_car_rentals]
    llm_with_tools = llm.bind_tools(tools)

    # Define graph nodes
    def llm_call(state: MessagesState):
        """Invoke the LLM with system instructions and conversation history."""
        messages = [SystemMessage(content=INSTRUCTIONS)] + state["messages"]
        return {"messages": [llm_with_tools.invoke(messages)]}

    def should_continue(state: MessagesState):
        """Route to tools if the LLM made tool calls, otherwise end."""
        last_message = state["messages"][-1]
        if last_message.tool_calls:
            return "tools"
        return END

    # Build the graph: START → llm → (tools → llm)* → END
    graph = StateGraph(MessagesState)
    graph.add_node("llm_call", llm_call)
    graph.add_node("tools", ToolNode(tools))

    graph.add_edge(START, "llm_call")
    graph.add_conditional_edges("llm_call", should_continue, {"tools": "tools", END: END})
    graph.add_edge("tools", "llm_call")

    return graph.compile()


if __name__ == "__main__":
    agent = create_agent()
    # Serve via Foundry hosting adapter on port 8088
    from_langgraph(agent).run()
