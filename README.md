# AIAgent

A lightweight command-line coding agent powered by **Google Gemini function calling**. It accepts natural-language prompts, inspects and edits files in a sandboxed workspace, runs Python scripts, and iterates through tool-calling rounds to produce answers.

## How It Works

```
User Prompt ──> Gemini LLM ──> Function Call? ──> Execute Tool Locally
                    ^                                    |
                    └────────── Feed Result Back <───────┘
                                      │
                              No More Calls
                                      v
                               Final Answer
```

The agent loop sends your prompt to Gemini, which may request tool calls (read files, write files, run scripts). Each tool result is fed back to the model until it produces a final natural-language response — up to **5 iterations** per request.

## Quick Start

```bash
# 1. Clone and enter the project
git clone <repo-url> && cd aiagent

# 2. Install dependencies
pip install -e .

# 3. Set your Gemini API key
echo "GEMINI_API_KEY=your_key_here" > .env

# 4. Run the agent
python main.py "List files and explain what this calculator does"
```

## Prerequisites

- **Python 3.13+** (check with `python --version`)
- A **Google Gemini API key** ([get one here](https://aistudio.google.com/apikey))

## Installation

**pip:**
```bash
pip install -e .
```

**uv:**
```bash
uv pip install -e .
```

Dependencies are pinned in `pyproject.toml`:

| Package | Version | Purpose |
|---------|---------|---------|
| `google-genai` | 1.12.1 | Gemini API client |
| `python-dotenv` | 1.1.0 | `.env` file loading |

## Configuration

Create a `.env` file at the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

If the key is missing, the agent exits with:
```
RuntimeError: API Key not found. Check .env file..
```

### Config Constants

| Constant | File | Default | Description |
|----------|------|---------|-------------|
| `MAX_CHARS` | `config.py` | `10000` | Max characters returned when reading files |
| Sandbox path | `functions/call_functions.py` | `./calculator` | Directory the agent can access |
| Model | `main.py` | `gemini-2.5-flash` | Gemini model used |
| Max iterations | `main.py` | `5` | Tool-call rounds per request |
| Exec timeout | `run_python_file.py` | `30s` | Subprocess timeout for Python execution |

## Usage

### Basic
```bash
python main.py "Refactor calculator/main.py for clearer error messages"
```

### Verbose Mode
```bash
python main.py "Add tests for division edge cases" --verbose
```

Verbose mode outputs:
- Original user prompt
- Prompt and response token counts
- Tool invocation details and results

### Example Prompts

```bash
python main.py "List files and explain what this calculator does"
python main.py "Fix failing behavior in pkg/calculator.py and update tests"
python main.py "Run calculator tests and summarize failures"
python main.py "Add a README inside calculator/ explaining its API"
```

## Project Structure

```
aiagent/
├── main.py                     # Entrypoint — CLI parsing, Gemini client, agent loop
├── prompt.py                   # System prompt defining agent persona
├── config.py                   # Shared constants (MAX_CHARS)
├── .env                        # API key (gitignored)
├── pyproject.toml              # Project metadata and dependencies
├── uv.lock                     # Locked dependency resolution
│
├── functions/                  # Tool implementations
│   ├── call_functions.py       # Dispatch: maps function names → implementations
│   ├── get_files_info.py       # List directory entries with metadata
│   ├── get_file_content.py     # Read file content (truncated at MAX_CHARS)
│   ├── write_file.py           # Write content to files
│   └── run_python_file.py      # Execute Python scripts (30s timeout)
│
├── calculator/                 # Sandboxed workspace the agent operates on
│   ├── main.py                 # Calculator CLI app
│   ├── tests.py                # Unit tests (unittest)
│   ├── lorem.txt
│   └── pkg/
│       ├── calculator.py       # Infix expression evaluator
│       ├── render.py           # JSON output formatter
│       └── morelorem.txt
│
└── test_*.py                   # Script-style tool behavior checks
```

## Available Tools

The agent has access to four tools, all constrained to the `./calculator` sandbox:

### `get_files_info(directory=".")`
Lists directory entries with file size and `is_dir` flag.

### `get_file_content(filepath)`
Reads file content, truncated at `MAX_CHARS` (10,000 chars). A notice is appended if content was truncated.

### `write_file(filepath, content)`
Writes text to a file inside the sandbox. Auto-creates parent directories.

### `run_python_file(filepath, args=[])`
Runs a Python script with optional CLI arguments. 30-second timeout. Returns stdout, stderr, and exit code.

## Security

All tools enforce **path boundary validation** using `os.path.commonpath()`:

```python
abs_working_dir = os.path.abspath(working_directory)
target = os.path.abspath(os.path.join(abs_working_dir, user_path))
is_valid = os.path.commonpath([abs_working_dir, target]) == abs_working_dir
```

Operations outside `./calculator` are rejected. The sandbox path is hardcoded in `functions/call_functions.py`.

## Testing

**Tool behavior checks:**
```bash
python test_get_file_content.py
python test_get_files_info.py
python test_write_file.py
python test_run_python_file.py
```

**Calculator unit tests:**
```bash
python calculator/tests.py
```

## Extending

Suggested improvements:

- Add structured logging instead of `print` statements
- Add proper automated tests (e.g., `pytest`) for function modules
- Expand tools (search, diff, lint, formatting, test runner)
- Add retry/backoff and error categorization
- Parameterize the sandbox path instead of hardcoding
- Add CI workflow for lint + tests
- Add a LICENSE file (MIT/Apache-2.0)
- Add `.env.example` for onboarding

## License

This project is licensed under the [MIT License](LICENSE).
