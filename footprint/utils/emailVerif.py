from email_validator import validate_email, EmailNotValidError
import pkg_resources
import re


def validateEmail(email, is_new_account=False, blocklistPath='/data/emails.blocklist'):
    regex = re.compile(r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$")
    if not regex.findall(email):
        print("Invalid email address!")
        exit(0)
    try:
        validation = validate_email(email, check_deliverability=is_new_account, dns_resolver=True)
        email = validation.email
        verified = True
    except EmailNotValidError as e:
        print(str(e))
        verified = False
    stream = pkg_resources.resource_stream(__name__, blocklistPath)
    blocklist = stream.read().decode('utf-8').split('\n')
    blocklist_content = [line.rstrip() for line in blocklist]
    if email.split('@')[1] in blocklist_content:
        disposable = True
    else:
        disposable = False
    return verified, disposable


if __name__ == "__main__":
    email = "example@example.com"
    print(validateEmail(email))