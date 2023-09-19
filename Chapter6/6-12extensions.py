# Store information about a pizza being ordered.
pizza = {
    'crust': ['thick', 'thin', 'pan'],
    'sauce': ['tomato', 'barbeque', 'ranch'],
    'toppings': ['mushrooms', 'extra cheese', 'pepperoni'],
}


# I'm going to make a few different pizza variations

for k, v in pizza.items():
    for item in v:
        if k == 'crust' and item == 'thin':
            print(f"I want my pizza to have {item} {k}.")
        elif k == 'sauce' and item == 'tomato':
            print(f"I want my pizza to have {item} {k}")
        elif k == 'toppings' and item == 'mushrooms':
            print(f"I want my pizza to have {item} {k}")