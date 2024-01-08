import re
import tkinter as tk
from tkinter import messagebox

def is_strong_password(password):
    # Minimum length requirement
    length_ok = len(password) >= 8

    # Check for the presence of uppercase letters
    uppercase_ok = any(char.isupper() for char in password)

    # Check for the presence of lowercase letters
    lowercase_ok = any(char.islower() for char in password)

    # Check for the presence of digits
    digit_ok = any(char.isdigit() for char in password)

    # Check for the presence of special characters
    special_char_ok = re.search(r'[!@#\$%\^&\*\(\)_\+\-=\[\]\{\};:\'",<>\./?\\|`~]', password) is not None

    # Ensure all criteria are met
    is_strong = length_ok and uppercase_ok and lowercase_ok and digit_ok and special_char_ok

    return is_strong

def check_password_strength():
    password = password_entry.get()

    if is_strong_password(password):
        messagebox.showinfo("Password Strength", "Password is strong!")
    else:
        messagebox.showwarning("Password Strength", "Password is weak. Please consider strengthening it.")

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("300x150")

# Create and place widgets
password_label = tk.Label(root, text="Password:", font=("Helvetica", 12))
password_label.pack(pady=5)

password_entry = tk.Entry(root, show="*", font=("Helvetica", 12))
password_entry.pack(pady=5)

check_button = tk.Button(root, text="Check Password Strength", command=check_password_strength, font=("Helvetica", 12))
check_button.pack(pady=10)

# Run the GUI
root.mainloop()