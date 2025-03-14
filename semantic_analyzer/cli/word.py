import click
from ..analysis.word_analysis import analyze_word_similarity
from ..utils.vector_store import DEFAULT_VECTOR_PATH
import os

@click.group()
def word_group():
    """Word-level semantic analysis commands"""
    pass

@word_group.command()
@click.option('--near-words', '-n', multiple=True, help='Words that should be semantically similar')
@click.option('--far-words', '-f', multiple=True, help='Words that should be semantically different')
@click.option('--top-n', '-t', default=5, help='Number of similar words to return')
@click.option('--output-format', '-o', type=click.Choice(['json', 'table']), default='table',
              help='Output format for results')
@click.option('--vector-path', '-p', default=DEFAULT_VECTOR_PATH,
              help='Path to the Google News Word2Vec model file')
def analyze(near_words: list[str], far_words: list[str], top_n: int, output_format: str, vector_path: str):
    """Analyze word similarity based on near and far word constraints"""
    if not os.path.exists(vector_path):
        click.echo("\nError: Word2Vec model file not found!")
        click.echo(f"Expected path: {vector_path}")
        click.echo("\nTo use word analysis, you need to download the Google News Word2Vec model:")
        click.echo("1. Download the model from: https://code.google.com/archive/p/word2vec/")
        click.echo("2. Extract the downloaded file")
        click.echo("3. Either:")
        click.echo("   a) Place the extracted file at the expected path above")
        click.echo("   b) Or specify a different path using --vector-path")
        click.echo("\nExample command with custom path:")
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