dc = [
['Igor Jeremic', 1976, 8, 24],
['Munira Hasanagic', 1992, 12, 11],
['Aleksandar Lazarevic', 1991, 4, 23],
['Ivan Jankovic', 1983, 11, 27],
['Ivo Kovacevic', 1984, 11, 1],
['Mladen Milicevic', 1993, 3, 24 ],
['Goran Radovanovic', 1985, 2, 8],
['Slobodan Dolinic', 1980, 8, 5],
['Nebojsa Dolas', 1983, 2, 21],
['Marinko Jankovic', 1987, 5, 5],
['Andrija Garabinovic', 1980, 8, 13]
]

def dana_do_rodjendana(y,m,d):
    return y+m+d

dcd = [ ( dana_do_rodjendana(i[1],i[2],i[3]), i[0] ) for i in dc ] 

#dcd = []
#for i in range(0,len(dc)):
#    pr = dc[i]
#    dcd.append( (pr[0], dana_do_rodjendana(pr[1], pr[2], pr[3])) )


print(dcd)

dcd.sort()

print(dcd)
