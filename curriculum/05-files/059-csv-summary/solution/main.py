import csv


def sales_total(path):
    with open(path, encoding="utf-8", newline="") as file:
        return sum(
            int(row["price"]) * int(row["quantity"]) for row in csv.DictReader(file)
        )
