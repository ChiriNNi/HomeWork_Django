import os

def run_project(project_name):
    os.chdir(project_name)
    os.system("python manage.py runserver")

if __name__ == "__main__":
    project_name = input("Введите название проекта: ")
    run_project(project_name)