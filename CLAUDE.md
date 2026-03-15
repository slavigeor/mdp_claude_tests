# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Workflow Rules

- **Ask for approval on each step** and show the code before executing
- **Show token cost estimation** before planning or executing so the user can decide whether to proceed

## Code Style

- Use **classes (OOP)** for all modules
- Write **concise comments** explaining the code
- Format all Python files with **Black**

## Project Overview

A local CLI tool that reads job ads (from LinkedIn or company pages), reads the user's CV (PDF), and generates a tailored cover letter using Claude CLI.

See `agentic_development/linked_in.md` for the full build plan.

## Architecture

**Modular design** in `job_app_tool/`:

- `scraper.py` — `JobScraper` class: fetches and parses job ads from URLs
- `cv_reader.py` — `CVReader` class: reads PDF CVs using `pypdf`
- `generator.py` — `CoverLetterGenerator` class: pipes job ad + CV to `claude` CLI for generation
- `main.py` — CLI entry point using `argparse`

## Running the Application

```bash
source .venv/bin/activate
pip install -r requirements.txt
python -m job_app_tool.main --job-url <url> --cv <path-to-cv.pdf>
```

## Dependencies

- `beautifulsoup4` — HTML parsing for job ads
- `requests` — HTTP
- `pypdf` — PDF reading
- `black` — code formatting
