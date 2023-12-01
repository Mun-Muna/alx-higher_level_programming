#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    dir(hidden_4).sort()
    for str in dir(hidden_4):
        if not str.startswith("__"):
            print(str)
