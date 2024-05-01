class Task:
    """
    Class that represents a task.

    Attributes:
    - title: Task title.
    - description: Task desc.
    - completed: task status finished or not.
    """

    def __init__(self, title, description='', task_id=0):
        self.task_id = id
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True


class TaskList:
    """
    Class that represents a list of task.

    Attributes:
    - tasks: List of task objects
    """

    def __init__(self):
        self.tasks = []
        self.task_counter = 0

    def add_task(self, task):
        task.task_id = self.task_counter
        self.tasks.append(task)
        self.task_counter += 1

    def edit_task(self, index, title=None, description=None):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            if title:
                task.title = title
            if description:
                task.description = description

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
