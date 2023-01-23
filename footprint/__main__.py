from halo import Halo
import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from footprint.utils.emailVerif import validateEmail
from footprint.utils.social import checkSocials
from footprint.utils.lookup import Lookup
from footprint.utils.printFuncs import *
from footprint.utils.config import Config
from footprint.utils.apis import *

def run():
    printInit("footprint", "https://github.com/Frikallo/footprint", "v1.2")

    config = Config('.conf')
    apis = ["hunter", "breachdirectory", "emailrep"]
    def setAPI(api, key):
        if api in apis:
            config.set(api, key)
            config.save()
            print( "[" + colored("INFO","blue") + "]" + f" Set {api} key successfully")
            exit(0)
        else:
            print(f"\"{api}\" is not an accepted API")
            exit(0)

    args = sys.argv[1:]
    if "set" in args:
        api = args[args.index("set") + 1]
        key = args[args.index("set") + 2]
        setAPI(api, key)
    else:
        try:
            email = args[0]
        except IndexError:
            print("Usage: footprint <email> OR footprint [options]")
            print("Options:")
            print("set <api> <key> - Set API key for a specific API")
            exit(0)

    spinner = Halo(spinner='dots', color='white')
    spinner.start()

    configured_apis = available_apis(apis, config)
    verified, disposable = validateEmail(email)
    socials = checkSocials(email)
    domainRecords = Lookup(email)
    iapi = ipapi(email)
    psbDump = psbDumps(email)
    apiResults = {}
    for configured_api in configured_apis:
        if configured_api == "emailrep":
            apiResults["emailrep"] = emailRep(email, config.get("emailrep"))
        elif configured_api == "hunter":
            apiResults["hunter"] = hunter(email, config.get("hunter"))
        elif configured_api == "breachdirectory":
            apiResults["breachdirectory"] = BreachDirectory(email, config.get("breachdirectory"))
    spinner.stop()

    printVerify(email, verified, disposable)
    printSocial(socials)
    if "emailrep" in configured_apis:
        printEmailRep(apiResults["emailrep"])
    if "hunter" in configured_apis:
        printHunter(apiResults["hunter"])
    if "breachdirectory" in configured_apis:
        printBreachDirectory(apiResults["breachdirectory"])
    printPSB(psbDump)
    printIPAPI(iapi)
    printLookup(domainRecords)

if __name__ == '__main__':
    run()