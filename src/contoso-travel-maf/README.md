# Contoso Travel Agent — Microsoft Agent Framework

A production-ready travel concierge agent built with the [Microsoft Agent Framework (MAF)](https://github.com/microsoft-foundry/foundry-samples/tree/main/samples/python/hosted-agents/agent-framework) for the Microsoft Foundry Agent Service. It searches Contoso Travel's flight, hotel, and car rental inventory across five destination pairs (Seattle↔Paris, NYC↔London, SF↔Tokyo, Chicago↔Rome, Denver↔Cancún), returning real pricing and availability data.

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
contoso-travel-maf/
├── agent.py           # Main agent entry point
├── agent.yaml         # Foundry deployment manifest
├── tools.py           # Flight, hotel, and car rental search tools
├── requirements.txt   # Python dependencies
├── Dockerfile         # Container build definition
├── README.md          # This file
└── data/
    ├── flights.csv    # Flight inventory
    ├── hotels.csv     # Hotel inventory
    └── car_rentals.csv  # Car rental inventory
```
