# WORKSHOP: Observe, Protect & Optimize your AI Agents With Microsoft Foundry Control Plane

## Session Description

Want to build trustworthy agentic solutions? You need end-to-end observability and security that is built-in and not bolted-on. In this workshop, we’ll look at the Foundry Control Plane in Microsoft Foundry and go hands-on with three key features - Evaluations, Tracing and Red Teaming - and build intuition for using the “Operate” tab on the Foundry portal as a command center for monitoring our deployed solutions for insights.

<br/>

## Application Scenario

This workshop uses a **Contoso Travel** scenario to ground every lab in a realistic use case. Contoso Travel is a mid-size travel agency whose team of human advisors can no longer keep up with the volume of customer inquiries. They need an AI-powered travel assistant — a system of intelligent agents that can search real inventory, make personalized recommendations, and plan multi-leg trips just like their best human advisors.

We build a **multi-agent system** with four specialist agents:

- 🧑‍💼 **Concierge Agent** — the front desk, greeting customers and understanding their travel needs
- ✈️ **Flight Agent** — searches Contoso's flight inventory across 5 route pairs (Seattle↔Paris, NYC↔London, SF↔Tokyo, Chicago↔Rome, Denver↔Cancún)
- 🏨 **Hotel Agent** — finds hotels across 5 destination cities by star rating, price, and amenities
- 🚗 **Car Rental Agent** — looks up rental vehicles by city, type, and availability

Building the agents is only the beginning. Getting them **production-ready** requires an end-to-end workflow:

- **Create** — define agents with instructions and connect them to real data via function tools
- **Orchestrate** — compose specialist agents into a multi-agent workflow so they collaborate on complex requests
- **Trace** — instrument the system with OpenTelemetry so you can see exactly what happens inside every interaction
- **Evaluate** — systematically measure quality (fluency, coherence, task adherence) and safety at scale with built-in evaluators
- **Red-Team** — stress-test with adversarial attacks (jailbreaks, encoded prompts, crescendo attacks) to find vulnerabilities before your users do

Each lab walks you through one of these steps, building on the previous one, so you experience the full journey from first agent to production-ready system — and get a sandbox where you can explore new ideas (different attacks, custom evaluators, additional agents) on your own.

<br/>

## Implementation Approaches

This workshop implements the Contoso Travel scenario using **three different approaches**, so you can compare trade-offs and pick the right tool for your use case:

| Approach | Folder | Framework | Best For |
|----------|--------|-----------|----------|
| **Prompted Agents** | `1-prompt-agents/` | Azure AI Projects SDK | Simple agents defined via instructions + tools, no custom hosting |
| **Hosted Agents (MAF)** | `2-hosted-agents-maf/` | Microsoft Agent Framework | Custom Python agents with in-process tools, business logic, ML models |
| **Hosted Agents (LangGraph)** | `3-hosted-agents-langgraph/` | LangGraph + Foundry Adapter | Declarative graph-based agents with visual control flow and conditional routing |

### What You Learn from Each

- **Prompted Agents** — The fastest path to a working agent. You define instructions and tools via the SDK, and Foundry handles execution. Great for learning the core concepts (tracing, evaluation, red teaming) without infrastructure concerns.
- **Hosted Agents (MAF)** — Full control over agent logic. Your Python code runs inside the agent process, giving you in-process tool execution, custom business logic, and direct database access. You learn how custom code affects observability.
- **Hosted Agents (LangGraph)** — Declarative control flow as a graph. Nodes are functions, edges define routing, and the graph structure itself becomes visible in traces. You learn how graph-based architectures provide the richest observability.

**Key insight:** 

Evaluation and red teaming are **agent-agnostic** — they test external behavior through Responses API regardless of implementation. Tracing is where the **approaches differ** most, giving you progressively deeper visibility from prompted → MAF → LangGraph.

<br/>

## Learning Objectives

By completing this workshop, you should be able to get a better sense for the Microsoft Foundry Observability tooling and end-to-end developer workflows. Specifically, you should be able to:

1. Navigate the Microsoft Foundry portal experience to create & manage projects
1. Create, observe & optimize _prompted agents_ from portal or SDK
1. Create, observe & optimize _hosted agents_ from VS Code (via CLI, extension or SDK)
1. Understand tracing features & workflows (for debugging or observing agent execution)
1. Understand evaluation features & workflows (for assessing quality, safety & agentic performance)
1. Understand red-teaming features & workflows (for adversarial testing for diverse risks & attacks)
1. Understand and use core developer tools (AI Toolkit, Azure Dev CLI, Foundry SDK, Foundry portal)

We also encourage the use of this repository as a sandbox to explore "more" labs beyond the in-venue session time limits.

<br/>

## Getting Started

This workshop is setup for _self-guided learning using your own Azure subscription_. Visit the [Workshop Guide](./labs/README.md) page to get started, then follow the session outline to complete "core" labs in-venue. The repository also contains "more" labs that you can explore in your own time, later.

## Relevant Resources 

The Microsoft Foundry Control Plane giving you centralized control and oversight over your AI agent fleet - from planning ("Discover") to prototype ("Build") to production ("Operate") stages of your workflow. As shown in the figure, it combines capabilities for _security, compliance, fleet management and observability_ into a unified role-aware management interface accessed through the Microsoft Foundry portal.  In this workshop, we focus mostly on the _Observability_ features (tracing, evaluations, metrics) and explore related aspects like _red teaming_ that contribute to other capabilities like Security and Compliance.



Explore these resources to learn more:

1. [Foundry Control Plane Overview](https://learn.microsoft.com/en-us/azure/foundry/control-plane/overview?view=foundry) - learn to get enterprise-wide visibility, governance, and control of AI agents, models & tools
1. [Observability Overview](https://learn.microsoft.com/en-us/azure/foundry/concepts/observability?view=foundry) - learn about the ability to monitor, understand, and troubleshoot, your AI agents
1. [Agent Tracing Overview](https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-agent-concept?view=foundry) - learn about OpenTelemetry (OTel) protocols & semantic conventions support in Foundry
1. [Evaluations Overview](https://learn.microsoft.com/en-us/azure/foundry/concepts/built-in-evaluators?view=foundry) - learn about support for built-in and custom evaluators for quality, safety & agentic performance
1. [Red Teaming Overview](https://learn.microsoft.com/en-us/azure/foundry/concepts/ai-red-teaming-agent?view=foundry) - learn about support for adversarial testing for targeted risk categories & attack strategies

![FCP](./labs/assets/foundry-control-plane.png)

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit [Contributor License Agreements](https://cla.opensource.microsoft.com).

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must follow
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.