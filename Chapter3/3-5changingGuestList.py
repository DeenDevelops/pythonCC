#You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

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


