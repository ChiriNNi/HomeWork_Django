import os

def freeze_requirements():
    os.system("pip freeze > requirements.txt")
    print("Зависимости заморожены в файле requirements.txt.")

if __name__ == "__main__":
    project_name = input("Введите название проекта: ")
    freeze_requirements(project_name)