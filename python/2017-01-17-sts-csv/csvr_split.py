
with open('input.csv','r') as f:
    for line in f:
        aline=line.strip().split(',')
        for c in range(1,len(aline)):
            aline[c]=int(aline[c])
            
        print(aline)