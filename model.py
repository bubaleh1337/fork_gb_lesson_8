def data(): # получаем из файла
  with open('data_file.txt', 'r', encoding='utf-8') as data_file:
    data = data_file.read().split('\n')

  return data

def add_contact(contact): # добавляем контакт
  with open('data_file.txt', 'a', encoding='utf-8') as data_file:
    data_file.write(f'{contact}\n')

  return contact

def find_contact(data): # поиск данных
  command = input('Меню: \n1. Искать по ФИО \n2. Искать по номеру телефона') # view.py
  match command:
    case 1:
      find_name = input('Введите ФИО: ')
      for values in data:
        if data[values] == find_name:
          print(data[values])

    case 2:
      find_phone = input('Введите номер телефона: ')
      for values in data:
        if data[values] == find_phone:
          print(data[values])

data()
add_contact('+4654456')
find_contact('+4654456')
