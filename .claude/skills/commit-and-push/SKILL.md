---
name: commit-and-push
description: Commit all staged changes and push to GitHub
disable-model-invocation: false
context: fork
agent: commit-push-agent
allowed-tools: Bash(git:*)
---

# Commit and Push

Delegate to the commit-push-agent (runs on Haiku).

## Arguments

Pass a custom message: `/commit-and-push "feat: add job scraper"`
If no message is provided, the agent will generate one from the diff.
