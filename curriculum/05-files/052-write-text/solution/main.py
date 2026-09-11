def write_text(path, text):
    with open(path, "w", encoding="utf-8") as file:
        file.write(text)
