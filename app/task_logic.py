from fastapi import HTTPException


def question2(tasks):
    pass


def question3(tasks):
    pass


def question4(tasks):
    pass


def question5(tasks, task_id: int):
    pass


from fuzzywuzzy import process

def question6(tasks, query: str):
    # tasks: list of task objects
    task_names = [task.name for task in tasks]
    # Get matches with score >= 60 (tune if needed)
    matches = process.extract(query, task_names, limit=None)
    matched_tasks = [task for task in tasks if any(task.name == name and score >= 60 for name, score in matches)]
    return matched_tasks


def question7(tasks, task1_id, task2_id):
    # Create a dictionary for fast lookup
    task_dict = {task.id: task for task in tasks}

    # Helper: check if t2 is subtask of t1
    def is_subtask(parent_id, child_id):
        current = task_dict.get(child_id)
        while current:
            if current.parent_id == parent_id:
                return True
            current = task_dict.get(current.parent_id)
        return False

    if is_subtask(task1_id, task2_id):
        return f"Task {task2_id} is subtask of Task {task1_id}"
    elif is_subtask(task2_id, task1_id):
        return f"Task {task1_id} is subtask of Task {task2_id}"
    else:
        return None


def question8(tasks, criteria: dict, sort_by: str):
    
    raise HTTPException(status_code=401, detail="For this task, 8, you are expected to solve it using SQLAlchemy. Please don't use this function, and return the result directly from the ")


def question9(tasks, worker_threads: int):
    pass
