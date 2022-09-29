
from actions import add_info, search_info, look_info, delete_worker, update_info, export_info


number = 0
while number != 7:
    number = int(input('Введите действие, которое хотите совершить:\n 1 - добавление нового сотрудника; \n 2 - поиск сотрудника; \n 3 - просмотр списка сотрудников; \n 4 - удаление сотрудника из базы; \n 5 - редактирование данных сотрудника; \n 6 - экспорт данных; \n 7- закончить работу \n Введите номер: '))
    if number == 1:
        add_info()
    if number == 2:
        search_info()
    if number == 3:
        look_info()
    if number == 4:
        delete_worker()
    if number == 5:
        update_info()
    if number == 6:
        export_info()

