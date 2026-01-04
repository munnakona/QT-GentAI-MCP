# Hello Transformer

A simple Python project demonstrating sentiment analysis using Hugging Face Transformers.

## Prerequisites

- Python >= 3.13
- uv package manager (install with `pip install uv`)

## Installation

1. Clone the repository.
2. Navigate to the project directory.
3. Run `uv sync` to install dependencies.

## Usage

Run the main script:

```bash
python main.py
```

This will perform sentiment analysis on a sample sentence and print the result.

## Dependencies

The project uses the following main dependencies (managed via uv):

- `transformers>=4.57.3`
- `torch>=2.9.1`
- `accelerate>=1.12.0`
- `datasets>=4.4.2`
- `evaluate>=0.4.6`
- `sacremoses>=0.1.1`
- `sentencepiece>=0.2.1`
- `tokenizers>=0.22.1`

All dependencies are specified in `pyproject.toml`.
