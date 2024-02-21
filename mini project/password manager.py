from cryptography.fernet import Fernet

# Function to generate and write a new key to file (commented out as it's not needed if the key already exists)
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Function to load the key from file
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

# Load the key from file
key = load_key()

# Get the master password from the user and append it to the key
master_pwd = input("What is the master password? ")
key += master_pwd.encode()

# Create a Fernet instance with the modified key
fer = Fernet(key)

# Function to view decrypted passwords from passwords.txt
def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            # Decrypt and print the username and password
            decrypted_passw = fer.decrypt(passw.encode()).decode()
            print("User:", user, "| Password:", decrypted_passw)

# Function to add encrypted passwords to passwords.txt
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    # Encrypt the password and convert it to a string
    encrypted_pwd = fer.encrypt(pwd.encode()).decode()

    # Append the encrypted account name and password to passwords.txt
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + encrypted_pwd + "\n")

# Main loop for user interaction
while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue  # Continue to the next iteration of the loop if the mode is invalid
