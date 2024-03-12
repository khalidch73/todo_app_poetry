

# @app.delete("/todos/{todo_id}")
# def delete_todo(todo_id: int, db: Session = Depends(get_db)):
#     db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
#     if db_todo is None:
#         raise HTTPException(status_code=404, detail="Todo not found")
#     db.delete(db_todo)
#     db.commit()
#     return {"message": "Todo deleted"}

# main.py

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
import database

app = FastAPI()

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

# Endpoint to main todo app
@app.get("/")
def main_todo_route():
    return {"message": "My Todo_App"}

# Endpoint to create a new todo
@app.post("/todos/")
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    # Create a new Todo instance from the input data
    db_todo = database.Todo(id=todo.id, title=todo.title, description=todo.description)
    # Add the new Todo to the database session
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo
# Endpoint to to update an existing todo or create a new todo if it does not already exist

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = db.query(database.Todo).filter(database.Todo.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    
#  @app.put("/todos/{todo_id}")
# def update_todo(todo_id: int, updated_todo: Todo, db: Session = Depends(get_db)):
#     db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
#     if db_todo is None:
#         raise HTTPException(status_code=404, detail="Todo not found")
#     for key, value in updated_todo.dict().items():
#         setattr(db_todo, key, value)
#     db.commit()
#     return db_todo