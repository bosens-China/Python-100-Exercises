from stats import total, mean


def summarize(numbers):
    return {"count": len(numbers), "total": total(numbers), "mean": mean(numbers)}
