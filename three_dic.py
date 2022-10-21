queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]

storge = {} 
r = 100/len(queries) 
for querie in queries:
    h = len(querie.split())
   
    if h in storge:
        storge[h] += 1
    else:
        storge[h] = 1

for key, value in storge.items():
    i = (value * r)
    e = round(i)
    storge[key] = e

for key, value in storge.items():
    print(f'Количество ключевых запросов состоящих из {key} слов состовляет {value} % ')
