# RAG Agent for MyPortfolio

This project is a Retrieval-Augmented Generation (RAG) agent designed to answer questions about the portfolio owner. It utilizes embedding functions and a database to retrieve and generate accurate responses. This is currently a work in progress.

## Features

- **Question Answering**: Provides answers about the portfolio owner.
- **Embedding Function**: Retrieves relevant information.
- **Database Integration**: Populates and accesses stored data for efficient responses.

## Setup

1. Clone the repository.
2. Set up the virtual environment in `.venv`.
3. pull the llama3 model `ollama pull llama3`.
4. add files in the data folder.
5. Run `populate_database.py` to prepare the database.
6. Use `app.py` to start the agent.

## Usage

Run `app.py` to start the server and begin querying.

## Technologies

- Python
- Chroma
- Embedding APIs
- Ollama
- langChain
- Flask

