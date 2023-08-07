import requests
import json

endpoint = "http://127.0.0.1:8000/api/"

key = json.loads(open("key.txt", "r").read())["key"]

header = {"Authorization": f"Token {key}"}

def get_request(ep):
    response = requests.get(endpoint+ep)
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
    response = requests.post("http://127.0.0.1:8000/dj-rest-auth/login/", json={"username": "aq",
        "password": "!Qazzaz!",})
    file = open("key.txt", "w")
    file.write(response.text)
    file.close()
    print(response.text)

def filter_request(model, param, query):
    new_ep = endpoint+model+"/filter/"+str(param)+"/"+str(query)+"/"
    response = requests.get(new_ep, headers=header)
    print(response.text)

data=[{
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
        "title":"Harry Potter & The Philospher's Stone",
        "author":["J. K. Rowling"],
        "genre":['fiction'],
        'publisher':['Bloomsbury'],
        'publication_date':'1997-06-26',
    },
    {
        "title":"Debt: The First 5,000 Years",
        "author":["David Graeber"],
        "genre":['historical','economics'],
        'publisher':['Melville House'],
        'publication_date':'2011-01-01',
    },
    {
        "title":"The Impossible State",
        "author":["Wael Hallaq"],
        "genre":['acedemic'],
        'publisher':['Columbia University Press'],
        'publication_date':'2014-09-01',
        'price':32.00,
    },]

post_request('books/', data)