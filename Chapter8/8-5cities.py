def describe_city(city, country = 'United States'):
    print(f"{city.title()} is in {country.title()}.")

describe_city('jackson')
describe_city('minneapolis')
describe_city('dublin', 'ireland')