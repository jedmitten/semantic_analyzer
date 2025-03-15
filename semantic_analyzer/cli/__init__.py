import click
from .word import word
from .text import text

@click.group()
def cli():
    """Semantic Analysis Tool for Words and Text"""
    pass

cli.add_command(word)
cli.add_command(text)

if __name__ == '__main__':
    cli()

"""
CLI commands for semantic analysis.
""" 