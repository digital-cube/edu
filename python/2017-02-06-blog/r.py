

def g(s):

    if len(s) <= 1:
        return s

    return s[-1] + g(s[0:-1])

if __name__=="__main__":

    assert ( g('') == '' )
    assert ( g('x') == 'x' )
    assert ( g('12345') == '54321')

    print(g('abcde'))




#
# import random
#
#
# a = [chr(x) for x in list(range(ord('a'), ord('z')+1))+list(range(ord('A'), ord('Z')+1))]
#
# for length in range(2,8):
#
#     s = set()
#     iter = 0
#
#     while len(s)!=100:
#         iter+=1
#         random.shuffle(a)
#         s.add(''.join(a[:length]))
#
#     ar = list(s)
#     print("l{}={}".format(length,ar))
#
# self.assertTrue(True)
