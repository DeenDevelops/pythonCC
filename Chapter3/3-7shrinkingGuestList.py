# You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

people = ['Johnny Knoxville', 'Satoshi Tajiri', 'Shigeru Miyamoto']
message = ",you are formally invited to a dinner of the highest quality at Ruby Tuesdays."

print(people[0] + message)
print(people[1] + message)
print(people[2] + message)

noShow = people.pop(1)
newPerson = people.insert(1, 'Steve-O')

print("\nSadly, " + noShow + ", could not make it.")

print(people[0] + message)
print(people[1] + message)
print(people[2] + message)

people.insert(0, 'Tony')
people.insert(1, 'Tammy')
people.append('Timmy')

print("\nSome of my personal friends wanted to come to dinner. I have reserved a bigger table.\n")

print(people[0] + message)
print(people[1] + message)
print(people[2] + message)
print(people[3] + message)
print(people[4] + message)
print(people[5] + message)

print('\nSadly, there has been a change in logistics. Only 2 people can come to dinner.')
sorryMessage = 'Sorry: '

goodbye1 = people.pop(5)
goodbye2 = people.pop(4)
goodbye3 = people.pop(3)
goodbye4 = people.pop(2)

print(sorryMessage + goodbye1)
print(sorryMessage + goodbye2)
print(sorryMessage + goodbye3)
print(sorryMessage + goodbye4)

print(f"You're still invited: {people[0]}, {people[1]}")

del people[1]
del people[0]

print(people)