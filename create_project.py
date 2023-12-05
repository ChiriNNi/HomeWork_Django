import os

def create_django_project(project_name):
    os.system(f"django-admin startproject {project_name}")
    print(f"Проект {project_name} успешно создан.")

if __name__ == '__main__':
    project_name = input("Введите название проекта: ")
    create_django_project(project_name)