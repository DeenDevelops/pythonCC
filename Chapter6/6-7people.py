personThings = {
    'first name': 'john',
    'last name': 'smith',
    'age': '22',
    'city': 'boston',
}

personThings2 = {
    'first name': 'toddy',
    'last name': 'smith',
    'age': '25',
    'city': 'memphis'
}

personThings3 = {
    'first name': 'jim',
    'last name': 'halpert',
    'age': '28',
    'city': 'scranton' 
}

allPersonThings = [personThings, personThings2, personThings3]

for person in allPersonThings:
    for key, value in person.items():
        print(f"{key.title()}: {value.title()}")
