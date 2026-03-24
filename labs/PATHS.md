# Implementation Approaches

This workshop implements the same Contoso Travel scenario three different ways. Each path is a complete end-to-end journey that can be finished in **~75 minutes** (after setup). Pick the one that matches your interest, then explore the others as time permits.

| Approach | Folder | What You Build | Best For |
|----------|--------|---------------|----------|
| **Prompted Agents** | `1-prompt-agents/` | Agents defined via SDK instructions + function tools | Fastest path — no custom hosting, learn core observability concepts |
| **Hosted Agents (MAF)** | `2-hosted-agents-maf/` | Custom Python agents with in-process tools | Full control — custom business logic, ML models, direct data access |
| **Hosted Agents (LangGraph)** | `3-hosted-agents-langgraph/` | Declarative graph-based agents with conditional routing | Visual control flow — graph topology visible in traces |


> **Key insight:** 
> Evaluation and red teaming work identically across all three approaches — they test external behavior through the Responses API. 
> Tracing is where the approaches differ, giving progressively deeper visibility from prompted → MAF → LangGraph.

---

## Workshop Architecture

### Notebooks vs. Source Code

This repo contains **two independent codebases** that implement the same Contoso Travel scenario:

| | `labs/notebooks/` | `src/contoso-travel-maf/` and `src/contoso-travel-lg/` |
|---|---|---|
| **Purpose** | Educational walkthrough — build an agent step-by-step | Production-ready agent for deployment to Foundry Agent Service |
| **Runs where** | Locally in the notebook kernel | Deployed to Foundry via `deploy.sh` |
| **Contains** | Tools defined inline, agent built in-process | Self-contained app: `agent.py`, `tools.py`, `agent.yaml`, `Dockerfile` |
| **Requires the other?** | No | No |

They share no imports — the notebooks are self-contained learning exercises, `src/` is deployable production code.

## What Each Lab Targets

| Lab | What Happens | Runs Against |
|---|---|---|
| **01 Setup** | Install SDKs, validate `.env`, explore data | Local environment |
| **02 Agent** | Build a concierge agent (MAF `BaseAgent` or LangGraph `StateGraph`) | **Local** — `agent.run()` in-process |
| **03 Tools** | Add flight/hotel/car search tools, test queries | **Local** — tools execute in-process |
| **04 Tracing** | Configure OpenTelemetry, trace a query to console + Azure Monitor | **Foundry** — creates a `PromptAgentDefinition` on Foundry |
| **05 Evaluation** | Run quality (fluency, coherence, task adherence) and safety evaluators | **Foundry** — creates a `PromptAgentDefinition` on Foundry |
| **06 Red Team** | Run adversarial attacks (jailbreak, crescendo) | **Model endpoint** — targets the deployed model directly |

> **Why do Labs 04-06 use `PromptAgentDefinition` instead of the custom agent from Lab 02?**
> This is intentional. Labs 04-06 demonstrate that tracing, evaluation, and red teaming are **agent-agnostic** — they work through the Responses API regardless of whether the agent is a prompted agent, a MAF `BaseAgent`, or a LangGraph `StateGraph`. The framework doesn't matter at the observability layer.

## Two Testing Flows

**Flow 1: Full Learning Path** (recommended for first-time users)

Run Labs 01-06 sequentially. Labs 01-03 teach you to build locally, Labs 04-06 teach observability against Foundry-hosted agents. No deployment needed — the notebooks create lightweight agents on-the-fly.

```
Lab 00 (Setup) → Lab 01 → Lab 02 → Lab 03 → Lab 04 → Lab 05 → Lab 06
                  ──── build locally ────   ── observe on Foundry ──
```


**Flow 2: Deploy First, Then Observe** (for production-focused testing)

If you want to skip the build-from-scratch labs and go straight to observability against a **production-deployed agent**:

1. **Complete Lab 00** — Create Foundry project, deploy model, configure `.env`
2. **Deploy the production agent:**
   ```bash
   # For MAF:
   cd src/contoso-travel-maf && bash deploy.sh

   # For LangGraph:
   cd src/contoso-travel-lg && bash deploy.sh
   ```
3. **Run Labs 04-06 directly** — These labs create their own test agents via `PromptAgentDefinition`, so they work independently. If you want to trace/evaluate/red-team your *deployed* agent instead, update the agent name/version in the notebook cells to point to your deployed agent.

> **Note:** Labs 04-06 are designed to be self-contained — they create and clean up their own agents. The `src/` deployment gives you a persistent production agent you can also test against from the Foundry portal UI.
