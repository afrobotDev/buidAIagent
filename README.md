# AI Agent

A Gemini-powered AI agent designed to assist with coding tasks. This agent can perform file operations, read and write code, and execute Python scripts, making it a versatile tool for software development and debugging.

## Features

- **File Operations**: Read, write, and get information about files in the workspace.
- **Code Execution**: Run Python files and capture their output.
- **Intelligent Assistance**: Powered by Google's Gemini AI for natural language understanding and code generation.
- **Calculator Example**: Includes a sample calculator application that the agent can interact with.

## Installation

1. Ensure you have Python 3.13 or higher installed.
2. Clone or download the project repository.
3. Install dependencies using pip:

   ```bash
   pip install -e .
   ```

   Or using uv (if available):

   ```bash
   uv pip install -e .
   ```

## Setup

1. Create a `.env` file in the root directory of the project.
2. Add your Gemini API key to the `.env` file:

   ```
   GEMINI_API_KEY=your_api_key_here
   ```

   You can obtain a Gemini API key from the [Google AI Studio](https://makersuite.google.com/app/apikey).

## Usage

Run the AI agent from the command line with a prompt:

```bash
python main.py "Your coding task or question here"
```

For verbose output, include the `--verbose` flag:

```bash
python main.py "Debug this code" --verbose
```

The agent will process your request, potentially using its tools to interact with files and execute code within the `calculator` directory.

### Example

```bash
python main.py "Calculate 2 + 3 * 4"
```

This might result in the agent running the calculator application and returning the result.

## Project Structure

- `main.py`: The main entry point for the AI agent.
- `config.py`: Configuration settings, such as character limits.
- `prompt.py`: Contains the system prompt that defines the agent's behavior.
- `functions/`: Directory containing tool functions for file operations and code execution.
  - `call_functions.py`: Handles function calls to the available tools.
  - `get_file_content.py`: Tool to read file contents.
  - `get_files_info.py`: Tool to get information about files.
  - `write_file.py`: Tool to write to files.
  - `run_python_file.py`: Tool to execute Python files.
- `calculator/`: Example application directory.
  - `main.py`: Entry point for the calculator app.
  - `tests.py`: Tests for the calculator.
  - `pkg/`: Package containing calculator logic.
    - `calculator.py`: Core calculator class with expression evaluation.
    - `render.py`: Output formatting utilities.
- `test_*.py`: Unit tests for the various functions.

## Testing

Run the tests using pytest or your preferred test runner:

```bash
python -m pytest
```

Or run individual test files:

```bash
python test_get_file_content.py
```

## Dependencies

- `google-genai==1.12.1`: For interacting with Google's Gemini AI.
- `python-dotenv==1.1.0`: For loading environment variables from `.env` files.

## Author

[afrobotDev](https://github.com/afrobotDev)

## Contributing

Contributions are welcome! Please ensure that any changes maintain code quality and include appropriate tests.

## License

This project is licensed under the MIT License. See the LICENSE file for details (if applicable).
