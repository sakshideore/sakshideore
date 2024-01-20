import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = length_scale.get()
    complexity = complexity_scale.get()

    if length <= 0:
        messagebox.showerror("Error", "Password length must be greater than zero.")
        return

    if complexity <= 0:
        messagebox.showerror("Error", "Password complexity must be greater than zero.")
        return

    characters = ""
    if complexity >= 1:
        characters += string.ascii_letters
    if complexity >= 2:
        characters += string.digits
    if complexity >= 3:
        characters += string.punctuation

    password = ''.join(random.choices(characters, k=length))
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)

def reset_password():
    length_scale.set(8)
    complexity_scale.set(1)
    password_entry.delete(0, tk.END)

root = tk.Tk()
root.title("PASSWORD GENERATOR")

# Heading
heading_label = tk.Label(root, text="Password Generator", font=("bold", 20))
heading_label.pack(pady=10)

# User Name Entry
user_label = tk.Label(root, text="User Name:")
user_label.pack()
user_entry = tk.Entry(root)
user_entry.pack(pady=5)

# Password Length Entry
length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_scale = tk.Scale(root, from_=1, to=50, orient=tk.HORIZONTAL, length=200)
length_scale.set(8)
length_scale.pack(pady=5)

# Password Complexity Entry
complexity_label = tk.Label(root, text="Password Complexity:")
complexity_label.pack()
complexity_scale = tk.Scale(root, from_=1, to=3, orient=tk.HORIZONTAL, length=200)
complexity_scale.set(1)
complexity_scale.pack(pady=5)

# Generate Password Button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Password Display
password_label = tk.Label(root, text="Password:",font=("bold", 20))
password_label.pack()
password_entry = tk.Entry(root)
password_entry.pack(pady=5)

# Reset Password Button
reset_button = tk.Button(root, text="Reset Password", command=reset_password)
reset_button.pack(pady=10)

root.mainloop()