# Langchain Topic Analyzer

A FastAPI-based topic analysis tool that uses LangChain to generate summaries, keywords, quiz questions, and difficulty ratings for any given topic. 

## Features

- **Summary**: Get a 3-sentence explanation of any topic
- **Keywords**: Extract 5 most important keywords
- **Quiz**: Generate 3 question-answer pairs
- **Difficulty Rating**: Get a 1-5 difficulty score
- **Combined Analysis**:  Get all features in one request

## Tech Stack

- **FastAPI** - REST API framework
- **LangChain** - LLM orchestration
- **HuggingFace** - LLM provider (Llama 3.1 8B Instruct)
- **Pydantic** - Data validation

## Project Structure

```
.
├── main.py           # FastAPI application with API endpoints
├── pipeline.py       # LangChain chains and LLM configuration
├── models.py         # Pydantic models for request/response
├── pyproject.toml    # Project dependencies
├── . python-version   # Python version specification
└── . gitignore
```

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   uv sync
   ```
3. Create a `.env` file with your HuggingFace API key:  
   ```
   HF_API_KEY=your_api_key_here
   ```
4. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints

- `POST /get/analyze` - Full topic analysis
- `POST /get/summary` - Topic summary only
- `POST /get/keywords` - Keywords only
- `POST /get/quiz` - Quiz questions only
- `POST /get/difficulty` - Difficulty rating only

## Note

> **This is a learning project.** While there are simpler ways to solve this problem (like a single LLM call with structured output), this approach was deliberately chosen to explore LangChain fundamentals in-depth, including:
> - Chaining prompts and parsers
> - Parallel execution with `RunnableParallel`
> - Custom output parsers
> - Pydantic integration
