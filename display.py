#Coding : utf-8
#Coding by Yodavatar
#Licensed code MIT License
#App : PasswordGenerator

import tkinter
from tkinter import ttk
from generate import generate
from seed import*
from security import*

class PasswordGeneratorApp:
    """
    A simple password generator application using Tkinter.
    """
    def __init__(self, baseName=None, useTk=True, sync=False, use=None) -> None:
        """
        Initializes the PasswordGeneratorApp with a Tkinter window.
        """
        self.seed = int # Default seed value
        self.uppercase = False # Default to lowercase letters
        self.numbers = False # Default to no numbers
        self.symbols = False # Default to no symbols
        self.password = str # Default password value

        # Init the Tkinter App
        self.app = tkinter.Tk(screenName="Password Generator", baseName=baseName, useTk=useTk, sync=sync, use=use)
        self.app.geometry("500x400")
        self.app.title("Password Generator")
        # Initialize the grid of the App
        self.frame = ttk.Frame(self.app, padding=10)
        self.frame.grid()

        self.label1 = tkinter.Label(self.frame, text="Create a new password:")
        self.label1.grid(column=0, row=0, columnspan=3)

        self.button1 = tkinter.Button(self.frame, text="Desactivate Uppercase", bg="red", fg="white", command=self.ButtonUppercase)
        self.button1.grid(column=0, row=1)

        self.button2 = tkinter.Button(self.frame, text="Desactivate Numbers", bg="red", fg="white", command=self.ButtonNumbers)
        self.button2.grid(column=1, row=1)

        self.button3 = tkinter.Button(self.frame, text="Desactivate Symbols", bg="red", fg="white", command=self.ButtonSymbols)
        self.button3.grid(column=2, row=1)

        self.labelentry = tkinter.Label(self.frame, text="Length of password ->")
        self.labelentry.grid(column=0, row=2)

        self.entry = tkinter.Entry(self.frame, width=30)
        self.entry.grid(column=1, row=2)

        self.labelentry2 = tkinter.Label(self.frame, text="Maximum length: 50")
        self.labelentry2.grid(column=2, row=2)

        self.generate_button = tkinter.Button(self.frame, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(column=0, row=3, columnspan=3)

        self.label2 = tkinter.Label(self.frame, text="Your password will be generated here:")
        self.label2.grid(column=0, row=4, columnspan=3)

        self.copypassword = tkinter.Button(self.frame, text="Copy Password", bg="blue", fg="white", command=self.copy_password)
        self.copypassword.grid(column=1, row=5)

        self.label3 = tkinter.Label(self.frame, text="Your password security level is:")
        self.label3.grid(column=0, row=6, columnspan=3)

    def copy_password(self) -> None:
        """
        Copy the generated password to the clipboard.
        """
        if self.password:
            self.app.clipboard_clear()
            self.app.clipboard_append(self.password)

    def generate_password(self) -> None:
        """
        Generate a password based on user input and options selected.
        """
        if not self.entry.get().isdigit() or int(self.entry.get()) <= 0 or int(self.entry.get()) > 50:
            self.label2.config(text="Please enter a valid positive integer for password length.")
        else:
            self.length = int(self.entry.get())
            self.seed = create_seed()
            self.password = generate(self.seed, self.length, self.uppercase, self.numbers, self.symbols).generate()
            self.label2.config(text=self.password)

            security_check = security(self.password)
            self.label3.config(text=security_check.security_level())

    def ButtonUppercase(self) -> None:
        """
        Toggle the uppercase option.
        """
        self.uppercase = not self.uppercase
        if self.uppercase:
            self.button1.config(bg="green", text="Activate Uppercase")
        else:
            self.button1.config(bg="red", text="Desactivate Uppercase")

    def ButtonNumbers(self) -> None:
        """
        Toggle the numbers option.
        """
        self.numbers = not self.numbers
        if self.numbers:
            self.button2.config(bg="green", text="Activate Numbers")
        else:
            self.button2.config(bg="red", text="Desactivate Numbers")

    def ButtonSymbols(self) -> None:
        """
        Toggle the symbols option.
        """
        self.symbols = not self.symbols
        if self.symbols:
            self.button3.config(bg="green", text="Activate Symbols")
        else:
            self.button3.config(bg="red", text="Desactivate Symbols")

#Coding : utf-8
#Coding by Yodavatar
#Licensed code MIT License
#App : PasswordGenerator