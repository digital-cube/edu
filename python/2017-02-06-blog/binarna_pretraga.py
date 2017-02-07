
import sys
db_index = [('aaliyah', 110), ('aaron', 17), ('abigail', 83), ('aca', 183), ('adam', 43), ('addison', 64), ('adrian', 128), ('aidan', 9), ('aiden', 99), ('aleksandar', 190), ('alex', 80), ('alexa', 138), ('alexander', 32), ('alexandra', 141), ('alexis', 216), ('allison', 65), ('alyssa', 5), ('amelia', 136), ('andrea', 127), ('andrew', 148), ('andrija', 107), ('angel', 151), ('angelina', 137), ('anna', 87), ('anthony', 57), ('ariana', 132), ('arianna', 184), ('ashley', 31), ('aubrey', 85), ('audrey', 53), ('austin', 48), ('autumn', 211), ('ava', 178), ('avery', 170), ('ayden', 12), ('bailey', 187), ('bella', 3), ('benjamin', 113), ('blake', 204), ('brandon', 69), ('brayden', 95), ('brian', 115), ('brianna', 163), ('brody', 6), ('brooke', 54), ('brooklyn', 165), ('bryan', 11), ('caleb', 98), ('cameron', 51), ('camila', 112), ('carlos', 176), ('caroline', 129), ('carson', 173), ('carter', 202), ('charles', 168), ('charlotte', 96), ('chase', 39), ('chloe', 147), ('christian', 119), ('christopher', 116), ('claire', 196), ('cole', 75), ('colton', 149), ('connor', 49), ('cooper', 19), ('daniel', 102), ('david', 166), ('destiny', 16), ('diego', 145), ('dominic', 218), ('dylan', 182), ('eli', 29), ('elijah', 172), ('elizabeth', 197), ('ella', 209), ('emily', 90), ('emma', 195), ('eric', 205), ('ethan', 76), ('eva', 67), ('evan', 123), ('evelyn', 177), ('faith', 206), ('gabriel', 7), ('gabriella', 36), ('gabrielle', 169), ('gavin', 84), ('genesis', 161), ('gianna', 40), ('goran', 154), ('grace', 164), ('hailey', 91), ('hannah', 15), ('hayden', 13), ('henry', 199), ('hunter', 89), ('ian', 212), ('igor', 77), ('isaac', 118), ('isabella', 124), ('isaiah', 179), ('ivan', 52), ('jack', 198), ('jackson', 200), ('jacob', 101), ('jaden', 121), ('james', 122), ('jasmine', 62), ('jason', 26), ('jaxon', 42), ('jayden', 34), ('jeremiah', 188), ('jessica', 41), ('jesus', 30), ('jocelyn', 144), ('john', 181), ('jonathan', 68), ('jordan', 70), ('jose', 74), ('joseph', 186), ('joshua', 193), ('josiah', 27), ('jovan', 131), ('juan', 160), ('julia', 22), ('julian', 217), ('justin', 93), ('kaitlyn', 215), ('katherine', 180), ('kayla', 14), ('kaylee', 109), ('kevin', 150), ('khloe', 46), ('kimberly', 143), ('kylie', 79), ('landon', 18), ('lauren', 157), ('layla', 61), ('laza', 63), ('leah', 44), ('levi', 214), ('liam', 56), ('lillian', 71), ('lily', 103), ('logan', 47), ('lucas', 120), ('lucy', 159), ('luis', 133), ('luke', 10), ('mackenzie', 81), ('madeline', 207), ('madelyn', 73), ('madison', 174), ('makayla', 156), ('maria', 153), ('mariah', 1), ('marinko', 111), ('mason', 94), ('matthew', 194), ('max', 203), ('maya', 97), ('melanie', 158), ('mia', 37), ('michael', 104), ('mika', 142), ('mladen', 35), ('molly', 88), ('morgan', 208), ('munira', 126), ('naomi', 86), ('natalia', 135), ('natalie', 108), ('nathan', 50), ('nathaniel', 175), ('nenad', 213), ('nevaeh', 106), ('nicholas', 130), ('noah', 162), ('oliver', 134), ('olivia', 146), ('owen', 191), ('paige', 20), ('parker', 92), ('payton', 114), ('pera', 4), ('peyton', 24), ('rachel', 140), ('riley', 2), ('robert', 25), ('ryan', 38), ('samantha', 125), ('samuel', 82), ('sarah', 59), ('savannah', 21), ('sebastian', 117), ('serenity', 152), ('slavisa', 23), ('sloba', 45), ('sofia', 58), ('sophia', 139), ('sophie', 33), ('stella', 155), ('steva', 167), ('sydney', 72), ('taylor', 201), ('thomas', 100), ('trinity', 210), ('tristan', 185), ('trta', 8), ('tyler', 78), ('valeria', 219), ('victoria', 66), ('william', 189), ('wyatt', 192), ('xavier', 28), ('zachary', 55), ('zika', 60), ('zoe', 171), ('zoey', 105)]

def linear_search(name):
    global db_index

    idx=1
    for i in db_index:
        if i[0]==name:
            return i[1], idx
        idx+=1

    return None


def binary_search(name, start=0, end=len(db_index)-1, level=0):

    # print (level*' '+'binary_sarch({},{},{})'.format(name, start, end))

    if not hasattr(binary_search, 'cnt'):
        binary_search.cnt = 0

    binary_search.cnt += 1

    if start == end - 1:
        if db_index[start][0] == name:
            return db_index[start][1]
        if db_index[end][0] == name:
            return db_index[end][1]

        return None

    sredina = ( end + start ) // 2

    if db_index[sredina][0] == name:
        return db_index[sredina][1]

    if db_index[sredina][0] > name:

        return binary_search( name, start, sredina, level+1)
    else:

        return binary_search( name, sredina, end, level+1)


if __name__=="__main__":

    for i in range(0, len(db_index)):

        pos_l = linear_search( db_index[i][0] )

        if not hasattr(binary_search, 'cnt'):
            binary_search.cnt = 0
        binary_search.cnt = 0

        pos_b = binary_search( db_index[i][0] )

        print ("{:<20} {:<10}   {:<10}".format(str(db_index[i]), str(pos_l), str((pos_b, binary_search.cnt))))
        # assert( pos_l == pos_b )

#