from fastapi import HTTPException

from collections import defaultdict

def question2(tasks):
    grouped = defaultdict(list)
    for task in tasks:
        grouped[task.parent_id].append(task)
    
 
    for parent in grouped:
        grouped[parent].sort(key=lambda t: t.created_at, reverse=True)
    return grouped


from datetime import datetime, timedelta

def question3(tasks):
    today = datetime.now().date()
    tomorrow = today + timedelta(days=1)
    
    result = []
    for task in tasks:
        due_date = task.due_date.date()
        if (due_date == today or due_date == tomorrow) and task.priority == 1:
            result.append(task)
    return result


def question4(tasks):
    child_parent_ids = set(task.parent_id for task in tasks if task.parent_id != 0)
    parents = [task for task in tasks if task.id not in child_parent_ids and task.parent_id == 0]
    return parents


def question5(tasks, task_id: int):
    # Find the task
    task = next((t for t in tasks if t.id == task_id), None)
    if not task:
        return 0
    parent_id = task.parent_id
    siblings = [t for t in tasks if t.parent_id == parent_id and t.id != task_id]
    return len(siblings)


from fuzzywuzzy import fuzz

def question6(tasks, query: str):

    result = []
    for task in tasks:
        similarity = fuzz.partial_ratio(task.name.lower(), query.lower())
        if similarity >= 70:  # 70% match threshold
            result.append(task)
    return result


def question7(tasks):
 
    task_dict = {task.id: task for task in tasks}

    def get_parent_chain(task_id):
        chain = []
        current = task_dict.get(task_id)
        while current and current.parent_id != 0:
            chain.append(current.parent_id)
            current = task_dict.get(current.parent_id)
        return chain

    result = {}
    for task in tasks:
        chain = get_parent_chain(task.id)
        result[task.id] = chain if chain else None
    return result


from datetime import datetime

def question8(tasks, start_date, end_date):
 
    result = []
    for task in tasks:
        created = task.created_at.date()
        if start_date <= created <= end_date:
            if task.status != "completed" and created.weekday() != 6:  # Sunday = 6
                result.append(task)
    return result


import asyncio

async def execute_task(task, duration):
    print(f"Executing task {task.name}")
    await asyncio.sleep(duration / 10)  # duration/10 seconds for demo
    print(f"Finished task {task.name}")

def question9(tasks, worker_threads: int):
    async def worker():
        semaphore = asyncio.Semaphore(worker_threads)
        async def run(task):
            async with semaphore:
                await execute_task(task, task.duration)

        await asyncio.gather(*(run(task) for task in tasks))

    asyncio.run(worker())
