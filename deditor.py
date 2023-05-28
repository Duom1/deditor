#!/usr/bin/python3

import sys, os
import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditor:
    def __init__(self, root, path):
        self.root = root
        self.current_file = path
        self.root.title("Deditor")
        self.text_area = tk.Text(self.root)
        self.text_area.pack(fill=tk.BOTH, expand=True)

        self.create_menu()
        self.key_binds()

        if self.current_file != False and os.path.isfile(self.current_file):
            with open(self.current_file) as file:
                content = file.read()
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, content)

    def key_binds(self):
        self.root.bind("<Control-q>", lambda x: self.root.quit())
        self.root.bind("<Control-o>", lambda x: self.open_file())
        self.root.bind("<Control-s>", lambda x: self.save_file())
        self.root.bind("<Control-S>", lambda x: self.save_file_as())
        self.root.bind("<Control-n>", lambda x: self.new_file())

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", accelerator="Ctrl+n", command=self.new_file)
        file_menu.add_command(label="Open", accelerator="Ctrl+o", command=self.open_file)
        file_menu.add_command(label="Save", accelerator="Ctrl+s", command=self.save_file)
        file_menu.add_command(label="Save As", accelerator="Ctrl+Shift+s", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", accelerator="Ctrl+q", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        menu_bar.add_command(label="About", command=self.about)

        self.root.config(menu=menu_bar)

    def about(self):
        messagebox.showinfo("About", "Deditor (Duomi Editor) is a text editor written in python by Duom1 on github")

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
    if len(sys.argv) > 1:
        editor = TextEditor(root, os.path.abspath(sys.argv[1]))
    else:
        editor = TextEditor(root, False)
    root.mainloop()

