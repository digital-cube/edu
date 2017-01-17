import csv

with open('input.csv','r') as f:
    
    reader = csv.reader(f)
    
    for aline in reader:
        for c in range(1,len(aline)):
            aline[c]=int(aline[c])
        print(aline)