# view.py
import tkinter as tk
from tkinter import simpledialog, messagebox


class TaskView:
    """
    Class that represents View using Tkinter para la GUI.

    Attributes:
    - controller: Controller instance to connect with Model
    - root: Main app window
    - task_listbox: Listbox to show the task list
    """

    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Lista de Tareas")
        self.task_listbox = tk.Listbox(self.root)
        self.task_listbox.pack(fill=tk.BOTH, expand=True)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack()

        tk.Button(btn_frame, text="Agregar", command=self.add_task).pack(side=tk.LEFT)
        tk.Button(btn_frame, text="Editar", command=self.edit_task).pack(side=tk.LEFT)
        tk.Button(btn_frame, text="Eliminar", command=self.delete_task).pack(side=tk.LEFT)
        tk.Button(btn_frame, text="Completar", command=self.mark_completed).pack(side=tk.LEFT)

    def update_view(self, tasks):
        self.task_listbox.delete(0, tk.END)
        for task in tasks:
            status = "✔" if task.completed else "✘"
            self.task_listbox.insert(tk.END, f"{task.task_id} {task.title} - {task.description} [{status}]")

    def add_task(self):
        title, description = self.get_task_input()
        self.controller.add_task(title, description)

    def edit_task(self):
        index = self.get_task_index()
        title, description = self.get_task_input()
        self.controller.edit_task(index, title, description)

    def delete_task(self):
        index = self.get_task_index()
        self.controller.delete_task(index)

    def mark_completed(self):
        index = self.get_task_index()
        self.controller.mark_completed(index)

    def get_task_input(self):
        title = simpledialog.askstring("Entrada", "Título:")
        description = simpledialog.askstring("Entrada", "Descripción:")
        return title, description

    def get_task_index(self):
        try:
            return int(simpledialog.askstring("Entrada", "Número de la tarea:"))
        except (ValueError, TypeError):
            messagebox.showerror("Error", "Índice inválido.")
            return None

    def show_error(self, message):
        messagebox.showerror("Error", message)
    def start(self):
        self.root.mainloop()
