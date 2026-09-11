import json


def word_report(source, destination):
    with open(source, encoding="utf-8") as file:
        words = file.read().lower().split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    with open(destination, "w", encoding="utf-8") as file:
        json.dump(counts, file, ensure_ascii=False)
    return counts
