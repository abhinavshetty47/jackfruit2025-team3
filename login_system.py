import hashlib
import os
import pandas as pd
from datetime import datetime

USER_FILE = "users.txt"
LOG_FILE = "login_logs.csv"

# Password Hashing Function
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Register User
def register():
    username = input("Enter new username: ").strip()
    password = input("Enter new password: ").strip()

    if not username or not password:
        print("Username and password cannot be empty!")
        return

    # Check duplicate user
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            for line in f:
                stored_user, _ = line.strip().split(":")
                if stored_user == username:
                    print("Username already exists!")
                    return

    hashed = hash_password(password)

    with open(USER_FILE, "a") as f:
        f.write(f"{username}:{hashed}\n")

    print("Registration successful!")

# Log Login Attempts using Pandas
def log_attempt(username, status):
    entry = {
        "Username": username,
        "Status": status,
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # If CSV exists → read it
    if os.path.exists(LOG_FILE):
        df = pd.read_csv(LOG_FILE)
        df = pd.concat([df, pd.DataFrame([entry])], ignore_index=True)
    else:
        df = pd.DataFrame([entry])

    df.to_csv(LOG_FILE, index=False)

# Login User
def login():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    hashed = hash_password(password)

    if not os.path.exists(USER_FILE):
        print("No users registered!")
        return

    with open(USER_FILE, "r") as f:
        for line in f:
            stored_user, stored_pass = line.strip().split(":")
            if stored_user == username and stored_pass == hashed:
                print("Login successful! Welcome", username)
                log_attempt(username, "Success")
                return

    print("Invalid credentials!")
    log_attempt(username, "Failed")

# Menu
def main():
    while True:
        print("\n---- Secure Login System ----")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()

    

