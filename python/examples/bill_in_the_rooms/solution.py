import datetime
import csv
import sys

'''

id  ,'destination,      ,prefix,z,m,cost
4201,"Macedonia, mobile",38977,3,1,0.50
4202,"Macedonia, mobile",38978,3,1,0.50
4203,Italy,39,9,,0.05
4204,"Italy, Rete Fissa",390,9,,0.05
4205,"Italy, Servizio Clienti TIM",39119,9,,0.05
4206,"Italy, Seat Pagine Gialle S.p.A.",391240,9,,1.20
4207,"Italy, 1244 S.R.L.",391244,9,,1.20

'''

byLengthByPrefix = {}
samocena={}
def loadPrices():
    with open('prices.csv') as csvfile:
        spamreader= csv.reader(csvfile)
        for row in spamreader:
            if row[0]=='Nr':
                continue

            destination = row[1]
            prefix = row[2]
            cost = int(100*float(row[5]))

            l = len(prefix)
            if l not in byLengthByPrefix:
                byLengthByPrefix[l] = {}

            byLengthByPrefix[l][prefix] = [destination, cost]



def findPrefix(number):
    for l in range(12,0,-1):
        if len(number) < l:
            continue

        np=number[:l]
        if np in byLengthByPrefix[l]:
            return byLengthByPrefix[l][np]

    return ['N/A',0]

def izdvojicCene():

    poSobi={}

    for row in csv.reader(open('cdr.txt'), delimiter='|'):

        '''

    datum   |vreme   |  |src||duration|destination|
    0       | 1      |  | 3 ||5       |6          |

    21.06.16|11:59:57|17|199||00:00:17|03351345680||2|||0|2|
    21.06.16|12:26:12|17|199||00:00:03|03351345680||2|||0|2|
    21.06.16|12:27:14|17|199||00:00:03|3351345680||2|||0|2|


        '''
        cdate=row[0]
        ctime=row[1]

        dt_end = datetime.datetime.strptime( '20{}-{}-{}T{}'.format(cdate[6:8],cdate[3:5],cdate[0:2],ctime), "%Y-%m-%dT%H:%M:%S" )

        if dt_end.month!=8:
            continue

        room = row[3]
        duration = 3600*int(row[5][0:2]) + 60*int(row[5][3:5]) + int(row[5][6:8])
        destination = row[6]

        if len(destination)<5:
            continue

        if destination[0]=='0' and destination[1]!='0':
            destination='39'+destination

        if destination[:2]=='00':
            destination=destination[2:]

        dt_start = dt_end - datetime.timedelta( seconds=duration )

        dest_name, price_cent = findPrefix(destination)


        # print( dt_start,dt_end, room, duration, destination, 'price=', dest_name, price_cent, round(price_cent*duration/60/100,2) )

        if room not in poSobi:
            poSobi[room]=[]

        poSobi[room].append( [dt_start, dt_end, duration, destination, round(price_cent*duration/60/100,2)] );

    sobe = [ int(i) for i in poSobi.keys() ]
    sobe.sort()

    for soba in sobe:
        print ('soba:',soba)

        # print(poSobi[str(soba)])
        cena=0
        for poziv in poSobi[str(soba)]:
            cena+=poziv[4]
            print( poziv[0], poziv[1], poziv[3], poziv[4] )

        print('\nukupno za sobu {} je {} eur'.format(soba,round(cena,2)))




if __name__=="__main__":

    loadPrices()
    izdvojicCene()
