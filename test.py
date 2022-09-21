import requests
BASE = 'http://localhost:5000/'

# response= requests.get(BASE + 'hello')
# response= requests.get(BASE + 'hello/manish/25')
# print(response.json())

# responsePost= requests.post(BASE + 'hello/manish/25')
# print(responsePost.json())

videoData = [{"name": "how to manish", "views": 33000, "likes": 10},
             {"name": "manish", "views": 1231000, "likes": 123456},
             {"name": "bnhartyu", "views": 1000, "likes": 0}]

for i in range(0, len(videoData)):
    response = requests.put(BASE + "/video/" + str(i), videoData[i])
    print(response.json())

response = requests.delete(BASE + "/video/0")

# responseVideo = requests.put(
#     BASE + 'video/1', {"name": "manish", "views": 1000, "likes": 10})
# print(responseVideo.json())
input()
responseVideo = requests.get(BASE + 'video/2')
print(responseVideo.json())
