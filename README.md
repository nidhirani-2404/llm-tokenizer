# 🤖 LLM Tokenizer

A simple Python project to understand how **GPT models tokenize text** using the tiktoken library.

## ✨ Features

- **Encode** text into tokens
- **Decode** tokens back to text
- **Count** total tokens

## 📦 Installation

```bash
pip install -r requirements.txt
```


## 🚀 Run

```bash
python tokenizer.py
python detokenizer.py

```

---

## 🔍 Context Window & Token Limitations

Understanding the context window and token limits is crucial for working with LLMs. Here's a quick reference:

| Model | Context Window | Max Output | Total Tokens | Notes |
|-------|----------------|-----------|--------------|-------|
| **GPT-4** | 8,192 | 4,096 | 8,192 | Latest and most capable |
| **GPT-4 Turbo** | 128,000 | 4,096 | 128,000 | Extended context |
| **GPT-4o** | 128,000 | 4,096 | 128,000 | Optimized for speed & cost |
| **GPT-3.5 Turbo** | 4,096 | 2,048 | 4,096 | Fast and cost-effective |
| **Claude 3 Opus** | 200,000 | 4,096 | 200,000 | Very large context |
| **Claude 3 Sonnet** | 200,000 | 4,096 | 200,000 | Balanced performance |
| **Claude 3 Haiku** | 200,000 | 4,096 | 200,000 | Fastest, cost-effective |
| **Llama 2** | 4,096 | N/A | 4,096 | Open-source |
| **Llama 2 70B** | 4,096 | N/A | 4,096 | Larger variant |
| **Mistral 7B** | 32,768 | N/A | 32,768 | Extended context |
| **PaLM 2** | 32,000 | N/A | 32,000 | Google's large model |
| **Cohere Command** | 4,096 | N/A | 4,096 | General purpose |

### Key Concepts

- **Context Window**: The maximum number of tokens the model can process at once (input + output)
- **Max Output**: The maximum number of tokens the model can generate in a single response
- **Token Limits**: Important to stay under these limits to avoid errors or truncation

### 💡 Tips for Token Management

1. **Monitor Token Count**: Use this tokenizer to count tokens in your prompts before sending to APIs
2. **Optimize Prompts**: Keep prompts concise to maximize available tokens for responses
3. **Batch Processing**: For large documents, split them into chunks that fit within context limits
4. **Choose the Right Model**: Select models with appropriate context windows for your use case

---

**Get started with tokenization today!**
