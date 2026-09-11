def active_names(users):
    return [user["name"] for user in users if user["active"]]
