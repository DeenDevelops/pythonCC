sandwich_orders = ['ham', 'cheese', 'turkey']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f'Making your {current_sandwich} sandwich.')
    finished_sandwiches.append(current_sandwich)


print("")
for sandwich in finished_sandwiches:
    print(f"Your {sandwich} sandwich is ready.")