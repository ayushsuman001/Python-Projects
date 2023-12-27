import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.tasks = []

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, width=40, height=10)
        self.task_listbox.pack()

        mark_button = tk.Button(root, text="Mark as Completed", command=self.mark_task)
        mark_button.pack(pady=5)

        delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        delete_button.pack(pady=5)

        self.task_listbox.bind("<Double-Button-1>", lambda event: self.mark_task())

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def mark_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            self.tasks[task_index] = "[Completed] " + self.tasks[task_index]
            self.update_task_list()

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            del self.tasks[task_index]
            self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
