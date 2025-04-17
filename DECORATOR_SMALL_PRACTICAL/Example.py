# Simulated session storage
session = {
    "logged_in": False,
    "email": ""
}

# Dummy credentials for demo
valid_email = "user@example.com"
valid_password = "123456"

# Decorator to check if user is logged in
def login_required(func):
    def wrapper():
        if session["logged_in"]:
            func()
        else:
            print("Access denied! Please log in first.\n")
    return wrapper

# Login function (no decorator here!)
def login():
    email = input("Enter email: ")
    password = input("Enter password: ")

    if email == valid_email and password == valid_password:
        session["logged_in"] = True
        session["email"] = email
        print("\nLogin successful!\n")
    else:
        print("\nInvalid email or password.\n")

# Protected functions

@login_required
def profile():
    print(f"Welcome, {session['email']}! This is your profile.\n")

@login_required
def account():
    print("Here is your account information.\n")

# Logout function
def logout():
    session["logged_in"] = False
    session["email"] = ""
    print("You have been logged out.\n")

# Menu to interact
def main():
    while True:
        print("=== Menu ===")
        print("1. Login")
        print("2. Profile")
        print("3. Account")
        print("4. Logout")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            login()
        elif choice == "2":
            profile()
        elif choice == "3":
            account()
        elif choice == "4":
            logout()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print(" Invalid choice. Try again.\n")

# Run the program
main()
