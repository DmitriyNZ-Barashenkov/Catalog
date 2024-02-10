# Телефонная книга


def display_entries():
    with open("phonebook.txt", "r") as file: # открываем файл для чтения
        lines = file.readlines()
        page_size: int = 10  # количество строк на странице
        page_number: int = 1


        while True:
            start_index = (page_number - 1) * page_size
            end_index = page_number * page_size

            for i in range(start_index, min(end_index, len(lines))):
                print(lines[i])

            if end_index >= len(lines):
                break

            user_input = input("Нажмите Enter для перехода на следующую страницу или «q», чтобы выйти: ")
            if user_input == "q":
                break

            page_number += 1

    # display_entries(): выводит все записи из файла "phonebook.txt" на экран,
    # разбивая их на страницы по 10 записей. Пользователь может пролистывать страницы и выйти из просмотра.




def search_entries(last_name="", first_name="", organization=""):
    with open("phonebook.txt", "r") as file:
        lines = file.readlines()

        for line in lines:
            entry = line.split(",")
            if last_name and entry[0] != last_name:
                continue

            if first_name and entry[1] != first_name:
                continue

            if organization and entry[3] != organization:
                continue

            print(line)

    print("Поиск завершен!")
    # search_entries(): выполняет поиск записей в файле "phonebook.txt" по заданным критериям фамилии,
    # имени и организации. Выводит соответствующие записи на экран

