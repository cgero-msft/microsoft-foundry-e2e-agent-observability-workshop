# Lab 01: Setup Development Environment

## 1. Launch GitHub Codespaces

1. [Fork the repository](https://github.com/Azure-Samples/microsoft-foundry-e2e-agent-observability-workshop/fork) to your own profile to get your sandbox.
1. Launch GitHub Codespace on your fork.
    - Click the blue Code button in your repo (in the browser)
    - Select the Codespaces tab
    - Click Create Codespace
1. A new browser tab opens with a VS Code environment
    - Wait till the IDE is completely loaded
    - Look for the terminal to become active
    - This can take quite a few minutes to complete
1. Congratulations - your dev environment is ready.

## 2. Run Setup-Env Script

1. In the VS Code terminal, run this command:

    ```bash
    ./labs/notebooks/setup-env.sh
    ```
1. It should prompt you to log into Azure as shown. Complete this step, then let the script run till complete.
    ![Run Env Script](assets/26-run-env-script.png)

1. You should see this success message - and a `.env` file with the right variables created should now be visible in the `labs/notebooks` folder. 
    ![Dev Env Ready](assets/27-dev-env-ready.png)
1. Congratulations - your local env variables are set.

## 3. Pick Your Code-First Path

Click on this [README.md](./../1-prompt-agents/README.md) to get instructions for the two code-first paths, and pick one. For _in-venue attendees_, we recommend trying the Foundry Skills path (new, preview - expect issues) to get an early intuition for how coding agents can influence your developer workflow.