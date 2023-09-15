current_users = ['pam', 'jim', 'michael', 'oscar', 'angela']
new_users = ['pam', 'jim', 'dwight', 'ryan', 'roy']

for user in new_users:
    if user in current_users:
        print(f"{user} is not available.")
    