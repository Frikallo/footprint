from halo import Halo
import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from footprint.utils.emailVerif import validateEmail
from footprint.utils.social import checkSocials
from footprint.utils.lookup import Lookup
from footprint.utils.printFuncs import *
from footprint.utils.config import Config

def run():
    printInit("footprint", "https://github.com/Frikallo/footprint", "v1.0")

    config = Config('.conf')
    apis = ["hunter", "haveibeenpwned", "shodan", "virustotal", "ipinfo"]
    def setAPI(api, key):
        if api in apis:
            config.set(api, key)
            config.save()
            print(f"Set {api} key successfully")
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

    verified, disposable = validateEmail(email)
    socials = checkSocials(email)
    domainRecords = Lookup(email)
    spinner.stop()

    printVerify(email, verified, disposable)
    printSocial(socials)
    printLookup(domainRecords)

if __name__ == '__main__':
    run()