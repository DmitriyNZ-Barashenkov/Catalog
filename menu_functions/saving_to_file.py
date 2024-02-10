def save_data(file_name: str):
    with open(file_name, "w") as new_file:
        with open("phonebook.txt", "r") as original_file:
            new_file.writelines(original_file.readlines())

    print("Данные успешно сохранены!")

    # save_data(): сохраняет данные из файла "phonebook.txt" в новый файл, указанный пользователем.