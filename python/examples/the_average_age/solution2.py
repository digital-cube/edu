with open('input.txt','r') as data:
    lista = data.read()

    print(lista)

    godine = lista.split()

    print(godine)

    godista = [ item for item in godine if item.isdigit() ]
    print(godista)
    godista = [ int(item) for item in godine if item.isdigit() ]
    print(godista)
    suma = sum(godista)
    length = len(godista)
    res = float(suma)/length
    print(res)
    print(round(res,2))

# another way
# print('{:.2f}'.format(res))
# print('{:.4f}'.format(res))
