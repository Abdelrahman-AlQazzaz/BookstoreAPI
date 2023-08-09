import requests
import json

endpoint = "http://127.0.0.1:8000/api/"

key = json.loads(open("key.txt", "r").read())["access"]

header = {"Authorization": f"Bearer {key}"}

def get_request(ep):
    response = requests.get(endpoint+ep, headers=header)
    print(response.text)

def post_request(ep, objs):
    for x in objs:
        response = requests.post(endpoint+ep, json=x, headers=header)
        print(response.text)

def put_request(ep, obj):
    response = requests.put(endpoint+ep, json=obj, headers=header)
    print(response.text)

def del_request(ep):
    response = requests.delete(endpoint+ep, headers=header)
    print(response.text)

def login_request():
    global header
    response = requests.post("http://127.0.0.1:8000/dj-rest-auth/login/", json={"username": "aq","password": "!Qazzaz!",})
    file = open("key.txt", "w")
    file.write(response.text)
    file.close()
    print(response.text)
    key = json.loads(open("key.txt", "r").read())["access"]

    header = {"Authorization": f"Bearer {key}"}

def filter_request(model, param, query):
    new_ep = endpoint+model+"/filter/"+str(param)+"/"+str(query)+"/"
    response = requests.get(new_ep, headers=header)
    print(response.text)

data=[
      {
        "title":"Animal Farm",
        "author":["George Orwell"],
        "genre":['political-satire'],
        'publisher':['Secker & Warburg'],
        'publication_date':'1945-08-27',
        'price':20.34
    },
    {
        "title":"Gulliver's Travels",
        "author":["Jonathan Swift"],
        "genre":['political-satire'],
        'publisher':['Benjamin Motte'],
        'publication_date':'1726-10-28',
    },
    {
        "title":"The Impossible State",
        "author":["Wael Hallaq"],
        "genre":['acedemic'],
        'publisher':['Columbia University Press'],
        'publication_date':'2014-09-01',
        'price':32.00,
    },]

get_request('books/filter/?title=Animal Farm/')