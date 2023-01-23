import requests
import json
import socket

def available_apis(apis, config):
    available_apis = []
    for api in apis:
        try:
            config.get(api)
        except KeyError:
            pass
        else:
            available_apis.append(api)
    return available_apis

def psbDumps(email):
    r = requests.Session()
    url = "https://psbdmp.ws/api/search/" + email
    r.headers = {"Accept", "application/json"}
    req = r.get(url)
    content = req.content
    response = json.loads(content)
    rets = []
    for line in response["data"]:
        rets.append("https://psbdmp.ws/dump/"+line['id'])
    return rets

def emailRep(email, key):
    r = requests.Session()
    url = "https://emailrep.io/query/" + email
    r.headers = {"Accept", "application/json"}
    r.headers = {"Key", key}
    req = r.get(url)
    content = req.content
    response = json.loads(content)
    return response

def hunter(email, key):
    r = requests.Session()
    url = "https://api.hunter.io/v2/email-verifier?email=" + email + "&api_key=" + key
    r.headers = {"Accept", "application/json"}
    req = r.get(url)
    content = req.content
    response = json.loads(content)
    return response

def BreachDirectory(email, key):
    r = requests.Session()
    url = "https://breachdirectory.p.rapidapi.com/"

    querystring = {"func":"auto","term":email}
    headers = {
        "X-RapidAPI-Key": key,
        "X-RapidAPI-Host": "breachdirectory.p.rapidapi.com"
    }

    req = r.get(url, headers=headers, params=querystring)
    content = req.content
    response = json.loads(content)
    return response

def ipapi(email):
    r = requests.Session()
    splt = email.split('@')[1]
    try:
        ip = socket.gethostbyname(splt)
    except:
        return "No IP found"
    url = "https://ipapi.co/" + ip + "/json/"
    r.headers = {"Accept", "application/json"}
    req = r.get(url)
    content = req.content
    response = json.loads(content)
    return response