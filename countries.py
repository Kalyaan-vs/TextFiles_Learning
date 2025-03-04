input_filename = "country_info.txt"

countries = {}
empty_data = {}
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
        empty_fields = []
        for key, value in country_dict.items():
            if not value:
                empty_fields.append(key)
                empty_data[country] = empty_fields
        # print(country_dict)
        countries[country.casefold()] = country_dict
        countries[code.casefold()] = country_dict
        countries[code3.casefold()] = country_dict
# print(countries)
# print(empty_data)
city = {*{}}
# print(countries.items())
for key, value in countries.items():
    if not value["capital"]:
        city.add(value["name"])
print(city)
# Challenge
while True:
    chosen_country = input("Please enter the name or code of the country: ")
    country_key = chosen_country.casefold()
    if country_key in countries:
        country_info = countries[country_key]
        # print(f"The currency of {chosen_country} is {country_info['currency']}")
        if country_info['capital']:
            capital_of_country = country_info['capital']
        else:
            capital_of_country = country_info["name"]
        print(f"The capital of {chosen_country} is {capital_of_country}")
    #     capital_of_country = country_info['capital']
    #     if capital_of_country:
    #         print(f"The capital of {chosen_country} is {capital_of_country}")
    #     else:
    #         print(f"The {chosen_country} doesn't have capital")
    elif chosen_country == "quit":
        break
    else:
        print("Invalid input")

# Revise
# while True:
#     chosen_country = input("Please enter the country name or country code: ")
#     country_key = chosen_country.casefold()
#     if chosen_country in countries:
#         country_info = countries[chosen_country]
#         if country_info["capital"]:
#             country_capital = country_info["capital"]
#         else:
#             country_capital = country_info["name"]
#         print(f"The {chosen_country} capital is {country_capital} ")
#     elif chosen_country == "quit":
#         break
#     else:
#         print("Invalid input")


