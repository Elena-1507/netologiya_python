ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

ids_list =[]
for el in ids.values():
    for i in el:
        ids_list.append(i)


id = set(ids_list)
id_list = sorted(id)
# print(id)
print(id_list)
