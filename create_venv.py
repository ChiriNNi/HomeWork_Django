import os

def create_virtualenv(venv_name):
    os.system(f"python -m venv {venv_name}")
    print(f"Виртуальное окружение {venv_name} успешно создано.")

if __name__ == "__main__":
    project_name = input("Введите название проекта: ")
    create_virtualenv(project_name)