def red(string: str) -> str:
    return f"\x1b[31m{string}\x1b[0m"


def green(string: str) -> str:
    return f"\x1b[32;1m{string}\x1b[0m"


def bright_black(string: str) -> str:
    return f"\x1b[30;1m{string}\x1b[0m"

def black(string: str)->str:
    return f"\x1b[30m{string}\x1b[0m"

def bright_white(string: str) -> str:
    return f"\x1b[37;1m{string}\x1b[0m"

def white(string:str)->str:
    return f"\x1b[37m{string}\x1b[0m"