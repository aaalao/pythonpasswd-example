import re
import string


def main():
    password = input("Enter Password:")
    passwd_check(password)


def passwd_check(passwd):
    specht = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if (any(x.isupper() for x in passwd) and any(x.islower() for x in passwd) and any(
            x.isdigit() for x in passwd) and any(specht.search(passwd) for x in passwd) and len(passwd) > 10):
        print("Password is accepted")

    else:
        if not (any(x.isupper() for x in passwd)):
            print('Entered Password must contain at least one capital case letters')
        if not (any(x.islower() for x in passwd)):
            print('Entered Password must contain at least one lower case letters')
        if not (any(x.isdigit() for x in passwd)):
            print('Entered Password must contain at least one numerical digit')
        if not (any(specht.search(passwd) for x in passwd)):
            print('Entered Password must contain at least one special character')
        if (len(passwd) < 11):
            print('Entered Password must contain more than 10 characters')


while (1):
    main()