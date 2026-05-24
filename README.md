# AIAgent (Gemini-Powered Coding Agent)

A lightweight command-line coding agent built with **Google Gemini function calling**.

It accepts a natural-language prompt, can inspect/edit files in a sandboxed workspace (`./calculator`), run Python scripts, and iterate for up to 5 tool-calling rounds before returning a final answer.

---

## What this project does

This repository demonstrates a compact “agent loop” architecture:

1. Send a user prompt to Gemini.
2. Let Gemini request tools (`get_files_info`, `get_file_content`, `write_file`, `run_python_file`).
3. Execute the requested tool locally.
4. Feed tool output back to the model.
5. Repeat until the model returns a natural-language answer.

The project is intentionally small and easy to inspect, making it a useful starter template for building more capable software agents.

---

## Core features

- **Gemini function calling integration** via `google-genai`.
- **Filesystem introspection** in a controlled working directory.
- **Safe file read/write guards** using path boundary checks.
- **Python execution tool** with timeout and structured output capture.
- **Verbose token/debug output** for development visibility.
- **Included sample workspace** (`calculator/`) the agent can operate on.

---

## Repository layout

```text
.
├── main.py                       # Agent entrypoint + loop
├── prompt.py                     # System prompt for model behavior
├── config.py                     # Shared config (e.g., max chars for file reads)
├── functions/
│   ├── call_functions.py         # Dispatches model-requested tools
│   ├── get_files_info.py         # List directory entries
│   ├── get_file_content.py       # Read file content with truncation
│   ├── write_file.py             # Write file content
│   └── run_python_file.py        # Execute Python files and capture output
├── calculator/                   # Tool sandbox / example codebase
│   ├── main.py                   # Calculator CLI
│   ├── tests.py                  # Unit tests for calculator behavior
│   ├── lorem.txt
│   └── pkg/
│       ├── calculator.py         # Expression evaluator
│       ├── render.py             # JSON output formatting
│       └── morelorem.txt
├── test_*.py                     # Script-style tool behavior checks
├── pyproject.toml                # Project metadata and dependencies
└── uv.lock                       # Locked dependency resolution

---

## Requirements

- **Python 3.13+**
- A **Gemini API key**

Dependencies (pinned in `pyproject.toml`):

- `google-genai==1.12.1`
- `python-dotenv==1.1.0`

---

## Installation

### Option A: pip

```bash
pip install -e .
```

### Option B: uv

```bash
uv pip install -e .
```

---

## Configuration

Create a `.env` file at repository root:

```env
GEMINI_API_KEY=your_api_key_here
```

If the key is missing, `main.py` exits with:

```text
RuntimeError: API Key not found. Check .env file..
```

---

## Usage

### Basic

```bash
python main.py "Refactor calculator/main.py for clearer error messages"
```

### Verbose mode

```bash
python main.py "Add tests for division edge cases" --verbose
```

Verbose mode prints:

- Original user prompt
- Prompt token count
- Response token count
- Tool invocation details

---

## How the agent is scoped

Tool execution is constrained to:

```text
./calculator
```

This is enforced in `functions/call_functions.py` by injecting:

- `working_directory = "./calculator"`

So even though you run the agent from repo root, the model’s tools read/write/execute within the calculator workspace.

---

## Available tools (function declarations)

### 1) `get_files_info(directory=".")`
Lists directory entries with file size and `is_dir` flag.

### 2) `get_file_content(filepath)`
Reads file content from the sandbox directory, limited by `MAX_CHARS` from `config.py`.
If truncated, a suffix note is appended.

### 3) `write_file(filepath, content)`
Writes text content to a target file path (inside sandbox).

### 4) `run_python_file(filepath, args=[])`
Runs a Python script with optional CLI args, timeout (30s), and returns formatted command/stdout/stderr text.

---

## Example tasks you can run

- “List files and explain what this calculator does.”
- “Fix failing behavior in `pkg/calculator.py` and update tests.”
- “Run calculator tests and summarize failures.”
- “Add a README inside `calculator/` explaining its API.”

---

## Running checks

This repo includes script-style checks like:

```bash
python test_get_file_content.py
python test_get_files_info.py
python test_write_file.py
python test_run_python_file.py
```

And calculator unit tests:

```bash
python calculator/tests.py
```

---

## Known implementation notes

- The main loop currently allows up to **5 model/tool turns** per request.
- Tool outputs are sent back to Gemini as user-role content to continue reasoning.
- Tool guardrails rely on `os.path.commonpath` path-boundary validation.
- `run_python_file` returns both stdout and stderr in all cases, and includes non-zero exit info.

---

## Extending this project

Good next improvements:

- Add structured logging instead of `print` statements.
- Add proper automated tests (e.g., `pytest`) for function modules.
- Expand tools (search, diff, lint, formatting, test runner abstraction).
- Add retry/backoff and error categorization for model/tool failures.
- Parameterize the sandbox path instead of hardcoding `./calculator`.
- Add CI workflow for lint + tests.

---

## License

No license file is currently present in this repository. Add one (e.g., MIT/Apache-2.0) before distribution.
