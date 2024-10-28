import json

# data = {}
# data['member']=[
#     {'name': 'John Doe', 'skill': 'Python', 'power': '100'},
#     {'name': 'Jane Doe', 'skill': 'Java', 'power': '90'},
#     {'name': 'Alex Smith', 'skill': 'JavaScript', 'power': '95'}
# ]

# with open('C:/Users/malik/Kerjaan/python-file/pertemuan5/member.json', 'w') as memberfile:
#     json.dump(data, memberfile)

with open('C:/Users/malik/Kerjaan/python-file/pertemuan5/member.json', 'r') as memberfile:
    data = json.load(memberfile)

    for member in data['member']:
        print("namanya adalah " + member['name'] + " membunyai skill: " + member['skill'] + " memiliki power: "+ member['power'])