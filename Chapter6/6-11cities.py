cities = {
    'jackson':{
        'country': 'united states',
        'population': '149,762',
        'fact': 'The city is named after General Andrew Jackson, after the Battle of New Orleans during the War of 1812.'
    },
    'minneapolis':{
        'country':'united states',
        'population':'425,336',
        'fact': 'Father Lois Hennepin was the first European in Minneapolis.',
    },
    'tokyo':{
        'country': 'japan',
        'population': '37,000,000',
        'fact': 'This is the most populous city in the world.',
    }
}

for city, cityInfo in cities.items():
    print(f"{city.title()} is located in {cityInfo['country'].title()} with a population of {cityInfo['population']}. Fun fact: {cityInfo['fact']}")
    print("")