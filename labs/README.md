# Workshop Guide

This workshop takes you on an end-to-end developer journey — from creating your first AI agent to tracing, evaluating, and red-teaming it before production. You'll build the **Contoso Travel** multi-agent system using one of three implementation approaches, then apply observability and security best practices that work across all of them.

**You will need your own Azure subscription** to complete this workshop.

---

## 1. Pre-Requisites

1. **GitHub account** → We use GitHub Codespaces for a consistent dev environment.
1. **Active Azure subscription** → With permissions to create AI Services and Foundry projects.
1. **Familiarity with Python and Jupyter Notebooks** → GitHub Copilot can help!

This repository includes a `devcontainer.json` for automated setup. **We recommend GitHub Codespaces for fast, consistent setup** — all tools, extensions, and dependencies are pre-installed.

---

## 2. Getting Started

1. **Fork this repo** → Navigate to the fork link and complete the workflow. You now have a personal sandbox.
1. **Launch GitHub Codespaces** from your fork → Opens VS Code in a new browser tab.
1. **Wait for setup to complete** → Verify extensions are installed and the terminal is active.
1. **Complete Lab 00 (Setup)** → This creates the Foundry project, deploys a model, and configures environment variables. **This step is shared across all paths.**

Once Lab 00 is done, pick your implementation path below. [Read about the implementations here](PATHS.md)

---

## 3. Session Outline

### Phase 0: Setup (Shared — All Paths) · ~15 min

Complete this first regardless of which path you choose.

| Step | What You Do | Notebook |
|:-----|:------------|:---------|
| 0.1 | Fork repo, launch Codespaces, wait for setup | _(see Getting Started above)_ |
| 0.2 | Create Foundry project, deploy model, enable App Insights, configure `.env` | [Lab 00 — Setup](notebooks/0-setup/lab-00-setup.ipynb) |

---

### Path A: Prompted Agents · ~75 min

| Step | What You Do | Notebook | ~Time |
|:-----|:------------|:---------|:------|
| A.1 | Install SDK, validate environment, explore sample data | [Lab 01 — Setup](notebooks/1-prompt-agents/lab-01-setup.ipynb) | 10 min |
| A.2 | Create your first prompted agent (Contoso Travel concierge) | [Lab 02 — Agent](notebooks/1-prompt-agents/lab-02-agent.ipynb) | 10 min |
| A.3 | Add function tools for flight, hotel, and car rental search | [Lab 03a — Tools](notebooks/1-prompt-agents/lab-03a-tools.ipynb) | 10 min |
| A.4 | Orchestrate specialist agents into a multi-agent workflow | [Lab 03b — Workflow](notebooks/1-prompt-agents/lab-03b-workflow.ipynb) | 10 min |
| A.5 | Instrument with OpenTelemetry tracing (console + Azure Monitor) | [Lab 04 — Tracing](notebooks/1-prompt-agents/lab-04-tracing.ipynb) | 10 min |
| A.6 | Run quality and safety evaluations at scale | [Lab 05 — Evaluation](notebooks/1-prompt-agents/lab-05-evaluation.ipynb) | 15 min |
| A.7 | Red-team with adversarial attacks (jailbreak, crescendo) | [Lab 06 — Red Teaming](notebooks/1-prompt-agents/lab-06-redteam.ipynb) | 10 min |

---

### Path B: Hosted Agents — Microsoft Agent Framework (MAF) · ~75 min

| Step | What You Do | Notebook | ~Time |
|:-----|:------------|:---------|:------|
| B.1 | Install MAF SDK, understand hosted agent architecture | [Lab 01 — Setup](notebooks/2-hosted-agents-maf/lab-01-setup.ipynb) | 10 min |
| B.2 | Build a custom concierge agent with `BaseAgent` | [Lab 02 — Agent](notebooks/2-hosted-agents-maf/lab-02-agent.ipynb) | 15 min |
| B.3 | Add local function tools with `Annotated` type hints | [Lab 03 — Tools](notebooks/2-hosted-agents-maf/lab-03-tools.ipynb) | 10 min |
| B.4 | Trace hosted agents (auto-instrumentation + custom spans) | [Lab 04 — Tracing](notebooks/2-hosted-agents-maf/lab-04-tracing.ipynb) | 15 min |
| B.5 | Evaluate quality and safety (same API, same evaluators) | [Lab 05 — Evaluation](notebooks/2-hosted-agents-maf/lab-05-evaluation.ipynb) | 15 min |
| B.6 | Red-team the hosted agent (same attacks, same methodology) | [Lab 06 — Red Teaming](notebooks/2-hosted-agents-maf/lab-06-redteam.ipynb) | 10 min |

> **Deploy first?** The production-ready app is in `src/contoso-travel-maf/`. Run `bash deploy.sh` to deploy to Foundry Agent Service before starting the tracing/eval/redteam labs.

---

### Path C: Hosted Agents — LangGraph · ~75 min

| Step | What You Do | Notebook | ~Time |
|:-----|:------------|:---------|:------|
| C.1 | Install LangGraph SDK, understand graph-based architecture | [Lab 01 — Setup](notebooks/3-hosted-agents-langgraph/lab-01-setup.ipynb) | 10 min |
| C.2 | Build a concierge agent as a `StateGraph` | [Lab 02 — Agent](notebooks/3-hosted-agents-langgraph/lab-02-agent.ipynb) | 15 min |
| C.3 | Add `@tool` nodes with conditional routing | [Lab 03 — Tools](notebooks/3-hosted-agents-langgraph/lab-03-tools.ipynb) | 10 min |
| C.4 | Trace graph execution (node spans, edge routing, state changes) | [Lab 04 — Tracing](notebooks/3-hosted-agents-langgraph/lab-04-tracing.ipynb) | 15 min |
| C.5 | Evaluate quality and safety (same API, three-way comparison) | [Lab 05 — Evaluation](notebooks/3-hosted-agents-langgraph/lab-05-evaluation.ipynb) | 15 min |
| C.6 | Red-team and complete the workshop | [Lab 06 — Red Teaming](notebooks/3-hosted-agents-langgraph/lab-06-redteam.ipynb) | 10 min |

> **Deploy first?** The production-ready app is in `src/contoso-travel-lg/`. Run `bash deploy.sh` to deploy to Foundry Agent Service before starting the tracing/eval/redteam labs.

---

### Teardown · ~5 min

When you're done, clean up your Azure resources:

1. **Delete the resource group** containing your Foundry project
2. **Verify model deployments were released** (check the Models + endpoints page)
3. **Stop your Codespace** (or it will auto-stop after idle timeout)

---

## 6. Questions or Feedback?

Use the Issues tab on this repository to share questions, bugs, or suggestions. We welcome contributions — see the [Contributing](../README.md#contributing) section in the main README.
