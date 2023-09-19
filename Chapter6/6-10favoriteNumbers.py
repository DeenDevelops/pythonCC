favoriteNumbers = {
    "jim": [1, 2, 3],
    "pam": [4, 5],
    "dwight": [6,7,8,9],
    "oscar": [10],
    "stanley": [11],
}

for name, number in favoriteNumbers.items():
    if len(number) > 1:
        print(f"{name.title()}'s favorite numbers are:")
        for num in number:
            print(num)
    else:
        print(f"{name.title()}'s favorite number is:")
        for num in number:
            print(num)