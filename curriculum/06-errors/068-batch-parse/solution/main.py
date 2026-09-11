def parse_counts(lines):
    values = []
    errors = []
    for number, line in enumerate(lines, start=1):
        try:
            values.append(int(line))
        except ValueError:
            errors.append(number)
    return {"values": values, "errors": errors}
