#!/usr/bin/python3

import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.current_file = ""
        self.root.title("Simple Text Editor")
        self.text_area = tk.Text(self.root)
        self.text_area.pack(fill=tk.BOTH, expand=True)

        self.create_menu()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_file_as)
        menu_bar.add_cascade(label="File", menu=file_menu)
        menu_bar.add_command(label="Exit", command=self.root.quit)

        self.root.config(menu=menu_bar)

    def new_file(self):
        self.current_file = False
        self.text_area.delete("1.0", tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
        if file_path:
            self.current_file = file_path
            with open(file_path, "r") as file:
                content = file.read()
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, content)

    def save_file(self):
        file_path = self.current_file
        if file_path:
            with open(file_path, "w") as file:
                content = self.text_area.get("1.0", tk.END)
                file.write(content)
            messagebox.showinfo("Information", "File saved successfully.")
        else:
            messagebox.showinfo("Information", "No file selected")
            self.save_file_as()

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(filetypes=[("All Files", "*.*")])
        if file_path:
            self.current_file = file_path
            with open(file_path, "w") as file:
                content = self.text_area.get("1.0", tk.END)
                file.write(content)
            messagebox.showinfo("Information", "File saved successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()

