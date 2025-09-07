from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Task(BaseModel):
  id: int
  title:str

to_do_list = []

#add task
@app.post("/tasks")
def add_task(task: Task):
      to_do_list.append(task.model_dump())
      return{"message": "Holla! you have added", "task": task}

#get task
@app.get("/all_tasks")
def get_all_task():
  return{"all_task": to_do_list}

#get single task by id and title 
@app.get("/tasks/{task_id}/{task_title}")
def get_task(task_id:int, task_title:str):
  for task in to_do_list:
    if task["id"] == task_id and task["title"] == task_title:
        return{"task": task}
  return{"Error": "You do not have this task"}
    

#delete task by id and title
@app.delete("/task/{task_id}/{task_title}")
def delete_task(task_id:int, task_title:str):
  for task in to_do_list:
    if task["id"] == task_id and task["title"] == task_title:
     to_do_list.remove(task)
     return{"message": "This task is deleted"}
  return{"Error": "You do not have this task"}
    
#update to do
@app.patch("/task/{task_id}")
def update_task(task_id:int, updated_task:Task):
  for task in to_do_list:
    if task["id"] == task_id:
     task.update(updated_task.model_dump())
     return{"message": "This task is updated", "task": task}
  return{"Error": "You do not have this task"}



