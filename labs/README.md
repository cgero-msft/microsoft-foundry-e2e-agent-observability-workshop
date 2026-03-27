# Workshop Guide

This workshop gives you two paths to choose from - that will take you on a developer journey to build your intuition for Microsoft Foundry Observability features in the context of a real-world scenario.

In **Path 1** you follow the tradition development route, using the Foundry SDK to write code manually. You will build a multi-agent Contoso Travel solution and explore tracing, evaluations and red-teaming capabilities in context.

In **Path 2** you follow the AI-assisted development route, using Foundry Skills with a coding agent to automate and accelerate the workflow. You will explore a more open-ended journey, starting with a recommended prompt then navigating the conversation on your own.

**Pick one path** to complete in venue - and explore the other one at your own pace later. _We recommend trying Path 2 and providing early feedback!_

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

### Path A: Prompt Agents · ~75 min

| Step | What You Do | Notebook | ~Time |
|:-----|:------------|:---------|:------|
| A.1 | Install SDK, validate environment, explore sample data | [Lab 01 — Setup](notebooks/1-prompt-agents/lab-01-setup.ipynb) | 10 min |
| A.2 | Create your first prompt agent (Contoso Travel concierge) | [Lab 02 — Agent](notebooks/1-prompt-agents/lab-02-agent.ipynb) | 10 min |
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

## 6. Skill Up — AI Toolkit Skills for Copilot

This Codespace comes with [AI Toolkit for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio) pre-installed. AI Toolkit registers **Copilot skills** — domain-specific knowledge packs that Copilot Chat activates automatically when your prompt matches their domain. You don't need to install or configure anything — just ask naturally.

### Available Skills

| Skill | What it does |
|-------|-------------|
| **microsoft-foundry** | Deploy, evaluate, trace, and manage Foundry agents end-to-end |
| **microsoft-foundry-agent-framework-code-gen** | Generate, scaffold, fix, or debug agent code using Microsoft Agent Framework SDK |

### Microsoft Foundry Skill — Sub-Skill Areas

The `microsoft-foundry` skill is organized into sub-skill areas, each with detailed reference content. These map directly to the labs in this workshop:

| Sub-Skill Area | Coverage | Workshop Labs |
|----------------|----------|---------------|
| **foundry-agent / create** | Create prompt or hosted agents, configure tools (file search, Bing grounding, Azure AI Search, MCP, memory, web search) | Lab 02 |
| **foundry-agent / deploy** | Docker build, ACR push, container start, `agent.yaml` configuration | `src/` deploy |
| **foundry-agent / invoke** | Run agents via SDK, handle streaming responses | Lab 02–03 |
| **foundry-agent / trace** | Search traces, analyze latency, analyze failures, conversation detail, KQL templates, eval correlation | Lab 04 |
| **foundry-agent / observe** | Deploy & setup monitoring, evaluate step, analyze results, compare & iterate, optimize & deploy, CI/CD monitoring | Lab 04–05 |
| **foundry-agent / eval-datasets** | Dataset curation, versioning, comparison, regression testing, trending, trace-to-dataset, seed dataset generation, eval lineage | Lab 05 |
| **foundry-agent / troubleshoot** | Diagnose deployment failures, agent errors, connectivity issues | All labs |
| **models / deploy-model** | Deploy models (preset or custom), model configuration | Lab 00 |
| **project** | Create Foundry projects, manage connections | Lab 00 |
| **resource** | Create AI Services / Foundry resources, provisioning patterns | Lab 00 |
| **rbac** | Role assignments and permissions for Foundry resources | Lab 00 |
| **quota** | Capacity planning, PTU guide, optimization, error resolution | Lab 00 |

### Example Prompts — What to Ask Copilot

These prompts activate the Foundry skill automatically. Try them in Copilot Chat during or after the labs:

| Sub-Skill Area | Example Prompt |
|----------------|---------------|
| **Tracing** | *"How do I set up OpenTelemetry tracing for my Foundry agent?"* |
| **Tracing** | *"Show me KQL queries to find slow agent responses in Azure Monitor"* |
| **Tracing** | *"Analyze the latency of my agent's tool calls"* |
| **Evaluation** | *"Run a batch evaluation for quality and safety on my agent"* |
| **Evaluation** | *"Compare evaluation results between two versions of my agent"* |
| **Eval Datasets** | *"Create an evaluation dataset from my traces"* |
| **Eval Datasets** | *"Generate a seed dataset for my Contoso Travel agent"* |
| **Observability** | *"Set up CI/CD monitoring for my deployed agent"* |
| **Deploy** | *"Deploy my MAF agent to Foundry Agent Service"* |
| **Troubleshoot** | *"My agent deployment failed — help me diagnose the issue"* |
| **Code Gen** | *"Add a hotel search tool to my MAF agent"* |
| **Code Gen** | *"Scaffold a new multi-agent workflow for Foundry"* |

### Copilot CLI — Agentic Actions from the Terminal

This Codespace also has **GitHub Copilot CLI** (`gh copilot`) available. You can ask Copilot to explain or suggest shell commands relevant to your labs. For example, after completing Lab 04 (Tracing), you might want to curate traces into an evaluation dataset for Lab 05:

```bash
# Ask Copilot CLI to help with an Azure Monitor query
gh copilot suggest "query Azure Monitor for all agent traces from the last hour"

# Or explain a command you're unsure about
gh copilot explain "az monitor app-insights query --app <resource> --analytics-query 'traces | where timestamp > ago(1h)'"
```

> **Tip: From traces to eval datasets** — One powerful workflow is using your production traces as evaluation data. After running Lab 04 (Tracing), ask Copilot:  
> *"Create an evaluation dataset from my traces"*  
> This activates the `eval-datasets / trace-to-dataset` sub-skill, which guides you through extracting real user queries and agent responses from Azure Monitor and formatting them as a `.jsonl` dataset you can feed into Lab 05 (Evaluation). This closes the loop between observability and continuous improvement.

---

## 7. Questions or Feedback?

Use the Issues tab on this repository to share questions, bugs, or suggestions. We welcome contributions — see the [Contributing](../README.md#contributing) section in the main README.
