1

import os
from cryptography.fernet import Fernet

# ------------------ Fernet Encryption ------------------

def generate_key():
    """Generate a Fernet key."""
    return Fernet.generate_key()

def save_key(key, filename="secret.key"):
    """Save the Fernet key to a file."""
    with open(filename, "wb") as key_file:
        key_file.write(key)

def load_key(filename="secret.key"):
    """Load the Fernet key from a file."""
    return open(filename, "rb").read()

def encrypt_file(input_file, output_file, key):
    """Encrypt a file using Fernet."""
    fernet = Fernet(key)
    with open(input_file, "rb") as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(output_file, "wb") as file:
        file.write(encrypted)

def decrypt_file(input_file, output_file, key):
    """Decrypt a file using Fernet."""
    fernet = Fernet(key)
    with open(input_file, "rb") as file:
        encrypted = file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(output_file, "wb") as file:
        file.write(decrypted)

# ------------------ Caesar Cipher ------------------

def caesar_encrypt(text, shift):
    """Encrypt text using Caesar cipher."""
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    """Decrypt text using Caesar cipher."""
    return caesar_encrypt(text, -shift)

def caesar_encrypt_file(input_file, output_file, shift):
    """Encrypt a file using Caesar cipher."""
    with open(input_file, "r") as file:
        original = file.read()
    encrypted = caesar_encrypt(original, shift)
    with open(output_file, "w") as file:
        file.write(encrypted)

def caesar_decrypt_file(input_file, output_file, shift):
    """Decrypt a file using Caesar cipher."""
    with open(input_file, "r") as file:
        encrypted = file.read()
    decrypted = caesar_decrypt(encrypted, shift)
    with open(output_file, "w") as file:
        file.write(decrypted)

# ------------------ Main Program ------------------

if __name__ == "__main__":
    print("Choose encryption method: 1) Fernet  2) Caesar Cipher")
    choice = input("Enter choice (1/2): ")

    if choice == "1":
        # Fernet encryption
        if not os.path.exists("secret.key"):
            key = generate_key()
            save_key(key)
        else:
            key = load_key()

        action = input("Do you want to encrypt or decrypt? (e/d): ")
        if action == "e":
            input_file = input("Enter the file to encrypt: ")
            output_file = input("Enter the output encrypted file name: ")
            encrypt_file(input_file, output_file, key)
            print("File encrypted successfully!")
        elif action == "d":
            input_file = input("Enter the file to decrypt: ")
            output_file = input("Enter the output decrypted file name: ")
            decrypt_file(input_file, output_file, key)
            print("File decrypted successfully!")

    elif choice == "2":
        # Caesar cipher
        shift = int(input("Enter shift value for Caesar Cipher: "))
        action = input("Do you want to encrypt or decrypt? (e/d): ")
        if action == "e":
            input_file = input("Enter the file to encrypt: ")
            output_file = input("Enter the output encrypted file name: ")
            caesar_encrypt_file(input_file, output_file, shift)
            print("File encrypted successfully!")
        elif action == "d":
            input_file = input("Enter the file to decrypt: ")
            output_file = input("Enter the output decrypted file name: ")
            caesar_decrypt_file(input_file, output_file, shift)
            print("File decrypted successfully!")