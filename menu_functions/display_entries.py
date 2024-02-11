# Телефонная книга, функция вызова всех записей и поиска по записям


def display_entries():
    with open("phonebook.txt", "r") as file: # открываем файл для чтения
        lines = file.readlines()
        # принимает на вход номер страницы (page_number) и размер страницы (page_size)
        page_size: int = 10  # количество строк на странице
        page_number: int = 1
        # позволяет показывать информацию из списка lines постранично

        while True:
            # вычисляет индексы начального (start_index) и конечного (end_index) элементов на данной странице
            start_index = (page_number - 1) * page_size
            end_index = page_number * page_size

            for i in range(start_index, min(end_index, len(lines))):
                print(lines[i])
            # выводит элементы списка с индексами от start_index до end_index или до конца списка (len(lines)) при условии,
            # что end_index меньше или равен длине списка.
            if end_index >= len(lines):
                break

            user_input = input("Нажмите Enter для перехода на следующую страницу или «q», чтобы выйти: ")
            if user_input == "q":
                break
            # номер страницы увеличивается на 1 (page_number += 1), и процесс повторяется для следующей страницы
            page_number += 1

    # display_entries(): выводит все записи из файла "phonebook.txt" на экран,
    # разбивая их на страницы по 10 записей. Пользователь может пролистывать страницы и выйти из просмотра.




def search_entries(last_name: str="", first_name: str="", organization: str=""):
    # считывает содержимое файла "phonebook.txt"
    with open("phonebook.txt", "r") as file:
        # считывает все строки из файла и возвращает список из всех считанных строк
        lines: list[str] = file.readlines()
        # проверяет каждую запись на соответствие заданным параметрам поиска (фамилии, имени и организации)
        for line in lines:
            entry: list[str] = line.split(",")
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

