import click
from typing import Optional
from ..analysis.sentence_analysis import analyze_sentence_similarity
from ..utils.models import SentenceAnalysisResult

@click.group()
def sentence():
    """Sentence-level semantic analysis commands"""
    pass

@sentence.command()
@click.option('--near-sentences', '-n', multiple=True, help='Sentences that should be semantically similar')
@click.option('--far-sentences', '-f', multiple=True, help='Sentences that should be semantically different')
@click.option('--output-format', '-o', type=click.Choice(['json', 'table']), default='table',
              help='Output format for results')
def analyze(near_sentences: list[str], far_sentences: list[str], output_format: str):
    """Analyze sentence similarity based on near and far sentence constraints"""
    if not near_sentences and not far_sentences:
        click.echo("Error: At least one near or far sentence must be specified")
        return

    result = analyze_sentence_similarity(
        near_sentences=list(near_sentences),
        far_sentences=list(far_sentences)
    )

    if output_format == 'json':
        click.echo(result.to_json())
    else:
        click.echo(result.to_table()) 