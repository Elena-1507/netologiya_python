stats = {'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
list = []
for item in stats.values():
    list.append(item)

max_list = max(list)

for network, sum in stats.items():
    if sum == max_list:
        print(network)
        

