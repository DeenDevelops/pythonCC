my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nProving that these are two separate lists:")

for food in my_foods:
    print(my_foods)

print("\n")
for friend_food in friend_foods:
    print(friend_foods)
