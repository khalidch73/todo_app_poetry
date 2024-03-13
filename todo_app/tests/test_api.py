import requests
import pytest

# # Test 1: Check the status code of the main route
# def test_status_code_main_route():
#     response = requests.get('http://127.0.0.1:8000')
#     assert response.status_code == 200

# # Test 2: Check the status code of the todos route after creating a new todo
# def test_status_code_todos():
#     response = requests.post('http://127.0.0.1:8000/todos/', json={
#         "id": 6,
#         "title": "Todo06",
#         "description": "add todo06 in my database."
#     })
#     assert response.status_code == 200

# # Test 3: Check the status code of updating a specific todo by ID
# def test_status_code_todos_ids():
#     # Replace {todo_id} with the actual ID you want to test
#     todo_id = 2
#     response = requests.put(f'http://127.0.0.1:8000/todos/{todo_id}', json={
#         "id": 2,
#         "title": "update todo",
#         "description": "Updated Description"
#     })
#     assert response.status_code == 200

# Test 4: Delete a todo that already exists in the database
# def test_delete_existing_todo():
#     # Create a new todo to ensure it exists in the database
#     response = requests.post('http://127.0.0.1:8000/todos/', json={
#         "id": 7,
#         "title": "Existing Todo",
#         "description": "This is an existing todo in the database"
#     })
#     assert response.status_code == 200

#     # Get the ID of the created todo
#     todo_id = response.json()["id"]

#     # Delete the todo by ID
#     response = requests.delete(f'http://127.0.0.1:8000/todos/{todo_id}')
#     assert response.status_code == 200


# # Test 5: Check the status code of retrieving a todo by its ID
# def test_get_todo_by_id():
#     # Create a new todo to retrieve later
#     response = requests.post('http://127.0.0.1:8000/todos/', json={
#         "id": 10,
#         "title": "Test Todo",
#         "description": "Test todo description"
#     })
#     assert response.status_code == 200

#     # Retrieve the todo by its ID
#     response = requests.get('http://127.0.0.1:8000/todos/10')
#     assert response.status_code == 200

#     # Check if the retrieved todo has the correct data
#     todo = response.json()
#     assert todo["id"] == 10
#     assert todo["title"] == "Test Todo"
#     assert todo["description"] == "Test todo description"


# Test 06: Check the status code and content of getting all todos
# def test_get_all_todos():
#     # Make a GET request to retrieve all todos
#     response = requests.get('http://127.0.0.1:8000/alltodos/')
    
#     # Check if the status code is 200 (OK)
#     assert response.status_code == 200
    
#     # Check if the response contains JSON data
#     assert response.headers['Content-Type'] == 'application/json'
    
#     # Check if the response contains a list of todos
#     assert isinstance(response.json(), list)
    
    # Optionally, you can check the content of the response further
    # For example, you can check if the response contains expected todos
    # assert len(response.json()) > 0  # Ensure there are todos returned

# Test 07: Check the status code of deleting all todos from the database
def test_delete_all_todos():
    # Send a DELETE request to the endpoint
    response = requests.delete('http://127.0.0.1:8000/todos/')
    
    # Assert the status code is 200
    assert response.status_code == 200