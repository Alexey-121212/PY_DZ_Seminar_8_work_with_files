# Дополнить справочник возможностью копирования данных из одного файла в другой.
# Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.

from typing import List

def read_file(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            return lines
    except FileNotFoundError:
        print('файла нет. Сначала введите данные\n')
        return []

def show_data(data: list):
    i=0
    for line in data:
        i+=1
        print(i, " ", line)
        
   
def save_data(file):
    print('Введите данные контакта:')
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    with open(file, 'a', encoding='utf-8') as f:
        f.write(f'{first_name}, {last_name}, {patronymic}, {phone_number}\n')

def search_data(contacts: List[str]):
    # ['Иван, Иванов, Иванович, 123', 'Петр, Иванов, Петрович, 456']
    search_str = input('Введите фамилию для поиска: ')
    founded = []
    # search_idx
    for contact in contacts:
        if search_str.lower() in contact.split(', ')[1].lower():
            founded.append(contact)
    return founded

def move_data(file_name, file_name_new, strnum):
    data = read_file(file_name)
    # Обрабатываем переменную strnum
    try:
        not_int = False
        strnum=int(strnum)
    except:
        return False
    
    if (len(data) < strnum):
        return False
    strnum-=1
    with open(file_name_new, 'a', encoding='utf-8') as f:
        f.write(data[strnum])
    return True
        
def main():
    file_name = 'phone_book.txt'
    file_name_new = 'phone_book_new.txt'
    flag = True
    while flag:
        print('0 - выход')
        print('1 - запись в файл')
        print('2 - показать записи')
        print('3 - найти запись')
        print('4 - перенести данные в другой файл')
        answer = input('Выберите действие: ')
        if answer == '0':
            flag = False
        elif answer == '1':
            save_data(file_name)
        elif answer == '2':
            data = read_file(file_name)
            show_data(data)
        elif answer == '3':
            data = read_file(file_name)
            founded_data = search_data(data)
            show_data(founded_data)
        elif answer == '4':
            strnum = input("Введите номер строки для переноса в {name} :".format(name=file_name_new))
            data = read_file(file_name)
            if move_data(file_name, file_name_new, strnum):
                print("\nСтрока {strnum} перенесена из файла {name_old} в файл {name_new}\n".format(strnum = strnum, name_old = file_name, name_new=file_name_new))
            else:
                print("\nОперация переноса строки завершилась неудачно\n")
    
if __name__ == '__main__':
    main()