import json
import http.client
import pickle
import math

if __name__=="__main__":

    with open('zones.json', 'r') as f:
        c = json.load(f)

    stream = {}
    for i in c['streams']:
        stream[i['type']] = i['data']

    print(stream.keys())

    zs={'1-165':0,
        '166-225':0,
        '226-270':0,
        '271-315':0,
        '316-360':0,
        '361-450':0,
        '450+': 0}

    zo={'1-156':0,
        '156-213':0}

    s=0

    for i in stream['watts']:

        if not i:
            i=0

        if i>=0 and i <= 165:
            zs['1-165'] += 1
        elif i > 165 and i <= 225:
            zs['166-225'] += 1
        elif i > 225 and i <= 270:
            zs['226-270'] += 1
        elif i>270 and i<=315:
            zs['271-315'] += 1
        elif i>315 and i <= 360:
            zs['316-360'] += 1
        elif i > 360 and i <= 450:
            zs['361-450'] += 1
        elif i>460:
            zs['450+'] += 1

        s+=1

    print(s)
    for i in ['1-165', '166-225', '226-270', '271-315', '316-360', '361-450', '450+']:
        print(i, zs[i], 100 * zs[i]/s)