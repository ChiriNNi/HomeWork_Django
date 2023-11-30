from django.shortcuts import render
import requests


def getResponse(request):
    url = "https://jsonplaceholder.typicode.com/todos/"
    response = requests.get(url)
    data = response.json()
    context = {'data': data}
    return render(request, 'index.html', context)


def objectInfo(request, param):
    url = "https://jsonplaceholder.typicode.com/todos/"
    response = requests.get(url)
    data = response.json()
    object = None
    for item in data:
        if item.get('id') == param:
            object = item
    return render(request, 'objectInfo.html', {'object': object})


def login_page(request):
    return render(request, 'login.html')


def about_page(request):
    return render(request, 'about.html')


def contacts_page(request):
    return render(request, 'contacts.html')