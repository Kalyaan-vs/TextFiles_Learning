import csv

csv_filename = "OlympicMedals_2020.csv"

with open(csv_filename, encoding="utf-8", newline="") as csv_file:
    header = (csv_file.readline().strip()).split(",")
    # print(type(header))
    print(f"Columns headers: {header}")
    reader = csv.reader(csv_file)
    # print(reader)
    for row in reader:
        print(row)
    # for Rank, Country, Gold, Silver, Bronze, Total in reader:
    #     Rank = int(Rank)
    #     Gold = int(Gold)
    #     Silver = int(Silver)
    #     Bronze = int(Bronze)
    #     Total = int(Total)
    #     print(Rank, Country, Gold, Silver, Bronze, Total)
