# streamlit_client.py

import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.title("Todo App")

def create_todo():
    id = st.number_input('Enter Todo Id')
    title = st.text_input("Enter Todo Title")
    description = st.text_area("Enter Todo Description")
    if st.button("Add Todo"):
        response = requests.post(f"{BASE_URL}/todos/", json={"id": id, "title": title, "description": description})
        if response.status_code == 200:
            st.success("Todo added successfully")

def update_todo():
    todo_id = st.number_input("Enter Todo ID to update")
    title = st.text_input("Enter Updated Todo Title")
    description = st.text_area("Enter Updated Todo Description")
    if st.button("Update Todo"):
        response = requests.put(f"{BASE_URL}/todos/{todo_id}", json={"id": todo_id, "title": title, "description": description})
        if response.status_code == 200:
            st.success("Todo updated successfully")

def delete_todo():
    todo_id = st.number_input("Enter Todo ID to delete")
    if st.button("Delete Todo"):
        response = requests.delete(f"{BASE_URL}/todos/{todo_id}")
        if response.status_code == 200:
            st.success("Todo deleted successfully")

def get_all_todos():
    # Function to get all todos
    response = requests.get(f"{BASE_URL}/alltodos/")
    if response.status_code == 200:
        todos = response.json()
        if todos:
            st.header("All Todos")
            todo_data = [{"ID": todo['id'], "Title": todo['title'], "Description": todo['description']} for todo in todos]
            st.table(todo_data)
        else:
            st.info("No todos found")

if __name__ == "__main__":
    get_all_todos()
    create_todo()
    update_todo()
    delete_todo()
    