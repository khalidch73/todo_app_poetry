from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
import database
from typing import List

app = FastAPI(title="Todos API", 
    version="0.0.1",
    servers=[
        {
            "url": "https://pleasantly-pumped-gecko.ngrok-free.app", # ADD NGROK URL Here Before Creating GPT Action
            "description": "Development Server"
        }
        ])

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic model for input data
class TodoCreate(BaseModel):
    id: int
    title: str
    description: str

# Pydantic model for returning todo data
class Todo(BaseModel):
    id: int
    title: str
    description: str

# 01 Endpoint to main todo app
@app.get("/")
def main_todo_route():
    return {"message": "My Todo_App"}

# 02 Endpoint to retrieve all todos
@app.get("/alltodos/", response_model=List[Todo])
def get_all_todos(db: Session = Depends(get_db)):
    all_todos = db.query(database.Todo).all()
    if all_todos is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return all_todos

# 03 Endpoint to retrieve a todo by its ID
@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo_by_id(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(database.Todo).filter(database.Todo.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

# 04 Endpoint to create a new todo
@app.post("/todos/")
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    # Create a new Todo instance from the input data
    db_todo = database.Todo(id=todo.id, title=todo.title, description=todo.description)
    # Add the new Todo to the database session
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


# 05 Endpoint to update an existing todo or create a new todo if it does not already exist
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = db.query(database.Todo).filter(database.Todo.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    for key, value in todo.dict().items():  # Corrected from updated_todo to todo
        setattr(db_todo, key, value)
    db.commit()
    return db_todo

# 07 Endpoint to delete a todo by ID
@app.delete("/todos/{todo_id}")
def delete_todo_by_id(todo_id: int, db: Session = Depends(get_db)):
    # Retrieve the todo from the database
    db_todo = db.query(database.Todo).filter(database.Todo.id == todo_id).first()
    if db_todo is None:
        # If todo with the given ID is not found, raise 404 Not Found error
        raise HTTPException(status_code=404, detail="Todo not found")
    # Delete the todo from the database
    db.delete(db_todo)
    db.commit()
    return {"message": "Todo deleted successfully"}

# # 08 Endpoint to delete all todos from the database
# @app.delete("/todos/")
# def delete_all_todos(db: Session = Depends(get_db)):
#     try:
#         # Delete all todos from the database
#         db.query(database.Todo).delete()
#         db.commit()
#         return {"message": "All todos deleted successfully"}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))