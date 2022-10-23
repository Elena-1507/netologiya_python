documents = [
{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
{"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
{"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
	'1': ['2207 876234', '11-2', '5455 028765'],
	'2': ['10006'],
	'3': []
}


def print_name(document_number):
	for i in documents:
		i_document_number = i['number']
		if i_document_number == document_number:
			print(i['name'])
			return
	else:
		print('Документ с таким номером не найден')

# print_name(input('Введите номер документа:'))

def print_shelf(document_number):
	for i, key in directories.items():
		for k in key:
			k_document_number = k
			if k_document_number == document_number:
				print(f'Документ номер {k} на полке {i}')
		else:
			print('Документ с таким номером не найден')

# print_shelf(input('Введите номер документа:'))

def print_list():
	for i in documents:
		hot = i.values()
		print(list(hot))

# print_list() 

def add_document():
	new_type = input('Введите тип документа: ')
	new_number = input('Введите номер документа: ')
	new_name = input('Введите имя владельца документа: ')
	new_directories = int(input('Введите номер полки для хранения: '))

	new_document = {
		'type': new_type,
		'number': new_number,
		'name': new_name
	}
	documents.append(new_document)

	if 0 < new_directories < 4:
		list = directories[str(new_directories)]
		list.append(new_number)
		print(directories)
	else:
		print('Полки не существует. Введите значение от 1 до 3')

# add_document()

command = input('Введите команду: ')
if command == 'p':
	print_name(input('Введите номер документа:'))
elif command == 's':
	print_shelf(input('Введите номер документа:'))
elif command == 'l':
	print_list()
elif command == 'a':
	add_document()
else:
	print('Упс... Команда мне не знакома. Попробуйте ещё раз')


