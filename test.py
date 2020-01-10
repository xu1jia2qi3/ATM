data = {
    'tsdf': {'name': 11, 'money': 100},
    'a': {'name': 33, 'money': 300},
    'asdfa': {'name': 22, 'money': 200},
    'qwe': {'name': 44, 'money': 400},
    'sss': {'name': 66, 'money': 600},
    'sdf': {'name': 55, 'money': 500}
}

sort = sorted(data.items(), key = lambda x:x[1]['money'])

# lambda x: True if x % 2 == 0 else False
print(sort)

for item in data.items():
    if item[1]['money'] >= 300:
        print(item)
