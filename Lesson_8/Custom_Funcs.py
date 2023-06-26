import os

def show_contacts(file_name):
    os.system('clear')
    with open(file_name, 'r') as file:
        data = file.readlines()

        for contact in data:
            print(contact, end = '')

    input('\n Нажмите любую кнопку')

def add_contact(file_name):
    os.system('clear')
    with open(file_name, 'a') as file:
        res = ' '
        res += input('Введите фамилию контакта: ') + ' '
        res += input('Введите имя контакта: ') + ' '
        res += input('Введите номер телефона контакта: ') + ' '

        file.write(res + '\n')
    input('Нажмите любую кнопку')

def search_contact(file_name):
    os.system('clear')
    target = input('Введите имя контакта для поиска: ')

    with open(file_name, 'r') as file:
        data = file.readlines()

        for contact in data:
            if target in contact:
                print(contact)
                break
        else:
            print('Контакта с таким именем нет в справочнике :(')
    input('Нажмите любую кнопку')

def drawing():
    os.system('clear')
    print('1 - Показать контакты')
    print('2 - Добавить контакт')
    print('3 - Найти контакт')
    print('4 - Удалить контакт')
    print('5 - Изменить контакт')
    print('6 - Выход')

def delete_contact(file_name):
    os.system('clear')
    show_contacts(file_name) 
    print('Какую по счету запись Вы хотели бы удалить?')
    number_contact = int(input('Введите номер записи: '))
    print(f'Удалить данную запись\n{file_name[number_contact - 1]}')
    file_name = file_name[:number_contact - 1] + file_name[number_contact + 1:]
    with open(file_name, 'w') as file:
        file.write(''.join(file_name))

def change_line(file_name, number_contact):
     answer = input(f"Изменить данную запись\n{file_name[number_contact]}?\nВведите ответ: ")
     while answer != 'да':
         number_contact= int(input('Введите номер записи: '))
         number_contact -= 1
         number_contact = int(input('Введите номер записи: ')) - 1
         print(f"Меняем данную запись\n{file_name[number_contact]}\n")
         name = file_name[number_contact].split('\n')[0]
         surname = file_name[number_contact].split('\n')[1]


def change_line(file_name, number_contact):
        file_name = file_name[:number_contact] + [f'{name};{surname};{phone};{address}'] + \
                       file_name[number_contact + 1:]
        if number_contact + 1 == len(file_name):
             file_name = file_name[:number_contact] + [f'{name}\n{surname}\n{phone}\n{address}\n'] + \
                          file_name[number_contact + 1:]
             file_name = file_name[:number_contact] + [f'{name};{surname};{phone};{address}\n']
        with open(file_name, 'w') as file:
             file.write(''.join(file_name))

def put_data(file_name):
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: '))
        number_journal -= 1
        change_line('file_name, number_contact')

def main(file_name):
    while True:
        os.system('clear')
        drawing()
        user_choice = int(input('Введите номер операции от 1 до 4: '))

        if user_choice == 1:
            show_contacts(file_name)
        elif user_choice == 2:
            add_contact(file_name)
        elif user_choice == 3:
            search_contact(file_name)
        elif user_choice == 4:
            delete_contact(file_name)
        elif user_choice == 5:
            put_data(file_name)
        elif user_choice == 6:
            print('Хорошего дня!')
            return
        
main("/Users/kate/Desktop/Python/test.txt")