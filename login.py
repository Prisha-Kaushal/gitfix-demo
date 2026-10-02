def login(username, password):
    if username == "admin" and password == "admin123":
        return "Login successful"

    if password == "":
        return "Password cannot be empty"

    return "Invalid username or password"


if __name__ == "__main__":
    print(login("admin", ""))
