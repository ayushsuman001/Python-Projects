import tkinter as tk

# Create a new window
window = tk.Tk()
window.title("To-Do List Application")

# Create a label widget for the title
title_label = tk.Label(window, text="To-Do List", font=("Arial", 18))
title_label.pack()

# Create a text box widget for entering tasks
task_entry = tk.Entry(window, width=50)
task_entry.pack()

# Create a list box widget for displaying tasks
task_list = tk.Listbox(window, width=50)
task_list.pack()

# Define a function for adding tasks to the list
def add_task():
    task = task_entry.get()
    if task != "":
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)

# Create a button widget for adding tasks
add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack()

# Define a function for removing tasks from the list
def remove_task():
    selected_task = task_list.curselection()
    task_list.delete(selected_task)

# Create a button widget for removing tasks
remove_button = tk.Button(window, text="Remove Task", command=remove_task)
remove_button.pack()

# Start the main event loop
window.mainloop()
