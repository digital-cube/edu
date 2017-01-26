"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

"""
Smallest number = SN
"""
def smallest_number():
    SN = 2520
    if SN % 11 == 0 and SN % 12 == 0:
        return SN
    else:
        SN += 2
    return SN

print("Smallest number of 11 and 12 is: {}".format(smallest_number()))

def smalest_number():
    SN = 2520
    while (SN % 11 == 0 and SN % 12 == 0 and SN % 13 == 0 and SN % 14 == 0 and SN % 14 == 0 and SN % 15 == 0 and SN % 16 == 0 and SN % 17 == 0 and SN % 18 == 0 and SN % 19 == 0 and SN % 20 == 0):
        SN += 20
    return SN

print("Smallest number of 11 to 20 is: {}".format(smalest_number()))

def problem_5():
    SN = 2520
    while True:
        SN = 2520
        if SN % 11 == 0 and SN % 12 == 0 and SN % 13 == 0 and SN % 14 == 0 and SN % 15 == 0 and SN % 16 == 0 and SN % 17 == 0  and SN % 18 == 0  and SN % 19 == 0 and SN % 20 == 0:
            continue
        else:
            return

# rangemax = 20
# def div_check(n):
#     for i in range(11,rangemax+1):
#         if n % i == 0:
#             continue
#         else:
#             return False
#     return True
#
# if __name__ == '__main__':
#    num = 2
#    while not div_check(num):
#        print (num)
#        num += 20
#    print (num)