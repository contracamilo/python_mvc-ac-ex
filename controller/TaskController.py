from model import Task, TaskList
from view import TaskView


class TaskController:
    """
       App class controller.

       Attributes:
       - task_list: Task List.
       - view: View instance for the UI.
    """

    def __init__(self):
        self.task_list = TaskList()
        self.view = TaskView(self)

    def run(self):
        self.view.start()

    def add_task(self, title, description):
        if title:
            task = Task(title, description)
            self.task_list.add_task(task)
            self.update_view()
        else:
            self.view.show_error("Título no puede estar vacío.")



    def edit_task(self, index, title, description):
        if index is not None:
            self.task_list.edit_task(index, title, description)
            self.update_view()

    def delete_task(self, task_id):
        if task_id is not None:
            try:
                self.task_list.remove_task(task_id)
                self.update_view()
            except ValueError:
                self.view.show_error("No se encontró ninguna tarea con el ID dado.")

    def mark_completed(self, index):
        if index is not None:
            self.task_list.mark_completed(index)
            self.update_view()

    def update_view(self):
        self.view.update_view(self.task_list.tasks)
