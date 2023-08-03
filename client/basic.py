import requests
import json

endpoint = "http://127.0.0.1:8000/api/"

key = json.loads(open('key.txt', 'r').read())['key']

header = {'Authorization': f'Token {key}'}

def get_request(ep):
    response = requests.get(ep)
    print(response.text)

def post_request(ep,objs):
    for x in objs:
        response = requests.post(ep, json=x, headers=header)
        print(response.text)

def put_request(id, obj):
    response = requests.put(endpoint+str(id)+'/', json=obj, headers=header)
    print(response.text)

def del_request(id):
    response = requests.delete(endpoint+str(id)+'/', headers=header)
    print(response.text)

def login_request():
    response = requests.post('http://127.0.0.1:8000/dj-rest-auth/login/', json={'username': 'aq',
        'password': '!Qazzaz!',})
    file = open('key.txt', 'w')
    file.write(response.text)
    file.close()
    print(response.text)

def filter_request(param, query):
    get_request(endpoint+"filter/"+str(param)+'/'+str(query)+'/')

data=[{
    'id':1,
    'title':'Nineteen Eighty-Four',
    'author':"George Orwell",
    'publisher':"Secker and Warburg",
    'genre':'politcal satire',
    'publication_date':"1949-06-08",
    'price':2,
    }]

