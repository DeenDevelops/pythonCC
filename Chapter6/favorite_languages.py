favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, lanugage in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {lanugage.title()}.")

print("")
# This line tells Python to pull all the keys from the dictionary favorite_languages and assign them one at a time to the variable name.
for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}.")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")