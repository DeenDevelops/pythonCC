usernames = ['jim', 'jon', 'tim', 'tom', 'jayden', 'admin']
usernames1 = ['admin']

for user in usernames:
    if user in usernames1:
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in today.")

