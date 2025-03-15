import click
from typing import Optional
from ..analysis.word_analysis import analyze_word_similarity
import os

@click.group()
def word():
    """Word-level semantic analysis commands"""
    pass

@word.command()
@click.option('--near-words', '-n', multiple=True, help='Words that should be semantically similar')
@click.option('--far-words', '-f', multiple=True, help='Words that should be semantically different')
@click.option('--top-n', '-t', default=5, help='Number of similar words to return')
@click.option('--output-format', '-o', type=click.Choice(['json', 'table']), default='table',
              help='Output format for results')
@click.option('--vector-path', '-p', help='Path to the Google News Word2Vec model file (can also be set via WORD_VECTOR_PATH env var)')
def analyze(near_words: list[str], far_words: list[str], top_n: int, output_format: str, vector_path: Optional[str]):
    """Analyze word similarity based on near and far word constraints"""
    # Get vector path from command line or environment variable
    vector_path = vector_path or os.getenv('WORD_VECTOR_PATH')
    
    if not vector_path:
        click.echo("\nError: Word2Vec model file path not provided!")
        click.echo("\nTo use word analysis, you need to provide the path to the Google News Word2Vec model in one of two ways:")
        click.echo("1. Using the --vector-path option:")
        click.echo("   semantic-analyzer word analyze -n 'heinous' -n 'cruel' -p /path/to/your/GoogleNews-vectors-negative300.bin")
        click.echo("\n2. Using the WORD_VECTOR_PATH environment variable:")
        click.echo("   export WORD_VECTOR_PATH=/path/to/your/GoogleNews-vectors-negative300.bin")
        click.echo("   semantic-analyzer word analyze -n 'heinous' -n 'cruel'")
        click.echo("\nTo get the model file:")
        click.echo("1. Download from: https://code.google.com/archive/p/word2vec/")
        click.echo("2. Extract the downloaded file")
        return

    if not os.path.exists(vector_path):
        click.echo("\nError: Word2Vec model file not found!")
        click.echo(f"Provided path: {vector_path}")
        click.echo("\nTo use word analysis, you need to download the Google News Word2Vec model:")
        click.echo("1. Download the model from: https://code.google.com/archive/p/word2vec/")
        click.echo("2. Extract the downloaded file")
        click.echo("3. Provide the path to the extracted file using --vector-path or WORD_VECTOR_PATH")
        click.echo("\nExample command:")
        click.echo("semantic-analyzer word analyze -n 'heinous' -n 'cruel' -p /path/to/your/GoogleNews-vectors-negative300.bin")
        return

    result = analyze_word_similarity(
        near_words=list(near_words),
        far_words=list(far_words),
        top_n=top_n,
        vector_path=vector_path
    )

    if output_format == 'json':
        click.echo(result.to_json())
    else:
        click.echo(result.to_table()) 