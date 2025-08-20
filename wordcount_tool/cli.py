# wordcount_tool/cli.py

import click
from .counter import WordCounter

@click.command()
@click.argument('filepath', type=click.Path(exists=True))
def main(filepath):
    """
    A simple command-line tool to count word frequencies in a text file.
    """
    counter = WordCounter(filepath)
    counts = counter.count_words()

    if counts:
        print("--- Word Counts ---")
        # Sort the words alphabetically for a clean output
        for word, count in sorted(counts.items()):
            print(f"{word}: {count}")