# Contoso Travel Agent — LangGraph

A production-ready travel concierge agent built with [LangGraph](https://github.com/langchain-ai/langgraph) for the Microsoft Foundry Agent Service. The agent uses a declarative state graph with a tool-calling loop to search real flight, hotel, and car rental inventory from CSV data files, providing customers with specific options, prices, and complete trip itineraries.

## Graph Structure

```
START → llm_call → should_continue? ─→ tools → llm_call (loop)
                                     └→ END
```

## Prerequisites

- Python 3.11+
- Azure subscription with an AI Foundry project
- Model deployment (default: `gpt-4.1-mini`)
- Foundry Agent Service access (`azd` CLI installed)

## Quick Start

### Local Run

```bash
# Set required environment variables
export AZURE_AI_PROJECT_ENDPOINT="https://<your-endpoint>/api/projects/<project-id>"
export AZURE_AI_MODEL_DEPLOYMENT_NAME="gpt-4.1-mini"  # optional, this is the default

# Install dependencies
pip install -r requirements.txt

# Run the agent
python agent.py
```

### Deploy to Foundry Agent Service

```bash
azd agent deploy
```

## Environment Variables

| Variable | Required | Description |
|---|---|---|
| `AZURE_AI_PROJECT_ENDPOINT` | Yes | Full Microsoft Foundry project endpoint |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | No | Model deployment name (default: `gpt-4.1-mini`) |

## Project Structure

```
contoso-travel-lg/
├── agent.py           # Main agent entry point with StateGraph
├── agent.yaml         # Foundry deployment manifest
├── tools.py           # @tool-decorated search functions
├── requirements.txt   # Python dependencies
├── Dockerfile         # Container build definition
├── README.md          # This file
└── data/
    ├── flights.csv    # Flight inventory
    ├── hotels.csv     # Hotel inventory
    └── car_rentals.csv  # Car rental inventory
```
