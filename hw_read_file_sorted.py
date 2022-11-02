import operator

count_dic = {}

def count_file_lines(file_name):
    with open(file_name, encoding='utf-8') as file:
        count = sum(1 for _ in file)
        print (count)
        count_dic[file_name] = (count)

count_file_lines('1.txt')
count_file_lines('2.txt')
count_file_lines('3.txt')

sorted_count_dic = sorted(count_dic.items(), key=operator.itemgetter(1))
print(sorted_count_dic)

count_dic = dict(sorted_count_dic)
print(count_dic)

# def open_file(file):

for count_dic_key, count_dic_value in count_dic.items():
    print(count_dic_key)
    print(f'Файл содержит {count_dic_value} строк')
    with open(count_dic_key, encoding='utf-8') as file:
        k = file.readlines()
        print(k)
