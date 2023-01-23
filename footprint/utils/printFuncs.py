from termcolor import colored
import pyfiglet
from footprint.utils.table import buildTable as table
from datetime import datetime

def printVerify(email, verified, disposable):
    print(f"Target Email:", colored(email, "red", "on_white"))
    if verified == True:
        print("|-->", colored("Verified \u2714", "green"))
    else:
        print("|-->", colored("Not Verified \u2718", "red"))
    if disposable == True:
        print("|-->", colored("Disposable \u2718", "red"))
    else:
        print("|-->", colored("Not Disposable \u2714", "green"))

def printSocial(social_result):
	print("\nSocial Media Results:")
	for social in social_result:
		print("|- " + social)

def printLookup(lookup_result):
    print("\nLookup Results:")
    table(lookup_result)

def printPSB(psb_result):
    print("\nPastebin Results:")
    if len(psb_result) == 0:
        print("|-->", colored("No Results \u2718", "red"))
    else:
        for psb in psb_result:
            print("|- " + psb)

def printHunter(hunter_result):
    print("\nHunter Results:")
    try:
        print("|- Disposable:", colored(hunter_result["data"]["disposable"], "yellow"))
        print("|- Webmail:", colored(hunter_result["data"]["webmail"], "yellow"))
        print("|- AcceptAll:", colored(hunter_result["data"]["accept_all"], "yellow"))    
        print("|- Score:", colored(hunter_result["data"]["score"], "yellow"))
        print("|- Result:", colored(hunter_result["data"]["result"], "yellow"))      
    except KeyError:
        print("|- Error getting results, may be rate limited.")

def printBreachDirectory(breach_directory_result):
    print("\nBreach Directory Results:")
    try:
        if breach_directory_result != None:
            for breach in breach_directory_result["result"]:
                print("|- Sources:", colored("\u2714", "green"))
                for source in breach["sources"]:
                    print("|-- "+source, colored("\u2714", "green"))
                try:
                    print("|- Password: "+breach["password"], colored("\u2714", "green"))
                    print("|- Sha1: "+breach["sha1"], colored("\u2714", "green"))
                    print("|- Hash: "+breach["hash"], colored("\u2714", "green"))
                except KeyError:
                    pass
            print(colored(f"|- email found in {len(breach_directory_result['result'])} breaches", "red"))
        else:
            print(colored("|- No results found", "red"))
    except KeyError:
        print(colored("|- Error getting results, may be rate limited.", "red"))

def printEmailRep(email_rep_result):
    print("\nEmailRep Results:")
    try:
        print("|- Reputation:", colored(email_rep_result["reputation"], "yellow"))
        print("|- Blacklisted:", colored(email_rep_result["blacklisted"], "white"))
        print("|- Malicious Activity:", colored(email_rep_result["details"]["malicious_activity"], "white"))
        print("|- Credential Leaked:", colored(email_rep_result["details"]["credential_leaked"], "white"))
        print("|- First Seen:", colored(email_rep_result["details"]["first_seen"], "yellow"))
        print("|- Last Seen:",colored(email_rep_result["details"]["last_seen"], "yellow"))
        print("|- Day Since Domain Creation:", colored(email_rep_result["details"]["days_since_domain_creation"], "white"))
        print("|- Spam:", colored(email_rep_result["details"]["spam"], "white"))
        print("|- Free Provider:", colored(email_rep_result["details"]["free_provider"], "white"))
        print("|- Deliverable:", colored(email_rep_result["details"]["deliverable"], "white"))
        print("|- Valid MX:", colored(email_rep_result["details"]["valid_mx"], "white"))
    except KeyError:
        print(colored("|- Error getting results, may be rate limited.", "red"))

def printInit(name, githublink, version):
    date = datetime.now().strftime("%A, %d %b %Y")
    name = pyfiglet.figlet_format(f"    {name}")
    print(
    f"""{name}
        {version}
        {colored(githublink, "cyan")}
        Now: {date}
    """)