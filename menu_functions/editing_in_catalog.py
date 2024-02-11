# функции добавления новых записей и редактирование старых

# принимает входные параметры: ФИО, организация, телефонные номера
def add_entry(last_name: str, first_name: str, middle_name: str, organization: str, work_phone: str, personal_phone: str):
    # открывает файл "phonebook.txt" в режиме дозаписи (если файл не существует, он будет создан)
    # и записывает новую запись в файл в формате CSV, разделяя каждое поле запятой
    with open("phonebook.txt", "a") as file:
        file.write(f"{last_name},{first_name},{middle_name},{organization},{work_phone},{personal_phone}\n")

    print("Новая запись успешно добавлена!")

    # add_entry(): добавляет новую запись в файл "phonebook.txt".
    # Пользователь должен указать фамилию, имя, отчество, организацию, рабочий и мобильный телефон

# заменяет существующую запись с указанной фамилией на новые значения
def edit_entry(last_name: str, new_last_name: str, new_first_name: str, new_middle_name: str, new_organization: str, new_work_phone: str, new_personal_phone: str):
    # открывает файл "phonebook.txt", считывает все строки,
    with open("phonebook.txt", "r+") as file:
        lines: list[str] = file.readlines()
        # ищет запись с указанной фамилией
        for i in range(len(lines)):
            # проходим по списку
            entry = lines[i].split(",") # разбивает строку lines[i] на подстроки, разделенные запятыми, и сохраняет их в список entry
            # В списке entry по индексу 0 ищем соответствие
            if entry[0] == last_name:
                # заменяет значения полей на новые значения и перезаписывает измененные строки обратно в файл.
                entry[0] = new_last_name
                entry[1] = new_first_name
                entry[2] = new_middle_name
                entry[3] = new_organization
                entry[4] = new_work_phone
                entry[5] = new_personal_phone

                lines[i] = ",".join(entry)

        file.seek(0) # Устанавливает позицию чтения/записи файла в начало файла.
        file.truncate()
        file.writelines(lines) # Записывает строки, указанные в переменной lines, в файл.
                               # Каждая строка будет записана на отдельной строке в файле.

    print("Запись успешно обновлена!")

    # edit_entry(): изменяет существующую запись в файле "phonebook.txt". Пользователь должен указать фамилию,
    # а затем новые значения фамилии, имени, отчества, организации, рабочего и мобильного телефонов.
