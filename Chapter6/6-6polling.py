favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'jon': 'go',
    'jim': 'rust'
}

takenPoll = ['sarah', 'edward']
for key in favorite_languages.keys():
    if key in takenPoll:
        print(f"{key.title()}, thank you for taking the poll.")
    else:
        print(f"{key.title()}, take the poll.")