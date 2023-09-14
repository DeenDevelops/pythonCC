pizzas = ['pepperoni', 'sausage', 'cheese']
pizzas.append('mushroom')

friend_pizzas = pizzas[:]
friend_pizzas.append('pineapple')

for pizza in pizzas:
    print("I like " + pizza + " pizza.")

print('\n')

for friend_pizza in friend_pizzas:
    print("My friend likes " + friend_pizza + " pizza.")


print("There are so many good pizzas!") 