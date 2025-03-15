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
# Basic usage with near words (vector path required via option or environment variable)
semantic-analyzer word analyze -n "heinous" -n "cruel" -p /path/to/your/GoogleNews-vectors-negative300.bin

# Using environment variable for vector path
export WORD_VECTOR_PATH=/path/to/your/GoogleNews-vectors-negative300.bin
semantic-analyzer word analyze -n "heinous" -n "cruel"

# Using far words
semantic-analyzer word analyze -f "back" -f "inhuman" -p /path/to/your/GoogleNews-vectors-negative300.bin

# Combining near and far words
semantic-analyzer word analyze -n "heinous" -n "cruel" -f "back" -f "inhuman" -p /path/to/your/GoogleNews-vectors-negative300.bin

# JSON output format
semantic-analyzer word analyze -n "heinous" -p /path/to/your/GoogleNews-vectors-negative300.bin -o json
```

Options:
- `-n, --near-words`: Words that should be semantically similar (optional)
- `-f, --far-words`: Words that should be semantically different (optional)
- `-t, --top-n`: Number of similar words to return (default: 5)
- `-o, --output-format`: Output format (json or table, default: table)
- `-p, --vector-path`: Path to the Word2Vec model file (can also be set via WORD_VECTOR_PATH env var)

### Sentence Analysis

```bash
# Basic usage with sentences to analyze
semantic-analyzer sentence analyze -s "The quick brown fox jumps over the lazy dog." -s "A fast brown fox leaps over a sleepy dog."

# Using input file (CSV)
semantic-analyzer sentence analyze -f sentences.csv

# Using input file (JSON)
semantic-analyzer sentence analyze -f sentences.json

# Using input file (TOML)
semantic-analyzer sentence analyze -f sentences.toml

# JSON output format
semantic-analyzer sentence analyze -s "The quick brown fox jumps over the lazy dog." -o json
```

Options:
- `-s, --sentences`: Sentences to analyze (optional if --input-file is provided)
- `-f, --input-file`: Input file (CSV, JSON, or TOML) containing sentences (optional if --sentences is provided)
- `-o, --output-format`: Output format (json or table, default: table)

### Paragraph Analysis

```bash
# Basic usage with paragraphs to analyze
semantic-analyzer paragraph analyze -p "The first paragraph of text to analyze. It can contain multiple sentences." -p "Another paragraph to analyze with different content."

# Using input file (CSV)
semantic-analyzer paragraph analyze -f paragraphs.csv

# Using input file (JSON)
semantic-analyzer paragraph analyze -f paragraphs.json

# Using input file (TOML)
semantic-analyzer paragraph analyze -f paragraphs.toml

# JSON output format
semantic-analyzer paragraph analyze -p "The first paragraph of text to analyze." -o json
```

Options:
- `-p, --paragraphs`: Paragraphs to analyze (optional if --input-file is provided)
- `-f, --input-file`: Input file (CSV, JSON, or TOML) containing paragraphs (optional if --paragraphs is provided)
- `-o, --output-format`: Output format (json or table, default: table)

## Input File Formats

The package supports flexible input formats for sentences and paragraphs. Files can be in CSV, JSON, or TOML format, and the content type can be specified either explicitly or implicitly.

### CSV Format
```csv
# With explicit type
sentences
"The first sentence to analyze."
"Another sentence for analysis."

# Without explicit type (first column is used)
text
"The first sentence to analyze."
"Another sentence for analysis."
```

### JSON Format
```json
# With explicit type
{
  "sentences": [
    "The first sentence to analyze.",
    "Another sentence for analysis."
  ]
}

# Without explicit type (array)
[
  "The first sentence to analyze.",
  "Another sentence for analysis."
]

# Without explicit type (first array value)
{
  "text": [
    "The first sentence to analyze.",
    "Another sentence for analysis."
  ]
}
```

### TOML Format
```toml
# With explicit type
sentences = [
  "The first sentence to analyze.",
  "Another sentence for analysis."
]

# Without explicit type (array)
[
  "The first sentence to analyze.",
  "Another sentence for analysis."
]

# Without explicit type (first array value)
[text]
values = [
  "The first sentence to analyze.",
  "Another sentence for analysis."
]
```

Note: For paragraph analysis, use the same format but with "paragraphs" as the key/column name instead of "sentences". If no type-specific key is provided, the first available array or column will be used.

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
