# Прикрутить графику, можно через customtkinter

from menu_functions import *


def main():
    while True:
        print("Телефонный каталог:")
        print("1. Вывести все контакты")
        print("2. Внести новый контакт")
        print("3. Изменить контакт")
        print("4. Найти контакт")
        print("5. Сохранить в новый файл")
        print("0. Выход")
# запускаем бесконечный цыкл whil True, пока не вернется значение Fals,
# это реализация меню в терминале
        choice = input("Выберете пункт меню: ")
        if choice == "1":
            display_entries()
        elif choice == "2":
            last_name = input("Укажите фамилию: ")
            first_name = input("Укажите имя: ")
            middle_name = input("Укажите очество: ")
            organization = input("Укажите организацию: ")
            work_phone = input("Укажите рабочий телефон: ")
            personal_phone = input("Укажите мобильный телефон: ")
            add_entry(last_name, first_name, middle_name, organization, work_phone, personal_phone)
        elif choice == "3":
            last_name = input("Enter last name of the entry to edit: ")
            new_last_name = input("Введите новую фамилию: ")
            new_first_name = input("Введите новое имя: ")
            new_middle_name = input("Введите новое отчество: ")
            new_organization = input("Введите новое название организации: ")
            new_work_phone = input("Введите новый рабочий телефон: ")
            new_personal_phone = input("Введите новый мобильный телефон: ") + "\n"
            edit_entry(last_name, new_last_name, new_first_name, new_middle_name, new_organization, new_work_phone,
                       new_personal_phone)
        elif choice == "4":
            last_name = input("Введите фамилию (оставьте пустым, если не ищете по фамилии): ")
            first_name = input("Введите имя (оставьте пустым, если не ищете по имени): ")
            organization = input("Введите организацию (оставьте пустым, если не ищете по организации): ")
            search_entries(last_name, first_name, organization)
        elif choice == "5":
            file_name = input("Введите имя файла для сохранения данных:")
            save_data(file_name)
        elif choice == "0":
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте еще раз.")

    # main(): главная функция, которая отображает меню и позволяет пользователю выбирать действия.


if __name__ == "__main__":
    main()
