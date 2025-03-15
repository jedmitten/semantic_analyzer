# Semantic Analyzer

A Python package for analyzing semantic similarity between words and text using state-of-the-art language models.

## Features

- Word-level semantic analysis using Google News Word2Vec model
- Text-level semantic analysis using Sentence Transformers
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
   - For text analysis: The Sentence Transformer model will be downloaded automatically on first use

## Usage

The package provides two main commands: `word` and `text`. Each command has an `analyze` subcommand with similar options.

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

### Text Analysis

```bash
# Basic usage with text segments to analyze
semantic-analyzer text analyze -t "The quick brown fox jumps over the lazy dog." -t "A fast brown fox leaps over a sleepy dog."

# Using input file (CSV)
semantic-analyzer text analyze -f texts.csv

# Using input file (JSON)
semantic-analyzer text analyze -f texts.json

# Using input file (TOML)
semantic-analyzer text analyze -f texts.toml

# JSON output format
semantic-analyzer text analyze -t "The quick brown fox jumps over the lazy dog." -o json
```

Options:
- `-t, --texts`: Text segments to analyze (optional if --input-file is provided)
- `-f, --input-file`: Input file (CSV, JSON, or TOML) containing texts (optional if --texts is provided)
- `-o, --output-format`: Output format (json or table, default: table)

## Input File Formats

The tool supports reading input from CSV, JSON, or TOML files. Each command group (words, texts) requires its specific key in the input file:

### CSV Format
```csv
words
"example"
"test"
```

### JSON Format
```json
{
    "words": ["example", "test"]
}
```

### TOML Format
```toml
words = ["example", "test"]

# TOML also supports multiline strings in arrays:
texts = [
    """This is a long text segment
    that spans multiple lines
    but is still a single segment.""",
    "This is another text segment."
]
```

Note: Each command group (words, texts) requires its specific key in the input file. The examples above show the format for each type of input.

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
