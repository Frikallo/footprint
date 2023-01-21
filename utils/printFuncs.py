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

def printInit(name, githublink, version):
    date = datetime.now().strftime("%A, %d %b %Y")
    name = pyfiglet.figlet_format(f"    {name}")
    print(
    f"""{name}
        {version}
        {colored(githublink, "cyan")}
        Now: {date}
    """
    )