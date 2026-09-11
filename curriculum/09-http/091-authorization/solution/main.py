def can_edit(user, owner_id):
    if user is None:
        return False
    return user["role"] == "admin" or user["id"] == owner_id
