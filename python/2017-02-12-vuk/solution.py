
input = []

with open('input.txt') as f:
    for line in f:
        line = line.strip()
        line = line.replace('  ',' ')
        if line:
            input.append([int(x) for x in line.split(' ')])

# print('-'*10)
# for i in input:
#     print(i)

while len(input) != 1:

    novi_niz = []
    for index in range(0, len(input[-2])):

        novi_niz.append( input[-2][index] + max(input[-1][index], input[-1][index+1]) )

    input[-2] = novi_niz
    del input[-1]


    # print('-'*10)
    # for i in input:
    #     print(i)

print(input[0][0])