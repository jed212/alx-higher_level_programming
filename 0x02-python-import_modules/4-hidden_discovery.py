#!/usr/bin/python3

if __name__ == "__main__":
    """Prints names defined by hidden_4 module."""
    import hidden_4

    n = dir(hidden_4)
    for n in n:
        if n[:2] != "__":
            print(n)
