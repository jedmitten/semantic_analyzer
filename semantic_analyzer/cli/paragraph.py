import click
from typing import Optional
from ..analysis.paragraph_analysis import analyze_paragraph_similarity
from ..utils.models import ParagraphAnalysisResult

@click.group()
def paragraph():
    """Paragraph-level semantic analysis commands"""
    pass

@paragraph.command()
@click.option('--near-paragraphs', '-n', multiple=True, help='Paragraphs that should be semantically similar')
@click.option('--far-paragraphs', '-f', multiple=True, help='Paragraphs that should be semantically different')
@click.option('--output-format', '-o', type=click.Choice(['json', 'table']), default='table',
              help='Output format for results')
def analyze(near_paragraphs: list[str], far_paragraphs: list[str], output_format: str):
    """Analyze paragraph similarity based on near and far paragraph constraints"""
    if not near_paragraphs and not far_paragraphs:
        click.echo("Error: At least one near or far paragraph must be specified")
        return

    result = analyze_paragraph_similarity(
        near_paragraphs=list(near_paragraphs),
        far_paragraphs=list(far_paragraphs)
    )

    if output_format == 'json':
        click.echo(result.to_json())
    else:
        click.echo(result.to_table()) 