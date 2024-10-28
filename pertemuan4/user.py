import csv

rows = [
    {'name': 'John Doe', 'skill': 'Python', 'power': '100'},
    {'name': 'Jane Doe', 'skill': 'Java', 'power': '90'},
    {'name': 'Alex Smith', 'skill': 'JavaScript', 'power': '95'}
]


with open('data.csv', 'a') as csvfile:
    field = ['name', 'skill','power']
    write = csv.DictWriter(csvfile, fieldnames=field)

    write.writeheader()
    write.writerows(rows)




