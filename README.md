# WORKSHOP: Observe, Protect & Optimize your AI Agents With Microsoft Foundry Control Plane

## Session Description

Want to build trustworthy agentic solutions? You need end-to-end observability and security that is built-in and not bolted-on. In this workshop, we’ll look at the Foundry Control Plane in Microsoft Foundry and go hands-on with three key features - Evaluations, Tracing and Red Teaming - and build intuition for using the “Operate” tab on the Foundry portal as a command center for monitoring our deployed solutions for insights.


## Application Scenario

We'll use a familiar scenario across all labs, allowing us to think about features and outcomes in the context of a real-world use case. 

**Contoso Travel** is a fictitious mid-size travel agency whose team of human advisors can no longer keep up with the volume of customer inquiries. They need an AI-powered travel assistant — a system of intelligent agents that can search real inventory, make personalized recommendations, and plan multi-leg trips just like their best human advisors.

In this workshop, we'll look at how you can build this application with observability in focus, picking one of two potential paths for implementation.

## Getting Started

Want to just dive in? Visit the [Lab Setup](./labs/notebooks/0-setup/lab-00-setup-project.md) page to get started. But first, complete scanning the rest of this README to get more context.

## Workshop Outline

The workshop is designed in three sections:
1. Project Setup - using Foundry Portal
1. Code-First - using Foundry SDK
1. Code-First - using Foundry Skills

Complete the first section - then pick one of the two options to proceed further. You can always do the second option at a later time. _We recommend trying option 2, which was just recently released in preview_ - it is in active development (so expect some issues or changes to occur) making it a great opportunity for feedback.

**Read on to learn more about each option**

<br/>


### Project Setup - With Foundry Portal

Here's what you'll achieve by completing this lab:

1. Explore the new Foundry UI and onboarding help
1. Experience the streamlined agent creation workflow
1. Create a Foundry project with an agent, model & app insights

Then, spend a few minutes using this sample agent to explore the observability features in the Foundry portal before writing a single line of code:
- Tracing - try a test prompt - observe trace elements in portal
- Evaluations - explore default metrics - create a new evaluation run
- Red Teaming - explore risks & attacks - create a red teaming scan

**Then, it's time to move from plan to prototype** and go code-first!


### Path 1: Code-First - With Foundry SDK

Think of this as the **traditional development path** for code-first. You'll complete a structured set of notebooks that explore tracing, evaluations and red-teaming and understand the code yourself.

You will walk away with a better intution for what each feature does - and have a sandbox (notebook) you can customize to explore more on each feature. **We will use this to build a multi-agent workflow for Contoso Travel**.


### Path 2: Code-First - With Foundry Skills 🆕

Think of this as the **future development path** for code-first. 
You'll use an early preview version of Foundry Skills and see how this allows you to guide the development without having to understand the specifics of code implementation.

You will walk away with an intuition for what the new _observe_ sub-skill does - and have a sandbox you can revisit to explore further steps in this conversation, on your own. This path is non-deterministic. We may all start with the same prompt, but our next steps will be guided by our own responses to the coding agent.

Visit the [Lab Setup](./labs/notebooks/0-setup/lab-00-setup-project.md) page to get started.

<br/>

## Microsoft Foundry Tools & Experiences

Microsoft Foundry provides different tools and features to streamline developer experiences for both low-code and code-first developers. We have instrumented this repository with a _devcontainer_ that has all dependencies pre-installed so you can use this as a sandbox to explore any of the following later:

- Foundry Portal - low-code UI experience perfect for initial planning
- Foundry SDK - code-first experience perfect for complex prototyping
- AI Toolkit Extension - bring low-code UI experiences into VS Code
- Copilot for Azure Extension - bring "skills" into VS Code for coding agents
- Azure CLI & Azure Developer CLI - command-line tools to simplify infra setup

In our default paths, we prioritize _starting_ at the Foundry Portal then getting familiar with either the Foundry SDK option (traditional way) or Foundry Skills option (coding agent way) as the next step.

<br/>

## Future Work: Explore Hosted Agents

Keep an eye on the repo for updates over the next few weeks. Our goal is to add additional paths as described below - which can explore Foundry Skills and end-to-end observability workflows for _hosted agent_ implementations for the same Contoso Travel scenario.


| Approach | Path | Framework | Best For |
|----------|--------|-----------|----------|
| **Prompt Agents** | `1-prompt-agents/` | Azure AI Projects SDK | Simple agents defined via instructions + tools, no custom hosting |
| **Hosted Agents (MAF)** | `2-hosted-agents-maf/` | Microsoft Agent Framework | Custom Python agents with in-process tools, business logic, ML models |
| **Hosted Agents (LangGraph)** | `3-hosted-agents-langgraph/` | LangGraph + Foundry Adapter | Declarative graph-based agents with visual control flow and conditional routing |

One takeaway is that evaluation and red-teaming are **agent-agnostic** — they test external behavior through Responses API regardless of how hat agent was implementated. Tracing is where the **approaches differ** most, giving you progressively deeper visibility from prompt → MAF → LangGraph.


## Relevant Resources 

The figure below provides a great visual representation of the _Foundry Control Plane_ capabilities. It combines capabilities for _security, compliance, fleet management and observability_ into a unified role-aware management interface accessed through the Microsoft Foundry portal.  

In this workshop, we focus mostly on the _Observability_ features (tracing, evaluations, metrics) and explore _red teaming_ in the context of _adversarial testing_ that aligns with both evaluations (how) and security (why) components of Foundry Control Plane. Use the linked resources to learn more about individual features:

| Resource | Description |
|----------|-------------|
| [Foundry Control Plane Overview](https://learn.microsoft.com/en-us/azure/foundry/control-plane/overview?view=foundry) | Enterprise-wide visibility, governance, and control of AI agents, models & tools |
| [Observability Overview](https://learn.microsoft.com/en-us/azure/foundry/concepts/observability?view=foundry) | Monitor, understand, and troubleshoot your AI agents |
| [Agent Tracing Overview](https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-agent-concept?view=foundry) | OpenTelemetry (OTel) protocols & semantic conventions support in Foundry |
| [Evaluations Overview](https://learn.microsoft.com/en-us/azure/foundry/concepts/built-in-evaluators?view=foundry) | Built-in and custom evaluators for quality, safety & agentic performance |
| [Red Teaming Overview](https://learn.microsoft.com/en-us/azure/foundry/concepts/ai-red-teaming-agent?view=foundry) | Adversarial testing for targeted risk categories & attack strategies |

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