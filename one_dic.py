from pprint import pprint
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

geo_logs_russia = []
for dictionary in geo_logs: # на этом шаге находятся элементы словаря
    for value in dictionary.values(): # на этом шаге находятся значения каждого словаря
        if value[1] == 'Россия':
            geo_logs_russia.append(dictionary)
pprint(geo_logs_russia)



