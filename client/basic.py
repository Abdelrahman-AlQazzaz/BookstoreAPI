import requests

endpoint = "http://127.0.0.1:8000/api/"

data=[{
    'title':'=asajfnkjsdngkjsndgbjsd',
    'author':"Wael Hallaq",
    'publisher':"Columbia Univeristy Press",
    'genre':'acedemic',
    'publication_date':"2012-11-20",
    'price':109.87,
    }]

def get_request(ep):
    response = requests.get(ep)
    print(response.text)

def post_request(ep, objs):
    for x in objs:
        response = requests.post(ep, json=x)
        print(response.text)

def put_request(ep, obj):
    response = requests.put(ep, json=obj)
    print(response.text)

def del_request(ep):
    response = requests.delete(ep)
    print(response.text)

put_request(endpoint+'4/', {'price':20000})