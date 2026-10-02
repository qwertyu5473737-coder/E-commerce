def get_user(username, users):
    for user in users:
        if user["username"] == username:
            return user
    return None
