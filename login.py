def login(username, password):
    if username == "admin" and password == "admin123":
        return "Login successful"

    if password == "":
        return password.strip()

    return "Invalid username or password"


if __name__ == "__main__":
    print(login("admin", ""))
