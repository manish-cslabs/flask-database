import requests
BASE = 'http://localhost:5000/'

# response= requests.get(BASE + 'hello')
response= requests.get(BASE + 'hello/manish/25')
print(response.json())

responsePost= requests.post(BASE + 'hello/manish/25')
print(responsePost.json())


