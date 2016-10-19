import json

a = {
    'BabyPhone': 'on',
    'Language': 'en'
}



b = {'General': {
        'Baby': {
            'BabyPhone': 'off'
        }
    },
    'Others': {
        'Language': 'en'
    }
}

a2b = {
    'BabyPhone': ['General', 'Baby', 'BabyPhone'],
    'Language': ['Others', 'Language']
}

print(a);
print(b);

for key in a.keys():
    print (key)
    path = a2b[key]
    print (path, ':', path[:-1])

    root = b
    for p in path[:-1]:
        root = root[p]

    root[path[-1]] = a[key]

print(json.dumps(b, indent=4))