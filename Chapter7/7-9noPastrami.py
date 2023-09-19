sandwich_order = ['ham', 'cheese', 'pastrami','pastrami', 'turkey', 'pastrami']
finished_sandwiches = []

print("Mamma mia! We have run out of pastrami!")

while 'pastrami' in sandwich_order:
    sandwich_order.remove('pastrami')

while sandwich_order:
    current_sandwich = sandwich_order.pop()
    print(f"Making {current_sandwich} sandwich.")

    finished_sandwiches.append(current_sandwich)
    print(f"Finished making {current_sandwich} sandwich.\n")

print(finished_sandwiches)