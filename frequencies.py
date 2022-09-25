"""Frequencies function."""
"""Function which produces a dictionary based on the frequency of items in the items list."""

def frequencies(items):
    try:
        items = [str(i) for i in items]
        frequencies = {}
        for i in items:
            frequencies = {i : items.count(i) for i in items}
        return frequencies
    except ValueError:
        "You did not enter a list correctly."
