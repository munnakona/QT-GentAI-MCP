# Huggingface QT

This Python script demonstrates the use of Hugging Face Transformers library for various natural language processing tasks, including sentiment analysis, translation, text generation, and text classification.

## Features

- **Sentiment Analysis**: Analyzes the sentiment of English text using a pre-trained DistilBERT model.
- **Translation**: Translates English text to Hindi using the Helsinki-NLP Opus model.
- **Text Generation**: Generates text based on a given prompt using the Qwen 3-0.6B model.
- **Text Classification**: Classifies text sentiment and returns all scores using the Qwen 3-0.6B model.

## Requirements

- Python 3.x
- Transformers library
- PyTorch or TensorFlow (automatically handled by transformers)

## Installation

1. Install the required library:

   ```bash
   pip install transformers
   ```
2. Ensure you have PyTorch or TensorFlow installed. The transformers library will guide you if needed.

## Usage

Run the script directly with Python:

```bash
python huggingface_qt.py
```

The script will execute the following tasks and print the results:

1. **Sentiment Analysis**: Analyzes a negative sentiment example.
2. **Translation**: Translates a sample English sentence to Hindi.
3. **Text Generation**: Generates text based on the prompt "write the small story".
4. **Text Classification**: Classifies a positive sentiment example and returns all scores.

## Code Structure

- `classifier`: Pipeline for sentiment analysis.
- `summerisator`: Pipeline for English to Hindi translation.
- `generator`: Pipeline for text generation.
- Another `classifier`: Pipeline for text classification with all scores.

## Examples

### Sentiment Analysis

```python
response = classifier("I got irritate standing in line at airport")
print(response)
# Output: [{'label': 'NEGATIVE', 'score': 0.9998}]
```

### Translation

```python
response = summerisator("I like Large Language models very much")
print(response)
# Output: [{'translation_text': 'मैं बड़े भाषा मॉडल बहुत पसंद करता हूं'}]
```

### Text Generation

```python
response = generator("write the small story")
print(response)
# Output: Generated text based on the prompt
```

### Text Classification

```python
response = classifier("I like Large Language models very much")
print(response)
# Output: [{'label': 'LABEL_0', 'score': 0.6}, {'label': 'LABEL_1', 'score': 0.4}]  # Example scores
```

## Notes

- The script is based on code originally generated in Google Colab.
- Some lines (e.g., positive sentiment example) are commented out.
- Ensure internet connection for model downloads on first run.

## License

This code is provided as-is for educational purposes. Refer to the original Colab notebook for any licensing information.
