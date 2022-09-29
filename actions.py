import uuid

def add_info():
    info_first_name = str(input('Введите фамилию: '))
    info_second_name = str(input('Введите имя: '))
    info_phone = int(input('Введите номер телефона: '))
    info_position = str(input('Введите должность: '))

    if info_first_name == "" or info_second_name == "" or  (info_phone > 100000000000 and info_phone < 10000000000) or info_position == "":
        print('Все строки должны быть заполнены - запись данных прервана')
        return
    with open('info_employees.txt', 'a', encoding="utf-8" ) as file:
        file.write(str(uuid.uuid1()) + ', ' + info_first_name + ', ' + info_second_name + ', ' + str(info_phone) + ', ' + info_position + '\n')
        file.close()


def search_info():
    number = int(input('По какому полю хотите искать запись: 0 - ID, 1 - Фамилия, 2 - Имя, 3 - Номер телефона, 4 - Должность \n Введите номер поля: '))
    if number > 4:
        print('Неверно введенная цифра - поиск прерван')
        return
    enter_info = str(input('Введите строку поиска: '))
    with open('info_employees.txt', 'r', encoding="utf-8" ) as file:
        for line in file:
            if enter_info.upper() in line.split(', ')[number].upper() and number != (len(line.split(', ')) - 1):
                print(line)
            elif number == (len(line.split(', ')) - 1) and enter_info.upper() in line.split(', ')[number][:-1].upper():
                print(line)
    file.close()


def look_info():
    with open('info_employees.txt', 'r', encoding="utf-8" ) as file:
        for line in file:
            print(line, end='')
    file.close()


def delete_worker():
    id_worker = str(input('Введите ID сотрудника, которого нужно удалить из базы: '))
    with open('info_employees.txt', 'r', encoding="utf-8" ) as file:
        lines = file.readlines()
    with open('info_employees.txt', 'w', encoding="utf-8" ) as file:   
        for line in lines:
            new_line = line.split(', ')
            if id_worker != new_line[0]:
                file.write(line) 
    file.close()


def update_info():
    id_worker = str(input('Введите ID сотрудника, данные которого нужно отредактировать: '))
    with open('info_employees.txt', 'r', encoding="utf-8" ) as file:
        lines = file.readlines()
    with open('info_employees.txt', 'w', encoding="utf-8" ) as file:   
        for line in lines:
            new_line = line.split(', ')
            if id_worker == new_line[0]:
                print(f'Найден сотрудник: {line}')
                number = int(input('По какому полю хотите отредактировать запись: 1 - Фамилия, 2 - Имя, 3 - Номер телефона, 4 - Должность \n Введите номер поля: '))
                change = str(input('Введите замену: '))
                new_line[number] = change
                if number == len(new_line) - 1:
                    file.write(', '.join(new_line) + '\n')
                else:
                    file.write(', '.join(new_line)) 
            else:
                file.write(line) 
    file.close()


def export_info():
    number = int(input('Выберите формат показа данных: \n1: ID, Фамилия, Имя, Телефон, Должность \n2: \nID \nФамилия \nИмя \nТелефон \nДолжность \nВведите номер формата: '))
    file = open('info_employees.txt', 'r', encoding="utf-8")
    new_file = open('export_file.txt', 'w', encoding="utf-8")
 
    if number == 1:
        for line in file:
            new_file.write(line)   
    elif number == 2:
       for line in file:
            info = line.split(', ')
            for i in info:
                new_file.write(i + '\n')   
            # new_file.write('\n')
    else:
        file.close()
        new_file.close()
        print('Неверно введенная цифра - экспорт данных прерван')
        return
    file.close()
    new_file.close()
