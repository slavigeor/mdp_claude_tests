---
name: commit-and-push
description: Commit all staged changes and push to GitHub
disable-model-invocation: true
allowed-tools: Bash(git:*)
---

# Commit and Push

## Steps

1. Run `git status` and `git diff --staged` to show what will be committed
2. If there are unstaged files, ask the user which to add
3. Create a commit message using conventional commits (feat:, fix:, docs:, refactor:)
4. Show the commit message and ask for approval
5. Commit and push to origin

## Arguments

Pass a custom message: `/commit-and-push "feat: add job scraper"`
If no message is provided, generate one from the diff.

## Rules

- Never force push
- Always show changes and ask for confirmation before pushing
- Use Haiku as a model
