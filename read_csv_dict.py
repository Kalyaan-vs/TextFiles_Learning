import csv

cereal_filename = "cereal_grains.csv"
with open(cereal_filename, "r", encoding="utf-8", newline="") as cereal_file:
    reader = csv.DictReader(cereal_file)
    for row in reader:
        print(row)

csv.register_dialect("kalyaan", csv.excel)
print(csv.list_dialects())
csv.unregister_dialect("kalyaan")
print(csv.list_dialects())