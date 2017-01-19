



def dec2bin(dec):

    bin = ''
    if dec==0:
        return '0'

    while dec > 0:
        bin += '1' if dec % 2 else '0'
        dec //= 2

    return bin[::-1]

def dec2hex(dec):

    hex = ''
    if dec == 0:
        return '0'

    l=['0', '1', '2', '3', '4', '5', '6',
       '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    m = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '10': 'A',
         '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F',
         }

    while dec > 0:

        # 1
        # if ostatak > 9:
        #     ostatak = chr(65 + ostatak - 10)

        # 2
        # ostatak = m[str(dec % 16)]

        # 3
        ostatak = l[dec % 16]

        hex += "{}".format(ostatak) if ostatak else '0'
        dec //= 16

    return hex[::-1]

def dec2alphabet_and_numbs_36(dec):

    res = ''
    if dec == 0:
        return '0'

    l = [str(i) for i in range(0,10)] + \
        [chr(i) for i in range(ord('A'), ord('Z')+1)]

    length = len(l)

    while dec > 0:
        ostatak = l[dec % length]
        res += ostatak
        dec //= length

    return res[::-1]


def dec2alphabet_and_numbs_62(dec):

    res = ''
    if dec == 0:
        return '0'

    l = [str(i) for i in range(0,10)] + \
        [chr(i) for i in range(ord('A'), ord('Z')+1)] +\
        [chr(i) for i in range(ord('a'), ord('z') + 1)]

    length = len(l)

    while dec > 0:
        ostatak = l[dec % length]
        res += ostatak
        dec //= length

    return res[::-1]

if __name__=="__main__":
    for i in range(10000,10300):
        print(i, dec2alphabet_and_numbs_62(i), dec2alphabet_and_numbs_36(i), dec2hex(i), dec2bin(i))