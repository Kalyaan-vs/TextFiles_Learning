import csv

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Imelda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

keys = ["album", "artist", "year"]
field_keys = {"album": "Album", "artist": "Artist", "year": "Year"}

filename = "albums.csv"
with open(filename, "w", encoding="utf-8", newline="",) as output_file:
    writer = csv.DictWriter(output_file, fieldnames=field_keys.values(), quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()
    for row in albums:
        zip_object = zip(keys, row)
        # print(zip_object)
        # for thing in zip(keys, row):
        #     print("\t", thing)
        albums_dict = dict(zip_object)
        print(albums_dict)
        transformed_dict = {field_keys[key]: value for key, value in albums_dict.items()}
        writer.writerow(transformed_dict)
# print(getattr(csv.excel, "delimiter"))
