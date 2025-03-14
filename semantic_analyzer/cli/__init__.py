import click
from .word import word_group
from .sentence import sentence_group
from .paragraph import paragraph_group

@click.group()
def cli():
    """Semantic Analysis Tool for Words, Sentences, and Paragraphs"""
    pass

cli.add_command(word_group)
cli.add_command(sentence_group)
cli.add_command(paragraph_group)

if __name__ == '__main__':
    cli()

"""
CLI commands for semantic analysis.
""" 