data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac - Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

# plant_filename = "flower_print.txt"
#
# with open(plant_filename, "w") as plants:
#     for plant in data:
#         print(plant, file=plants)
#
# new_list = []
# with open(plant_filename, 'r') as plants:
#     for plant in plants:
#         new_list.append(plant.rstrip())
#
# print(new_list)

# plant_filename = "flower_write.txt"
#
# with open(plant_filename, 'w') as plants:
#     for plant in data:
#         plants.write(plant)
#
print(data)
print(type(data))
string_representation = data.__str__()
print(string_representation)
print(type(string_representation))

filename = "test_write.txt"

with open(filename, "w") as text:
    for i in range(10):
        print(i, file=text)

with open(filename, "a") as text:
    for i in range(10):
        text.write(str(i) + "\n")
