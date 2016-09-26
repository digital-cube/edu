text_rooms = '''
1: 100, 101, 102, 104
2: 200, 201, 202, 203, 204
3: 300, 301
1: 103
'''

j_floors = {}

# x = text_rooms.split('\n')
x = text_rooms.splitlines()
# print(x)

for i in x:
    if i != '':
        a = i.split(':')
        # print(a)
        floor = a[0]
        rooms = a[1].split(',')

        if floor not in j_floors:
            j_floors[floor] = []
        for room in rooms:
            j_floors[floor].append(room)

for f in j_floors:
    j_floors[f].sort()

print(j_floors)
