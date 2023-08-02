import requests

endpoint = "http://127.0.0.1:8000/api/"

data=[
    {
    'title':'Impossible State',
    'author':"Wael Hallaq",
    'publisher':"Columbia Univeristy Press",
    'genre':'acedemic',
    'publication_date':"2012-11-20",
    'price':109.87,
    },{
    'title':'Blink',
    'author':"Malcolm Gladwell",
    'publisher':"Bay Back Books",
    'genre':'self-development',
    'publication_date':"2005-01-11",
    'price':36.9,
    },{
    'title':'Gulliver`s Travels',
    'author':"Jonathan Swift",
    'publisher':"Benjamin Motte",
    'genre':'political satire',
    'publication_date':"1726-10-28",
    'price':19.87,
    }]

def get_Request(ep):
    response = requests.get(ep)
    print(response.text)

def post_Request(ep, objs):
    for x in objs:
        response = requests.post(ep, json=x)
        print(response.text)


