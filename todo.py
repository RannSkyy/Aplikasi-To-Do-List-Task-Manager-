import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "tasks.json"

# ================= LOAD TASK =================
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

# ================= SAVE TASK =================
def save_tasks():
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

# ================= ADD TASK =================
def add_task():
    task = entry.get()
    if task == "":
        messagebox.showwarning("Warning", "Task tidak boleh kosong")
        return
    tasks.append({"task": task, "done": False})
    entry.delete(0, tk.END)
    save_tasks()
    refresh_list()

# ================= TOGGLE DONE =================
def toggle_done():
    try:
        index = listbox.curselection()[0]
        tasks[index]["done"] = not tasks[index]["done"]
        save_tasks()
        refresh_list()
    except:
        messagebox.showwarning("Warning", "Pilih task terlebih dahulu")

# ================= DELETE TASK =================
def delete_task():
    try:
        index = listbox.curselection()[0]
        tasks.pop(index)
        save_tasks()
        refresh_list()
    except:
        messagebox.showwarning("Warning", "Pilih task terlebih dahulu")

# ================= REFRESH LIST =================
def refresh_list():
    listbox.delete(0, tk.END)
    for t in tasks:
        status = "✔" if t["done"] else "✖"
        listbox.insert(tk.END, f"{status} {t['task']}")

# ================= UI =================
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x450")
root.resizable(False, False)

tasks = load_tasks()

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=10, padx=10, fill=tk.X)

btn_add = tk.Button(root, text="Tambah Task", command=add_task)
btn_add.pack(pady=5)

listbox = tk.Listbox(root, font=("Arial", 12))
listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

btn_done = tk.Button(root, text="Tandai Selesai", command=toggle_done)
btn_done.pack(pady=5)

btn_delete = tk.Button(root, text="Hapus Task", command=delete_task)
btn_delete.pack(pady=5)

refresh_list()
root.mainloop()