# You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.

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

