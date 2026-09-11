import csv


def read_people(path):
    with open(path, encoding="utf-8", newline="") as file:
        return [
            {"name": row["name"], "age": int(row["age"])}
            for row in csv.DictReader(file)
        ]
