


import socket

import validate_email
import csv

data = []

with open('nlc.csv', 'rt') as f:
    for line in csv.reader(f):
        data.append({'email': line[1].lower().strip() , 'name':line[0]})

domains = {}
emls = {}

for row in data:
    if validate_email.validate_email(row['email']):
        email = row['email'] + row['name']
        a = email.split('@')
        domain = a[1]

        if not email in emls:
            emls[email] = 1
        else:
            emls[email]+=1

        if domain in ('pc.dk','asmund.dk', 'mail.dk'):
            continue

        if domain in domains:
            domains[domain] += 1
        else:
            domains[domain] = 1


list_of_domains = [(domains[i], i) for i in domains]

list_of_domains.sort(reverse=True)

print(list_of_domains)

# for i in list_of_domains:
    # try:
    #     socket.getaddrinfo(i[1],0,0,0,0)
    # except:
    #     print("imamo problem sa domenom",i)

print(emls)
list_of_emls = [(emls[i], i) for i in emls]
list_of_emls.sort(reverse=True)

print(list_of_emls)

for i in list_of_emls:
    if i[0]>1:
        print(i)
