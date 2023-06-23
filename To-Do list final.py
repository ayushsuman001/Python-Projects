import tkinter as tk

window = tk.Tk()
window.title("To-Do List Application")

title_label = tk.Label(window, text="To-Do List", font=("Arial", 18))
title_label.pack()

task_entry = tk.Entry(window, width=50)
task_entry.pack()

task_list = tk.Listbox(window, width=50)
task_list.pack()

# Define a function for adding tasks to the list
def add_task():
    task = task_entry.get()
    if task != "":
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)

add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack()

def remove_task():
    selected_task = task_list.curselection()
    task_list.delete(selected_task)

remove_button = tk.Button(window, text="Remove Task", command=remove_task)
remove_button.pack()

window.mainloop()
