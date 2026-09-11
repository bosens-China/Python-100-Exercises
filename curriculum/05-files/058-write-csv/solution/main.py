import csv


def write_people(path, people):
    with open(path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerows(people)
