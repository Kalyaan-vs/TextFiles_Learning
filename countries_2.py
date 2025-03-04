input_filename = "country_info.txt"

countries = {}
code_lookup = {}
with open(input_filename) as country_file:
    country_file.readline()  # To skip the first line the data
    for row in country_file:
        data = row.strip("\n").split("|")
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep="\n\t")
        country_dict = {
            "name": country,
            "capital": capital,
            "country_code": code,
            "cc3": code3,
            "dialing_code": dialing,
            "timezone": timezone,
            "currency": currency,
        }
        # print(country_dict)
        countries[country.casefold()] = country_dict
        code_lookup[code.casefold()] = country.casefold()
print(countries)
# print(code_lookup)

# Challenge
while True:
    chosen_country = input("Please enter the name or code of the country: ")
    country_key = chosen_country.casefold()
    if country_key in countries or country_key in code_lookup:
        if len(country_key) == 2:
            country_info = countries[code_lookup[country_key]]
        else:
            country_info = countries[country_key]
        country_name = country_info["name"]
        print(f'The capital of {country_name} is {country_info["capital"]}')

    elif country_key == "quit":
        break
    else:
        print("Invalid input")
