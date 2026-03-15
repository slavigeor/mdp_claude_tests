# Goals for this session

- I want to learn as much as possible about Claude code: MCPs, Skills, Agents, Memory, Hooks, Project set up. I want to test out these functionalities with instructions from you
- I want to discuss a plan for building a tool locally that can read a job add (on linkedin or a specific company page), can read my CV and then update my CV with a short cover letter so I am ready to apply
    - what kind of language should be used
    - how would the functionality work
    - what kind of steps are to be followed
- do both goals together so I can learn by doing

---

# Plan: Job Application Tool + Learn Claude Code by Doing

## Approach
Build the tool step-by-step, learning one Claude Code feature per phase.

## Phase 1: Project Setup → **CLAUDE.md & Project Config**
- Create `job_app_tool/` folder with proper structure
- Update CLAUDE.md, init git, configure `.claude/settings.local.json`
- **Learn**: How CLAUDE.md guides Claude Code, project settings, permissions

## Phase 2: Job Ad Scraping → **MCPs (Model Context Protocol)**
- Build `scraper.py` to fetch & parse job ads from URLs
- Set up an MCP server (e.g., Fetch MCP) to show how MCPs extend Claude Code
- **Libs**: `beautifulsoup4`, `requests`
- **Learn**: What MCPs are, how to configure them, how they add capabilities

## Phase 3: CV Reading → **Memory & Skills**
- Build `cv_reader.py` to read PDF/DOCX/TXT CVs
- Store CV path & user preferences in Claude Code Memory
- **Libs**: `pypdf`, `python-docx`
- **Learn**: Memory system (types, saving, recalling), Skills (explain-code, simplify)

## Phase 4: AI Generation → **Claude CLI & Agents**
- Build `generator.py` using `claude` CLI as subprocess (no API key, uses existing subscription)
- Pipes job ad + CV as a prompt → gets cover letter + CV suggestions back
- **Learn**: `claude` CLI usage, Agent subagent types, prompt engineering

## Phase 5: CLI & Automation → **Hooks**
- Wire into CLI: `python main.py --job-url <url> --cv <path>`
- Set up Hooks for auto-linting or testing
- **Learn**: Hook types (pre/post), automation patterns

## File Structure
```
job_app_tool/
├── __init__.py
├── scraper.py        # job ad fetching/parsing
├── cv_reader.py      # CV file reading
├── generator.py      # Claude API integration
├── main.py           # CLI entry point
└── requirements.txt
```

## Dependencies
`beautifulsoup4`, `requests`, `pypdf`, `black`

## User Notes
- CV format: **PDF** (use `pypdf` for reading)
- No API key needed — uses `claude` CLI via subprocess
- Code style: OOP (classes), concise comments, Black formatting

Test