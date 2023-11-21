import requests
def getResponse():
    url = "https://jsonplaceholder.typicode.com/todos/"
    response = requests.get(url)
    data = response.json()
    return data

content = getResponse()
print(content[1])
for item in content:
    print(item['title'])