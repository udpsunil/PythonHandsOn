# Checking Usernames

current_users = ['root', 'admin', 'administrator', 'sunil', 'udupi']
new_users = ['sunil', 'UDUPI', 'eid1', 'eid2']

for user in new_users:
    if user.lower() in [u.lower() for u in current_users]:
        print(user+" needs to enter a new username.")
    else:
        print("your requested username "+user+" is available.")