from login import login


def test_empty_password():
    result = login("admin", "")
    assert result == "Password cannot be empty"


def test_valid_login():
    result = login("admin", "admin123")
    assert result == "Login successful"


def test_invalid_login():
    result = login("admin", "wrongpassword")
    assert result == "Invalid username or password"
