from itertools import zip_longest
from sys import stdout

def printh(*tables, sep=" " * 8, file=stdout):
    """
    Concatenate repr()-style tabular outputs horizontally.

    Parameters
    ----------
    *tables : objects or strings
        Either dataframe-like objects or pre-rendered repr strings.
    sep : str
        Separator between tables.

    Returns
    -------
    str
    """
    rendered = [
        t if isinstance(t, str) else repr(t)
        for t in tables
    ]

    split = [r.splitlines() for r in rendered]
    widths = [max(map(len, lines), default=0) for lines in split]

    padded = [
        [line.ljust(width) for line in lines]
        for lines, width in zip(split, widths)
    ]

    rows = zip_longest(*padded, fillvalue="")

    print(
        "\n".join(
            sep.join(col.ljust(w) for col, w in zip(row, widths))
            for row in rows
        ),
        file=file
    )
