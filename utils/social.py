import requests
import json
import re

def twitter(email):
    r = requests.Session()
    url = "https://api.twitter.com/i/users/email_available.json?email=" + email
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
    Host = "api.twitter.com"
    Accept = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    r.headers = {'User-Agent': user_agent}
    r.headers = {'Host': Host}
    r.headers = {'Accept': Accept}
    req = r.get(url)
    text = str(req.json())
    if req.status_code == 200:
        if text.find("'valid': False") == True:
            return "Twitter \U0001f440"
        else:
            return "Twitter [Not here!]"
    else:
        return "Twitter [Couldn't check!]"

def instagram(email):
    r = requests.Session()
    url = "https://www.instagram.com/accounts/account_recovery_send_ajax/"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
    r.headers = {'user-agent': user_agent}
    r.headers.update({'X-CSRFToken': "missing"})
    data = {"email_or_username":email}
    req = r.post(url,data=data)
    if req.status_code == 200:
        if req.text.find("We sent an self.email to")>=0:
            return "Instagram \U0001f440"
        elif req.text.find("password")>=0:
            return "Instagram \U0001f440"
        elif req.text.find("sent")>=0:
            return "Instagram \U0001f440"
        else:
            return "Instagram [Not here!]"
    else:
        return "Instagram [Couldn't check!]"

def spotify(email):
    r = requests.Session()
    url = "https://spclient.wg.spotify.com/signup/public/v1/account"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
    r.headers = {"User-Agent": user_agent}
    r.headers = {"Content-Type", "application/x-www-form-urlencoded"}
    data = {"validate":"1", "email":email}
    req = r.post(url,data=data)
    status = req.json()["status"]
    if req.status_code == 200:
        if status == 20:
            return "Spotify \U0001f440"
        else:
            return "Spotify [Not here!]"
    else:
        return "Spotify [Couldn't check!]"

def discord(email):
    r = requests.Session()
    url = "https://discord.com/api/v9/auth/register"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
    jsonStr = json.dumps({"email":f"{email}","username":"asdsadsad","password":"q1e31e12r13*","invite":None,"consent":True,"date_of_birth":"1973-05-09","gift_code_sku_id":None,"captcha_key":None,"promotional_email_opt_in":False})
    r.headers = {"Content-Type", "application/json"}
    r.headers = {"User-Agent": user_agent}
    r.headers = {"X-Debug-Options", "bugReporterEnabled"}
    req = r.post(url, jsonStr)
    if req.status_code == 400:
        if len(req.json()["errors"]["email"]["_errors"]) > 0:
            if req.json()["errors"]["email"]["_errors"][0]["code"] == "EMAIL_ALREADY_REGISTERED":
                return "Discord \U0001f440"
            else:
                return "Discord [Not here!]"
        else:
            return "Discord [Not here!]"
    elif req.status_code == 429:
        return "Discord [Rate limited!]"
    else:
        return "Discord [Couldn't check!]"

def github(email):
    r = requests.Session()
    url = "https://github.com/signup_check/email"
    prereq = r.get("https://github.com/join")
    text = prereq.text
    token_regex = re.compile(
        r'<auto-check src="/signup_check/username[\s\S]*?value="([\S]+)"[\s\S]*<auto-check src="/signup_check/email[\s\S]*?value="([\S]+)"'
    )
    token = token_regex.search(text)
    if token:
        email_token = token.group(2)
    else: 
        return "Github [Couldn't check!]"
    req = r.post(url, data={"value": email, "authenticity_token": email_token})
    if req.status_code == 200:
        return "Github \U0001f440"
    elif req.status_code == 429:
        return "Github [Rate Limited!]"
    elif req.status_code == 422:
        if req.text == "Email is invalid or already taken":
            return "Github \U0001f440"
        return "Github [Not here!]"
    else:
        return "Github [Couldn't check!]"
        
def checkSocials(email):
    rets = []
    socials = [twitter, instagram, spotify, discord, github]
    for social in socials:
        try:
            rets.append(social(email))
        except:
            rets.append(f"{social.__name__} [Error!]")
    return rets

if __name__ == "__main__":
    email = "example@example.com"
    print(checkSocials(email))