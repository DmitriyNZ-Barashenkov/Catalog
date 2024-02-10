def add_entry(last_name: str, first_name: str, middle_name: str, organization: str, work_phone: str, personal_phone: str):
    with open("phonebook.txt", "a") as file:
        file.write(f"{last_name},{first_name},{middle_name},{organization},{work_phone},{personal_phone}\n")

    print("Новая запись успешно добавлена!")

    # add_entry(): добавляет новую запись в файл "phonebook.txt".
    # Пользователь должен указать фамилию, имя, отчество, организацию, рабочий и мобильный телефон


def edit_entry(last_name: str, new_last_name: str, new_first_name: str, new_middle_name: str, new_organization: str, new_work_phone: str, new_personal_phone: str):
    with open("phonebook.txt", "r+") as file:
        lines = file.readlines()

        for i in range(len(lines)):
            entry = lines[i].split(",")
            if entry[0] == last_name:
                entry[0] = new_last_name
                entry[1] = new_first_name
                entry[2] = new_middle_name
                entry[3] = new_organization
                entry[4] = new_work_phone
                entry[5] = new_personal_phone

                lines[i] = ",".join(entry)

        file.seek(0)
        file.truncate()
        file.writelines(lines)

    print("Запись успешно обновлена!")

    # edit_entry(): изменяет существующую запись в файле "phonebook.txt". Пользователь должен указать фамилию,
    # а затем новые значения фамилии, имени, отчества, организации, рабочего и мобильного телефонов.
