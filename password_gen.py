import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Password Generator By Ayon")
        self.root.geometry("400x300")

        self.root.configure(bg="white")
       
        tk.Label(root, text="Password Length:", bg="white", fg="black", font=("Arial", 12)).pack(pady=5)
        self.length_var = tk.IntVar(value=12)
        tk.Entry(root, textvariable=self.length_var, font=("Arial", 12), bg="#F5F5F5", fg="#333").pack(pady=5)

        self.include_uppercase = tk.BooleanVar(value=True)
        self.include_numbers = tk.BooleanVar(value=True)
        self.include_symbols = tk.BooleanVar(value=True)

        tk.Checkbutton(root, text="Include Uppercase Letters", variable=self.include_uppercase, bg="white", fg="black", selectcolor="#D3D3D3", font=("Arial", 10)).pack(anchor="w", padx=20)
        tk.Checkbutton(root, text="Include Numbers", variable=self.include_numbers, bg="white", fg="black", selectcolor="#D3D3D3", font=("Arial", 10)).pack(anchor="w", padx=20)
        tk.Checkbutton(root, text="Include Symbols", variable=self.include_symbols, bg="white", fg="black", selectcolor="#D3D3D3", font=("Arial", 10)).pack(anchor="w", padx=20)

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password, font=("Arial", 12), bg="#4A90E2", fg="white", activebackground="#357ABD", activeforeground="white", bd=0)
        self.generate_button.pack(pady=10)

        self.password_entry = tk.Entry(root, font=("Arial", 14), justify="center", bg="#F5F5F5", fg="#333")
        self.password_entry.pack(pady=10, fill="x", padx=20)


        self.copy_button = tk.Button(root, text="Copy Password", command=self.copy_to_clipboard, font=("Arial", 12), bg="#4A90E2", fg="white", activebackground="#357ABD", activeforeground="white", bd=0)
        self.copy_button.pack(pady=5)

    def generate_password(self):
        try:
            length = self.length_var.get()
            if length < 4:
                messagebox.showerror("Error", "Password length must be at least 4 characters.")
                return

            characters = string.ascii_lowercase

            if self.include_uppercase.get():
                characters += string.ascii_uppercase

            if self.include_numbers.get():
                characters += string.digits

            if self.include_symbols.get():
                characters += string.punctuation

            if not characters:
                messagebox.showerror("Error", "No character set selected.")
                return

            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, password)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def copy_to_clipboard(self):
        password = self.password_entry.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            self.root.update()
            messagebox.showinfo("Copied", "Password copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No password to copy. Please generate.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
