def read_lines(filename: str) -> list[str]:
    with open(filename) as f:
        return f.readlines()
