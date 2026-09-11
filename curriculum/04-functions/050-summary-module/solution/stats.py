def total(numbers):
    return sum(numbers)


def mean(numbers):
    if not numbers:
        return None
    return total(numbers) / len(numbers)
