from termcolor import colored
import pyfiglet
from footprint.utils.table import buildTable as table
from datetime import datetime
import os

def catchPrint(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except UnicodeEncodeError:
            printable = ["[", colored("UnicodeEncodeError", "blue"), "]", func.__name__, "=>"]
            for arg in args:
                printable.append(arg.encode("utf-8"))
            for kwarg in kwargs:
                printable.append(kwargs[kwarg].encode("utf-8"))
            print(printable)
    return wrapper

@catchPrint
def footPrint(*args, **kwargs):
    # get it??? footprint?? hahahaha
    print(*args, **kwargs)

def printVerify(email, verified, disposable):
    footPrint(f"Target Email:", colored(email, "red", "on_white"))
    if verified == True:
        footPrint("|-->", colored("Verified \u2714", "green"))
    else:
        footPrint("|-->", colored("Not Verified \u2718", "red"))
    if disposable == True:
        footPrint("|-->", colored("Disposable \u2718", "red"))
    else:
        footPrint("|-->", colored("Not Disposable \u2714", "green"))

def printSocial(social_result):
	footPrint("\nSocial Media Results:")
	for social in social_result:
		footPrint("|- " + social)

def printLookup(lookup_result):
    footPrint("\nLookup Results:")
    table(lookup_result)

def printPSB(psb_result):
    footPrint("\nPastebin Results:")
    if len(psb_result) == 0:
        footPrint("|-->", colored("No Results \u2718", "red"))
    else:
        for psb in psb_result:
            footPrint("|- " + psb)

def printHunter(hunter_result):
    footPrint("\nHunter Results:")
    try:
        footPrint("|- Disposable:", colored(hunter_result["data"]["disposable"], "yellow"))
        footPrint("|- Webmail:", colored(hunter_result["data"]["webmail"], "yellow"))
        footPrint("|- AcceptAll:", colored(hunter_result["data"]["accept_all"], "yellow"))    
        footPrint("|- Score:", colored(hunter_result["data"]["score"], "yellow"))
        footPrint("|- Result:", colored(hunter_result["data"]["result"], "yellow"))      
    except KeyError:
        footPrint("|- Error getting results, may be rate limited.")

def printBreachDirectory(breach_directory_result):
    footPrint("\nBreach Directory Results:")
    results = []
    try:
        if breach_directory_result != None:
            for breach in breach_directory_result["result"]:
                results.append("|- Sources:", colored("\u2714", "green"))
                for source in breach["sources"]:
                    results.append("|-- "+source, colored("\u2714", "green"))
                try:
                    results.append("|- Password: "+breach["password"], colored("\u2714", "green"))
                    results.append("|- Sha1: "+breach["sha1"], colored("\u2714", "green"))
                    results.append("|- Hash: "+breach["hash"], colored("\u2714", "green"))
                except KeyError:
                    pass
            results.append(colored(f"|- email found in {len(breach_directory_result['result'])} breaches", "red"))
        else:
            results.append(colored("|- No results found", "red"))
    except KeyError:
        footPrint(colored("|- Error getting results, may be rate limited.", "red"))
    if len(results) >= 50:
        path = os.path.abspath(f"./BreachDirectory({datetime.now().strftime('%m/%d/%Y_%H:%M:%S')}).txt")
        with open(path, "w", encoding="utf-8") as f:
            for result in results:
                f.write(result)
        f.close()
        footPrint(f"Too many results to display, saved result to: {path}.")
    else:
        for result in results:
            footPrint(result)

def printEmailRep(email_rep_result):
    footPrint("\nEmailRep Results:")
    try:
        footPrint("|- Reputation:", colored(email_rep_result["reputation"], "yellow"))
        footPrint("|- Blacklisted:", colored(email_rep_result["blacklisted"], "white"))
        footPrint("|- Malicious Activity:", colored(email_rep_result["details"]["malicious_activity"], "white"))
        footPrint("|- Credential Leaked:", colored(email_rep_result["details"]["credential_leaked"], "white"))
        footPrint("|- First Seen:", colored(email_rep_result["details"]["first_seen"], "yellow"))
        footPrint("|- Last Seen:",colored(email_rep_result["details"]["last_seen"], "yellow"))
        footPrint("|- Day Since Domain Creation:", colored(email_rep_result["details"]["days_since_domain_creation"], "white"))
        footPrint("|- Spam:", colored(email_rep_result["details"]["spam"], "white"))
        footPrint("|- Free Provider:", colored(email_rep_result["details"]["free_provider"], "white"))
        footPrint("|- Deliverable:", colored(email_rep_result["details"]["deliverable"], "white"))
        footPrint("|- Valid MX:", colored(email_rep_result["details"]["valid_mx"], "white"))
    except KeyError:
        footPrint(colored("|- Error getting results, may be rate limited.", "red"))

def printIPAPI(ipapi_result):
    footPrint("\nIPAPI Results:")
    try:
        footPrint("|- IP:", colored(ipapi_result["ip"], "yellow"))
        footPrint("|- City:", colored(ipapi_result["city"], "white"))
        footPrint("|- Postal Code:", colored(ipapi_result["postal"], "white"))
        footPrint("|- Region:", colored(ipapi_result["region"], "white"))
        footPrint("|- Country:", colored(ipapi_result["country"], "white"))
        footPrint("|- Country Code:", colored(ipapi_result["country_code"], "white"))
        footPrint("|- Timezone:", colored(ipapi_result["timezone"], "white"))
        footPrint("|- Organization:", colored(ipapi_result["org"], "white"))
        footPrint("|- ASN:", colored(ipapi_result["asn"], "white"))
    except KeyError:
        footPrint(colored("|- Error getting results, may be rate limited.", "red"))

def printInit(name, githublink, version):
    date = datetime.now().strftime("%A, %d %b %Y")
    name = pyfiglet.figlet_format(f"    {name}")
    footPrint(
    f"""{name}
        {version}
        {colored(githublink, "cyan")}
        Now: {date}
    """)

if __name__ == "__main__":
    printVerify("example@example.com", True, False)