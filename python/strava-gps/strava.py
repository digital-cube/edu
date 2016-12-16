import json
import http.client
import pickle
import math

if __name__=="__main__":

    with open('strava.json', 'r') as f:
        c = json.load(f)

    stream = {}
    for i in c['streams']:
        stream[i['type']] = i['data']

    print(stream.keys())

    # load_google_map_elevations(stream)

    with open('galt.pck','rb') as f:
        alt2=pickle.load(f)

    print(alt2)

    first = True
    total_distance = 0

    from prettytable import PrettyTable

    table = PrettyTable(['time (sec)', 'strava distance(m)', 'latitude', 'longitude', 'strava-altitude', 'google-maps-altitude', 'h-distance', 'v-distance', 'distance', 'total-distance', 'speed m/s', 'pace min/km'])


    x, y = [], []

    last_s_distance = 0
    last_s_time = 0
    for i in range(len(stream['latlng'])):
        p = stream['latlng'][i]
        if first:
            first = False
            last_point = p
            last_elev = alt2[i]
            last_time = stream['time'][i]
            h_dist = 0
            v_dist = 0
            dist = 0
            speed = 0
        else:
            h_dist = 1000 * haversine((last_point[0], last_point[1]), (p[0], p[1]))
            v_dist = last_elev - alt2[i]
            time_diff = stream['time'][i] - last_time
            dist = math.sqrt(h_dist**2 + v_dist**2)
            last_elev = alt2[i]
            last_time = stream['time'][i]
            last_point = p
            speed = dist / time_diff

        pace = round(60.0 / (speed * 3.6), 2) if speed>0 else None

        total_distance += dist

        table.add_row(
            [stream['time'][i],
             stream['distance'][i],
             stream['latlng'][i][0],
             stream['latlng'][i][1],
             stream['altitude'][i],
             round(alt2[i],2),
             round(h_dist,2),
             round(v_dist,2),
             round(dist,2),
             round(total_distance,2),
             round(speed,2),
             round(pace,2) if pace else None

             ])

        # print(stream['time'][i], stream['latlng'][i], alt2[i], dist, 'vdist=',v_dist, stream['distance'][i], total_distance, speed, pace)

        if i > 0 and i % 10 == 0:

            segment_distance = total_distance - last_s_distance
            segment_time = stream['time'][i] - last_s_time

            print('tot_distance',total_distance, 'time', stream['time'][i], 'sdist',segment_distance, 'stime', segment_time, pace)

            speed = segment_distance / segment_time
            pace = round(60.0 / (speed * 3.6), 2) if speed>0 else None

            x.append(total_distance)
            y.append(pace)

            last_s_distance = total_distance
            last_s_time = stream['time'][i]





    # with open('table.txt','w') as f:
    #
    #     f.write(str(table))
    #
    # print(table)

# dv = zip( stream['distance'], stream['velocity_smooth'] )
#
# # print(dv)
#
# print('m,m/s,km/h,min/km');
#
# x=[]
# y=[]
# for i in dv:
#     minperkm = round(60.0 / (i[1]*3.6) ,2) if i[1]>0 else None
#     # print('{},{},{},{}'.format(i[0],i[1],round(i[1]*3.6,2),minperkm))
#     # print(i[0],'m',i[1],'m/s',round(i[1]*3.6,2),'km/h',minperkm,'min/perkm');
#
#     if not minperkm:
#         continue
#
#     if minperkm>3 and minperkm<10:
#         x.append(i[0])
#         y.append(minperkm)
#
#     print(i[0], minperkm)
#

import matplotlib.pyplot as plt
import numpy as np


line, = plt.plot(x, y)

axes = plt.gca()

axes.set_ylim([1, 15])

axes.invert_yaxis()

plt.show()


# s=10
# y2=[]
# for i in range(0,len(y)-`):
#     ss=0
#     for si in range(0,s):
#         ss+=y[i+si]
#     ss/=s
#     y2.append(ss)
# for i in range(len(y)-s, len(y)):
#     y2.append(y2[-1])

# y2=y[:5 ]


# print(len(x))
# print(len(y))
#
# line, = plt.plot(x, y)
#
# plt.gca().invert_yaxis()
#
# plt.show()
#
