user = input("Enter username: ").strip()
pwd = input("Enter password: ").strip()

auth_success = (user == "admin") and (pwd == "admin123")
print("Login successful" if auth_success else "Invalid username or password")
