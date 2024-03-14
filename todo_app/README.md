poetry run uvicorn todo_app.main:app --host 127.0.0.1 --port 8000
poetry run streamlit run streamlit_client.py
poetry run python python_console_client.py
ngrok config add-authtoken 2bcMHj2f8zjhvmTpNYPUSg4blOw_5aTbSSrJ2GsEDGWjEcm1d
