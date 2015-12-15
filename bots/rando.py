import random

__botname__ = "Rando"
__entryfunction__ = "rando"


def rando(opponent=None):
    return random.randrange(0, 2 + 1)
