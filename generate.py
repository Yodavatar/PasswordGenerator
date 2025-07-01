#Coding : utf-8
#Coding by Yodavatar
#Licensed code MIT License
#App : PasswordGenerator

import random
import string

class generate:
    def __init__(self, seed = int, length = int, uppercase = bool, numbers = bool, symbols = bool) -> None:
        """
        Initialize the password generator.
        """
        self.model = seed
        self.length = length
        self.uppercase = uppercase
        self.numbers = numbers
        self.symbols = symbols

    def generate(self) -> str:
        """
        Generate a password.
        """
        string.digits # Numeric digits
        string.ascii_lowercase # Lowercase letters
        string.ascii_uppercase # Uppercase letters
        string.punctuation # Special characters

        letterpossible = string.ascii_lowercase #default to lowercase letters
        if self.numbers:
            letterpossible += string.digits
        if self.symbols:
            letterpossible += string.punctuation
        if self.uppercase:
            letterpossible += string.ascii_uppercase

        # Generate the password
        password = ''.join(random.choice(letterpossible) for _ in range(self.length))
        return password
    
    def __str__(self) -> str:
        """
        Return a string representation of the password generator.
        """
        return f"Password Generator(seed={self.model}, length={self.length}, uppercase={self.uppercase}, numbers={self.numbers}, symbols={self.symbols})"

#print(generate(12345, 12, True, True, True).generate())  # Example usage

#Coding : utf-8
#Coding by Yodavatar
#Licensed code MIT License
#App : PasswordGenerator