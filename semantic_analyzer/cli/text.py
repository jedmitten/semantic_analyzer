import click
from ..analysis.text_analysis import analyze_text_qualitative
from ..utils.file_reader import read_input_file

@click.group()
def text():
    """Text-level semantic analysis commands"""
    pass

@text.command()
@click.option('--texts', '-t', multiple=True, help='Text segments to analyze')
@click.option('--input-file', '-f', type=click.Path(exists=True), help='Input file (CSV, JSON, or TOML) containing texts')
@click.option('--output-format', '-o', type=click.Choice(['json', 'table']), default='table',
              help='Output format for results')
def analyze(texts: list[str], input_file: str, output_format: str):
    """Provide qualitative analysis of text including sentiment, key themes, and content analysis"""
    if not texts and not input_file:
        click.echo("Error: Either --texts or --input-file must be provided")
        click.echo("\nExample usage:")
        click.echo("1. Direct input:")
        click.echo("   semantic-analyzer text analyze -t 'First text segment.' -t 'Second text segment.'")
        click.echo("\n2. From file:")
        click.echo("   semantic-analyzer text analyze -f input.csv")
        click.echo("\nFile formats supported:")
        click.echo("1. CSV: Must have a 'texts' column")
        click.echo("2. JSON: Must have a 'texts' key with array value")
        click.echo("3. TOML: Must have a 'texts' key with array value")
        return
    
    if texts and input_file:
        click.echo("Error: Cannot provide both --texts and --input-file")
        return
    
    if input_file:
        try:
            texts = read_input_file(input_file, required_type="texts")
        except ValueError as e:
            click.echo(f"Error: {str(e)}")
            click.echo("\nExample file formats:")
            click.echo("CSV:")
            click.echo("texts")
            click.echo("\"First text segment.\"")
            click.echo("\"Second text segment.\"")
            click.echo("\nJSON:")
            click.echo('{"texts": ["First text segment.", "Second text segment."]}')
            click.echo("\nTOML:")
            click.echo('texts = ["First text segment.", "Second text segment."]')
            return

    result = analyze_text_qualitative(
        texts=list(texts)
    )

    if output_format == 'json':
        click.echo(result.to_json())
    else:
        click.echo(result.to_table()) 