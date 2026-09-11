def save_store(store, path):
    with open(path, "w", encoding="utf-8") as file:
        file.write(store.export_json())


def load_store(store, path):
    with open(path, encoding="utf-8") as file:
        text = file.read()
    return store.import_json(text)
