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


