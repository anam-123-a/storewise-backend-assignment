from fastapi import HTTPException


def question2(tasks):
    grouped = {}

    for task in tasks:
        parent = task.parent_id
        if parent not in grouped:
            grouped[parent] = []
        grouped[parent].append(task)

    for parent in grouped:
        grouped[parent].sort(key=lambda x: x.created_at, reverse=True)

    return grouped


from datetime import datetime, timedelta

def question3(tasks):
    result = []
    today = datetime.today().date()
    tomorrow = today + timedelta(days=1)

    for task in tasks:
        if task.priority == 1:
            if task.due_date.date() == today or task.due_date.date() == tomorrow:
                result.append(task)

    return result


def question4(tasks):
    child_parent_ids = set()

   
    for task in tasks:
        if task.parent_id:
            child_parent_ids.add(task.parent_id)

    result = []

    
    for task in tasks:
        if task.id not in child_parent_ids:
            result.append(task)

    return result


def question5(tasks, task_id: int):
    parent_id = None

   
    for task in tasks:
        if task.id == task_id:
            parent_id = task.parent_id
            break

    count = 0

   
    for task in tasks:
        if task.parent_id == parent_id and task.id != task_id:
            count += 1

    return count


def question6(tasks, query: str):
    result = []
    query = query.lower()

    for task in tasks:
        if query in task.name.lower():
            result.append(task)

    return result


def question7(tasks):
    result = []

    for task in tasks:
        current = task
        while current.parent_id:
            parent = next((t for t in tasks if t.id == current.parent_id), None)
            if parent:
                result.append((task.id, parent.id))
                current = parent
            else:
                break

    return result


def question8(tasks, criteria: dict, sort_by: str):
    
    raise HTTPException(status_code=401, detail="For this task, 8, you are expected to solve it using SQLAlchemy. Please don't use this function, and return the result directly from the ")


import time
import threading

def worker(task):
    time.sleep(task.duration / 10)

def question9(tasks, worker_threads: int):
    threads = []

    for task in tasks:
        t = threading.Thread(target=worker, args=(task,))
        threads.append(t)
        t.start()

       
        if len(threads) >= worker_threads:
            for th in threads:
                th.join()
            threads = []

  
    for th in threads:
        th.join()

    return "Tasks executed"
