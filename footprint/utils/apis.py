from footprint.utils.config import Config
import requests
import json
import random
import pkg_resources

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

if __name__ == "__main__":
    apis = ["hunter", "haveibeenpwned", "shodan", "virustotal", "ipinfo"]
    #config = Config('.conf')
    #print(available_apis(apis, config))
    #print(psbDumps("noahskay@icloud.com"))
    #print(emailRep("noahskay@icloud.com"))
    #print(hunter("f.last@noah.co.uk", "aa2fd4604b9d42177a1a74b13b25eff96a23eab6"))
    #BreachDirectory("HI@GMAIL.COM", "6aaf3bd13amsh7eef51a55c30763p12db3ajsn9cbfd61e6ed0")