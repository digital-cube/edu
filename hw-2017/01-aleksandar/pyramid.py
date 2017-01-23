#!/usr/bin/env python3
import sys

def pyramid(broj):
    #jedina greska je ispravljena sa broj+1 u range-u
    for i in range(1,broj+1):
        print(" "*(broj-i)+2*("#"*i))

if __name__=="__main__":

    if len(sys.argv)!=2:
        print('koristi program sa {} br_linija'.format(sys.argv[0]))
        sys.exit()

    try:
        num=int(sys.argv[1])
    except:
        print('greska, broj linija mora biti ceo broj')
        sys.exit()

    if num>60:
        print('maksimalni linija broj moze biti 60')
        sys.exit()

    pyramid(num)

