import csv

rows = []

with open('person.csv', 'r') as csvfile:
    # csvreader = csv.reader(csvfile)
    csvreader = csv.DictReader(csvfile)

    # for row in csvreader:
    #     rows.append(row)
    rows = list(csvreader)
    print("total baris", csvreader.line_num)

# print(rows)

# for row in rows[:5]:
#     print(row[0] + "-" + row[1])

for row in rows[:5]:
    print(row["first_name"] + "-" + row["email"])