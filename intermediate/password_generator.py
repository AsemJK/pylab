import string
import random

def generate_password(min_length = 8,numbers = True,special_chars = True):
    letters = string.ascii_letters
    digits = string.digits if numbers else ''
    specials = string.punctuation if special_chars else ''
    all_characters = letters + digits + specials
    if len(all_characters) == 0:
        raise ValueError("At least one character type must be selected.")
    password = ''.join(random.choice(all_characters) for _ in range(min_length))
    return password


# Example usage
if __name__ == "__main__":
    print("Generated Password:", generate_password(12, True, True))
    print("Generated Password:", generate_password(10, False, True))
    print("Generated Password:", generate_password(15, True, False))
    print("Generated Password:", generate_password(8, False, False))  # Only letters