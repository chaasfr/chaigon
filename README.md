## AI Code Improver Agent

This project is an AI agent designed to read and improve code. It leverages the power of large language models to understand, analyze, and refactor code to enhance its quality, efficiency, and readability.

### Functionality

The primary goal of this agent is to take a codebase as input, analyze it based on user prompts, and then output improved code. This can include:

*   **Bug fixing:** Identifying and correcting errors in the code.
*   **Code optimization:** Improving the performance and efficiency of the code.
*   **Readability enhancements:** Making the code easier to understand and maintain.
*   **Code refactoring:** Restructuring the code to improve its design and architecture.

### Example Usage

To use the agent, execute the following command in your terminal:

```bash
uv run main.py "Your prompt here"
```

For example, to use the calculator module, you might run:

```bash
uv run main.py "Please review the calculator module for potential improvements in error handling and efficiency."
```

The agent will then process your request and attempt to improve the code based on your instructions. The improved code will be outputted to the console.

### Getting Started

1.  Clone the repository to your local machine.
2.  Install UV: `pip install uv`
3.  Create a virtual environment using UV: `uv venv`
4.  Activate the virtual environment: `source .venv/bin/activate` (Linux/macOS) or `.venv\Scripts\activate` (Windows)
5.  Install the required dependencies using UV: `uv pip install -r requirements.txt`
6.  Run the agent with your desired prompt as described above.  For example: `uv run main.py "Please review the calculator module for potential improvements in error handling and efficiency."`

### Contributing

We welcome contributions to this project! If you have any ideas for improvements or new features, please submit a pull request.
