import random
import string
#python code to generate passwords
def generate_password(length, strength):
    """
    Generates a random password of the specified length, containing a mix of lowercase letters, uppercase letters, numbers, and symbols.
    """
    if strength == "weak":
        words = ["password", "secret", "1234"]
        return random.choice(words)
    elif strength == "medium":
        length = 8
    else:
        length = 12
        
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    password_strength = input("How strong do you want your password to be? (weak/medium/strong)")
    password = generate_password(0, password_strength)
    print("Your password is:", password)

if __name__ == "__main__":
    main()
