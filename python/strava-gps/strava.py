import json

with open('strava.json', 'r') as f:
    c = json.load(f)

stream = {}

for i in c['streams']:
    # print(i.keys())
    # print(i['type'], i['series_type'])
    stream[i['type']] = i['data']


dv = zip( stream['distance'], stream['velocity_smooth'] )

# print(dv)

print('m,m/s,km/h,min/km');
for i in dv:
    minperkm = round(60.0 / (i[1]*3.6) ,2) if i[1]>0 else None
    print('{},{},{},{}'.format(i[0],i[1],round(i[1]*3.6,2),minperkm))
    # print(i[0],'m',i[1],'m/s',round(i[1]*3.6,2),'km/h',minperkm,'min/perkm');


