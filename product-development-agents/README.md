# Copilot Agents Team

This repository contains a set of AI agents designed to work together in a GitHub Copilot environment to deliver high-quality software.

## The Team

*   **Product Manager (`product-manager.agent.md`)**: The orchestrator. Plans the work, manages the lifecycle, and coordinates the other agents.
*   **Full Stack Staff Engineer (`full-stack-engineer.agent.md`)**: The builder. Implements features using strict TDD and best practices.
*   **Code Reviewer (`code-reviewer.agent.md`)**: The gatekeeper. Reviews code for style, security, and maintainability.
*   **QA Engineer (`qa-engineer.agent.md`)**: The tester. Runs regression tests and verifies functionality.

## Workflow

1.  **Start with the Product Manager**: Open `product-manager.agent.md` in Copilot Chat (or select the mode).
2.  **Define the Task**: Tell the PM what you want to build.
3.  **Planning**: The PM will create a plan and ask for your approval.
4.  **Execution Loop**:
    *   PM delegates to **Staff Engineer** to implement.
    *   PM delegates to **Code Reviewer** to check the code.
    *   PM delegates to **QA Engineer** to verify stability.
    *   PM asks you to **Commit** the changes.
5.  **Completion**: The PM provides a final report.

## Installation

1.  Copy the `.agent.md` files into your project's root directory or your VS Code User Data `prompts` folder.
2.  Ensure you have GitHub Copilot Chat installed in VS Code Insiders.
3.  Start chatting with the **Product Manager**!

## Requirements

*   VS Code Insiders
*   GitHub Copilot Chat
