import requests 
import json

def cat():
    url = 'https://catfact.ninja/fact'
    rr = requests.get(url)
    print(rr)
    return cat 

def bit():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    rr = requests.get(url)
    rq = rr.json()
    print(rq)
    return bit

def bored():
    url = 'https://www.boredapi.com/api/activity'
    rr = requests.get(url)
    print(rr)
    return bored

def age():
    age1 = input("Enter your age: ")
    url = 'https://api.agify.io?name={age1}'
    rr = requests.get(url)
    print(rr)
    return age

def gender():
    gender1 = input("Enter your gender: ")
    url = 'https://api.genderize.io/?name={gender1}'
    rr = requests.get(url)
    print(rr)
    return gender

def nation():
    nat = input("Enter your name (I will tell your nationality): ")
    url = 'https://api.genderize.io/?name={gen}'
    rr = requests.get(url)
    print(rr)
    return nation

def location():
    url = 'https://api.ipify.org/?format=json'
    res = requests.get(url)
    rr = res.json()
    print(rr)
    return location

def ip():
    loc = int(input("Enter your ip address: "))
    url = 'https://ipinfo.io/{loc}/geo'
    res = requests.get(url)
    rr = res.json()
    print(rr)
    return ip

def rand():
    url = 'https://randomuser.me/api/'
    rr = requests.get(url)
    res = rr.json
    print(res)
    return rand

print("press 1 for cat facts\npress 2 for bitcoin price\npress 3 for activity\npress 4 for age finder\npress 5 for gender finder\npress 6 for nationality finder\npress 7 for your ip\npress 8 for ip info ( ip is input\npress 9 for random user info gen)")
choice = input("Enter your number of the process: ")
if choice =='1':
    cat()
elif choice =='2':
    bit()
elif choice =='3':
    bored()
elif choice =='4':
    age()
elif choice =='5':
    gender()
elif choice =='6':
    nation()
elif choice =='7':
    location()
elif choice =='8':
    ip()
elif choice =='9':
    rand()
else:
    print("run again , wrong process")



