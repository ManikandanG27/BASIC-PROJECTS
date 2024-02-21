from cryptography.fernet import Fernet

# Function to load the encryption key from file
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

# Load the encryption key
key = load_key()
fer = Fernet(key)

# Function to view decrypted passwords from passwords.txt
def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            # Decrypt and print the username and password
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())

# Function to add encrypted passwords to passwords.txt
def add():
    name = input('Account Name: ')
    pwd = input("Password: ")
    with open('passwords.txt', 'a') as f:
        # Write the encrypted username and password to file
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

# Main loop for user interaction
while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")  # Notify the user of invalid input
        continue  # Continue to the next iteration of the loop
