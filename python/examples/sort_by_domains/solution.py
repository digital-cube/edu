import csv
byDomains = {}

with open('x.csv') as csvfile:

    names = csv.reader(csvfile)

    for row in names:
        name = row[0]
        lastname = row[1]
        email = row[2].lower()
        domain = email.split('@')[1]

        if domain not in byDomains:
            byDomains[domain] = []

        byDomains[domain].append( [email, name, lastname] )

domains = list(byDomains.keys())
domains.sort()

t = [(len(byDomains[domain]),domain) for domain in byDomains]
t.sort(reverse=True)

print(t)