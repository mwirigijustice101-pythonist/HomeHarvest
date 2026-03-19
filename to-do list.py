import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("To-Do List")  # Set window title
root.geometry("300x400")  # Set window size

# List to store tasks
tasks = []

def add_task():
    """Adds a task to the list."""
    task = task_entry.get()  # Get task from the entry field
    if task:
        tasks.append(task)  # Add task to the list
        task_listbox.insert(tk.END, task)  # Display task in the listbox
        task_entry.delete(0, tk.END)  # Clear input field
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")  # Show warning if input is empty

def remove_task():
    """Removes selected task from the list."""
    try:
        selected_task_index = task_listbox.curselection()[0]  # Get index of selected task
        task_listbox.delete(selected_task_index)  # Remove task from listbox
        del tasks[selected_task_index]  # Remove task from the list
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")  # Show warning if no task is selected

# Creating input field, buttons, and task list
task_entry = tk.Entry(root, width=30)  # Input field for entering tasks
task_entry.pack(pady=10)  # Add spacing around the input field

add_button = tk.Button(root, text="Add Task", command=add_task)  # Button to add tasks
add_button.pack()  # Display the button

remove_button = tk.Button(root, text="Remove Task", command=remove_task)  # Button to remove tasks
remove_button.pack()  # Display the button

task_listbox = tk.Listbox(root, width=40, height=15)  # Listbox to display tasks
task_listbox.pack(pady=10)  # Add spacing around the listbox

# Run the application
root.mainloop()