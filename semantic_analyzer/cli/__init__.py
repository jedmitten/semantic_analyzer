import click
from .word import word
from .sentence import sentence
from .paragraph import paragraph

@click.group()
def cli():
    """Semantic Analysis Tool for Words, Sentences, and Paragraphs"""
    pass

cli.add_command(word)
cli.add_command(sentence)
cli.add_command(paragraph)

if __name__ == '__main__':
    cli()

"""
CLI commands for semantic analysis.
""" 