import csv


data = [
    {"name": "Alice", "age": 25, "city": "New York"},
    {"name": "Bob", "age": 30, "city": "Los Angeles"},
]

# Mapping old keys to new fieldnames
fieldnames = {"name": "Full Name", "age": "Age (Years)", "city": "Current City"}

with open("output_renamed.csv", mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames.values())

    writer.writeheader()  # Writes: Full Name, Age (Years), Current City

    for row in data:
        transformed_row = {fieldnames[key]: value for key, value in row.items()}  # Rename keys
        writer.writerow(transformed_row)

print("CSV file with renamed headers created!")
