

def test():

    ip="123.xzc.221.44"

    #saip=ip.split('.')
    # aip=[]
    # for i in saip:
    #     aip.append(int(i))

    try:
        aip = [int(i) for i in ip.split('.')]

        if len(aip)!=4:
            return False

        for i in aip:
            if i<0 or i>255:
                return False

        print (aip)

    except Exception as e:
        return False

    return True

print(test())
