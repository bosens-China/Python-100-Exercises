def group_names(names):
    groups = {}
    for name in names:
        key = name[0]
        if key not in groups:
            groups[key] = []
        groups[key].append(name)
    return groups
