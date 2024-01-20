import os
import tkinter as tk
from tkinter import messagebox

class TodoList(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("TO-DO LIST")
        self.geometry("400x300")

        self.frame = tk.Frame(self)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.create_widgets()

        self.tasks = []

        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as file:
                for line in file:
                    self.tasks.append(line.strip())

        self.load_tasks()

    def create_widgets(self):
        self.listbox = tk.Listbox(self.frame, width=50, height=10)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox.config(yscrollcommand=self.scrollbar.set)

        self.entry = tk.Entry(self.frame, width=50)
        self.entry.pack(fill=tk.X, pady=10)

        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(self.frame, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.clear_button = tk.Button(self.frame, text="Clear Completed", command=self.clear_completed)
        self.clear_button.pack(pady=5)

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
            self.save_tasks()

    def delete_task(self):
        selected_task = self.listbox.get(tk.ANCHOR)
        if selected_task:
            self.tasks.remove(selected_task)
            self.listbox.delete(self.listbox.curselection())
            self.save_tasks()

    def clear_completed(self):
        self.tasks = [task for task in self.tasks if not task.startswith("* ")]
        self.listbox.delete(0, tk.END)
        self.load_tasks()

    def load_tasks(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            if task.startswith("* "):
                self.listbox.insert(tk.END, task[2:])
            else:
                self.listbox.insert(tk.END, task)

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task}\n")

    def on_closing(self):
        self.save_tasks()
        messagebox.showinfo("Goodbye", "Your tasks have been saved.")

if __name__ == "__main__":
    app = TodoList()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()