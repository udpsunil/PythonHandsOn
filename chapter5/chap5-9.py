# Hello Admin
usernames = []
if usernames == []:
    print("We need some users")

usernames = ['admin', 'root', 'sunil', 'linus', 'sunilu']

username = 'admin'

if usernames == []:
    print("We need some users")

if username in usernames:
    print("Hello "+username+", would you like a status report?")
else:
    print("Thank you for logging in "+username)