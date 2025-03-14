# Semantic Analyzer

A Python package for analyzing semantic similarity between words, sentences, and paragraphs using state-of-the-art language models.

## Features

- Word-level semantic analysis using Google News Word2Vec model
- Sentence-level semantic analysis using Sentence Transformers
- Paragraph-level semantic analysis using Sentence Transformers
- Flexible input options for near and far semantic relationships
- JSON and table output formats
- Command-line interface with intuitive options

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/semantic_analyzer.git
cd semantic_analyzer
```

2. Install using `uv`:
```bash
uv pip install -e .
```

3. Download the required models:
   - For word analysis: Download the Google News Word2Vec model from [Google's word2vec page](https://code.google.com/archive/p/word2vec/)
   - For sentence/paragraph analysis: The Sentence Transformer model will be downloaded automatically on first use

## Usage

The package provides three main commands: `word`, `sentence`, and `paragraph`. Each command has an `analyze` subcommand with similar options.

### Word Analysis

```bash
# Basic usage with near words
semantic-analyzer word analyze -n "heinous" -n "cruel"

# Using far words
semantic-analyzer word analyze -f "back" -f "inhuman"

# Combining near and far words
semantic-analyzer word analyze -n "heinous" -n "cruel" -f "back" -f "inhuman"

# Specifying custom vector path
semantic-analyzer word analyze -n "heinous" -p /path/to/your/GoogleNews-vectors-negative300.bin

# JSON output format
semantic-analyzer word analyze -n "heinous" -o json
```

Options:
- `-n, --near-words`: Words that should be semantically similar (optional)
- `-f, --far-words`: Words that should be semantically different (optional)
- `-t, --top-n`: Number of similar words to return (default: 5)
- `-o, --output-format`: Output format (json or table, default: table)
- `-p, --vector-path`: Path to the Word2Vec model file

### Sentence Analysis

```bash
# Basic usage with near sentences
semantic-analyzer sentence analyze -n "The cat is on the mat" -n "A feline rests on the rug"

# Using far sentences
semantic-analyzer sentence analyze -f "The dog is in the yard"

# Combining near and far sentences
semantic-analyzer sentence analyze -n "The cat is on the mat" -f "The dog is in the yard"

# JSON output format
semantic-analyzer sentence analyze -n "The cat is on the mat" -o json
```

Options:
- `-n, --near-sentences`: Sentences that should be semantically similar (optional)
- `-f, --far-sentences`: Sentences that should be semantically different (optional)
- `-o, --output-format`: Output format (json or table, default: table)

### Paragraph Analysis

```bash
# Basic usage with near paragraphs
semantic-analyzer paragraph analyze -n "First paragraph text..." -n "Similar paragraph text..."

# Using far paragraphs
semantic-analyzer paragraph analyze -f "Different paragraph text..."

# Combining near and far paragraphs
semantic-analyzer paragraph analyze -n "First paragraph text..." -f "Different paragraph text..."

# JSON output format
semantic-analyzer paragraph analyze -n "First paragraph text..." -o json
```

Options:
- `-n, --near-paragraphs`: Paragraphs that should be semantically similar (optional)
- `-f, --far-paragraphs`: Paragraphs that should be semantically different (optional)
- `-o, --output-format`: Output format (json or table, default: table)

## Output Format

### Table Format
```
Word Similarity Analysis
==================================================

Near words: heinous, cruel
Far words: back, inhuman

Similar Words:
------------------------------
Word                 Score     
------------------------------
malevolent          0.8234
vicious             0.7891
brutal              0.7654
```

### JSON Format
```json
{
  "near_words": ["heinous", "cruel"],
  "far_words": ["back", "inhuman"],
  "similar_words": [
    {"word": "malevolent", "similarity": 0.8234},
    {"word": "vicious", "similarity": 0.7891},
    {"word": "brutal", "similarity": 0.7654}
  ]
}
```

## Requirements

- Python >= 3.11
- gensim >= 4.3.3
- numpy >= 1.24.0
- pandas >= 2.0.0
- sentence-transformers >= 2.2.0
- click >= 8.1.8

## License

MIT License
