favorite_places = {
    'john': ['washington'],
    'stacy': ['new york', 'hobby lobby', 'georgia'],
    'jim': ['arkansas', 'mississippi', 'tj max']
}

for name, places in favorite_places.items():
    if len(places) > 1:
        print(f"{name.title()}'s favorite places are:")
        for place in places:
            print("\t" + place.title())
    else:
        print(f"{name.title()}'s favorite place is:")
        for place in places:
            print("\t" + place.title())