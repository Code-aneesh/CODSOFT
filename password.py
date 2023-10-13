import random
import string

def generate_password(length,lowercase, uppercase, digits,special_chars):
   
    charset = ""
    if lowercase:
        charset += string.ascii_lowercase
    if uppercase:
        charset += string.ascii_uppercase
    if digits:
        charset += string.digits
    if special_chars:
        charset += string.punctuation

    if not charset:
        return "Please select at least one character set for the password."
    password = ''.join(random.choice(charset) for _ in range(length))
    return password
def main():
    print("Password Generator")
    length = int(input("Enter the desired password length: "))
    lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
    uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
    digits = input("Include digits? (y/n): ").lower() == "y"
    special_chars = input("Include special characters? (y/n): ").lower() == "y"
    password = generate_password(length, lowercase, uppercase, digits, special_chars)
    print("Generated Password:", password)
if __name__ == "__main__":
    main()
