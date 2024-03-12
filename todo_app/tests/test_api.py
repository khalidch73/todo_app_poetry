# test_api.py
import requests
# test 1
response1 = requests.get('http://127.0.0.1:8000')
def test_status_code_main_route ():
    assert response1.status_code == 200
# test 2
response2 = requests.post('http://127.0.0.1:8000/todos/', json= {
  "id": 1,
  "title": "Test todo",
  "description": "add my test todo"
})
def test_status_code_todos ():
    assert response2.status_code == 200
    # assert response2.json()["message"] == "Test Todo"
# test 3
response3 = requests.put('http://127.0.0.1:8000/todos/{todo_id}', json= {
  "id": 3,
  "title": "update todo",
  "description": "Updated Description"
})
def test_status_code_todos_ids ():
    assert response3.status_code == 200
    # assert response2.json()["message"] == "Todo updated"
# def test_update_todo():
#     response = client.put("/todos/1", json={"title": "Updated Todo", "description": "Updated Description"})
#     assert response.status_code == 200
#     assert response.json()["title"] == "Updated Todo"

# def test_delete_todo():
#     response = client.delete("/todos/1")
#     assert response.status_code == 200
#     assert response.json()["message"] == "Todo deleted"