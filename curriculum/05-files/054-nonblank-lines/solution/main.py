def read_nonblank(path):
    with open(path, encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]
