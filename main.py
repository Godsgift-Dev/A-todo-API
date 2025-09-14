from fastapi import FastAPI
from pydantic import BaseModel
from db import todo_collection
from bson import ObjectId

app = FastAPI()

class Task(BaseModel):

  title:str                                                                                



#add task
@app.post("/tasks")
def add_task(task: Task):
      todo_collection.insert_one(task.model_dump())
      return{"message": "Holla! you have added", "task": task}

#get task
@app.get("/all_tasks")
def get_all_task():
 tasks = list(todo_collection.find({}, {"_id": 0}))
 return{"all_task": tasks}

#get single task by id and title 
@app.get("/tasks/{task_id}/{task_title}")
def get_task(task_id:int, task_title:str):
   task = list(todo_collection.find_one({"id": ObjectId(task_id), "title": task_title}))
   if task:
    return{"task": task}
   return{"Error": "You do not have this task"}
    

#delete task by id and title
@app.delete("/task/{task_id}/{task_title}")
def delete_task(task_id:int, task_title:str):
  for task in todo_collection:
    if task["id"] == task_id and task["title"] == task_title:
     todo_collection.remove(task)
     return{"message": "This task is deleted"}
  return{"Error": "You do not have this task"}
    
#update to do
@app.patch("/task/{task_id}")
def update_task(task_id:int, updated_task:Task):
  for task in todo_collection:
    if task["id"] == task_id:
     task.update(updated_task.model_dump())
     return{"message": "This task is updated", "task": task}
  return{"Error": "You do not have this task"}



