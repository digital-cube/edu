
def is_palindrom(n):

    s = str(n)
    l = len(s)

    for i in range(0, l//2):
        if s[i] != s[l-1-i]:
            return False

    return True


def largest_palindrom():

    palindroms = []

    for a in range(999, 100, -1):
        for b in range(999, 100, -1):
            if is_palindrom(a*b):
                palindroms.append(a*b)

    return max(palindroms)

if __name__=="__main__":

    print(largest_palindrom())
