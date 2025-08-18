# LC_Model

A modular Python project for experimenting with various Large Language Models (LLMs) using LangChain, OpenAI, Hugging Face, and more. This project demonstrates how to interact with LLMs via API and locally, manage environment variables, and run tests.

## Features
- Run and test LLMs from OpenAI, Hugging Face, and other providers
- Support for both API-based and local model inference
- Environment variable management with `.env`
- Modular code structure for easy extension
- Unit testing with pytest

## Project Structure
```
LC_Model/
├── BaseLLMs/                # Demos and utilities for base LLMs
├── ChatModels/              # Demos for chat-based LLMs (OpenAI, Hugging Face, etc.)
├── tests/                   # Test scripts
├── .env                     # Environment variables (not committed)
├── .gitignore               # Git ignore rules
├── requirement.txt          # Python dependencies
```

## Setup
1. **Clone the repository**
2. **Install dependencies:**
   ```bash
   pip install -r requirement.txt
   ```
3. **Configure environment variables:**
   - Copy `.env.example` to `.env` and fill in your API keys (OpenAI, Hugging Face, etc.)

## Usage
- Run demo scripts in `BaseLLMs/` or `ChatModels/` to interact with different LLMs.
- Example:
  ```bash
  python ChatModels/OpenAi_ChatModelDemo.py
  ```
- Run tests:
  ```bash
  pytest
  ```

## Notes
- Some models require valid API keys and internet access.
- For local inference, ensure you have the necessary model files and hardware resources.
- If you encounter errors, check your `.env` and model support for chat/completion.

## License
This project is for educational and research purposes.
