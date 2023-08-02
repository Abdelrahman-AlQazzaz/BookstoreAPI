import requests
import json

endpoint = "http://127.0.0.1:8000/api/"

token = json.loads(open('token.txt', 'r').read())['access']

header = {'Authorization': f'Bearer {token}',}

def get_request(ep):
    response = requests.get(ep)
    print(response.text)

def post_request(ep, objs):
    for x in objs:
        response = requests.post(ep, json=x, headers=header)
        print(response.text)

def put_request(id, obj):
    response = requests.put(endpoint+str(id)+'/', json=obj, headers=header)
    print(response.text)

def del_request(id):
    response = requests.delete(endpoint+str(id)+'/', headers=header)
    print(response.text)

def obtain_token():
    response = requests.post(endpoint+"token/", json={'username': 'aq',
        'password': '!Qazzaz!',})
    file = open('token.txt', 'w')
    file.write(response.text)
    file.close()
    print(response.text)

data=[{
    'title':'1984',
    'author':"George Orwell",
    'publisher':"Secker and Warburg",
    'genre':'politcal satire',
    'publication_date':"1949-06-08",
    'price':20.09,
    }]

post_request(endpoint, data)
