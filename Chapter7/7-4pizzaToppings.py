prompt = "\nEnter a pizza topping."
prompt += "\n(Type 'quit' to exit.)\n"

active = True

while active:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"Adding {topping} to pizza.")
