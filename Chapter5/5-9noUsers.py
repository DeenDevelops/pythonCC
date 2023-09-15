usernames = []
usernames1 = []

for user in usernames:
    if user in usernames1:
        print("Hello admin, would you like to see a status report?")
    elif user in usernames:
        print(f"Hello {user}, thank you for logging in today.")
else:
    print("We need to find some users!")
