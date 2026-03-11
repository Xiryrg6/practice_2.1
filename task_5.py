import json


def num_int(num):
        num = str(num)
        while not(num.isdigit()):
            num = input("Это не число, попробуйте снова: ")
        return int(num)


def all_books():
    with open("resource/library.json", 'r', encoding="utf-8") as f:
        data = json.load(f)
        for book in data:
            print(f"ID: {book["id"]} Название: '{book["title"]}' Автор: {book["author"]}")
        input("Нажмите Enter, что бы вернуться.")


def search_books(choice):
    with open("resource/library.json", 'r', encoding="utf-8") as f:
        data = json.load(f)
        if choice:
            option = "author"
        else:
            option = "title"
        search = input("\nПоиск: ")
        flag = True
        for book in data:
            if book[option].lower() == search.lower():
                flag = False
                print(f"\nID: {book["id"]}\n" \
                      f"Название: {book["title"]}\n" \
                      f"Автор: {book["author"]}\n" \
                      f"Год: {book["year"]}\n" \
                      f"Статус: {book["available"]}")
        if flag:
            print("\nНичего не найдено.")
        input("\nНажмите Enter, что бы вернуться.\n")


def add_books(title, author, year):
    with open("resource/library.json", 'r', encoding="utf-8") as f:
        data = json.load(f)
    with open("resource/library.json", 'w', encoding="utf-8") as f:
        num_id = 0
        flag = False
        while True:
            num_id += 1
            for book in data:
                if book["id"] == num_id:
                    break
            else:
                flag = True
            if flag:
                break
        book = {"id":num_id, "title":title, "author":author, "year":year, "available": True}
        data.append(book)
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("\nКнига добавлена")


def change_status(num_id):
    with open("resource/library.json", 'r', encoding="utf-8") as f:
        data = json.load(f)
    with open("resource/library.json", 'w', encoding="utf-8") as f:
        for book in data:
            if book["id"] == num_id:
                book["available"] = not book["available"]
                print("\nСтатус изменён.")
                break
        else:
            print("\nID не найден.")
        json.dump(data, f, indent=4, ensure_ascii=False)



def del_books(num_id):
    with open("resource/library.json", 'r', encoding="utf-8") as f:
        data = json.load(f)
    with open("resource/library.json", 'w', encoding="utf-8") as f:
        for book in data:
            if book["id"] == num_id:
                data.remove(book)
                print("\nКнига удалена.")
                break
        else:print("\nID не найден.")
        json.dump(data, f, indent=4, ensure_ascii=False)


def export_list():
    with open("resource/library.json", 'r', encoding="utf-8") as f1:
        data = json.load(f1)
        with open("resource/available_books.txt", 'w', encoding="utf-8") as f2:
            for book in data:
                if book["available"]:
                    f2.write(f"Название: '{book["title"]}' Автор: {book["author"]}\n")
    print("\nФайл со списком экспортирован.")


def menu():
    while True:
        print("\nВыберите действие:\n" \
        "1.Просмотр всех книг\n" \
        "2.Поиск по автору/названию\n" \
        "3.Добавление новой книги\n" \
        "4.Изменение статуса доступности\n" \
        "5.Удаление книги\n" \
        "6.Экспорт списка доступных книг\n" \
        "7.Выход\n")
        choice = input("Введите число: ")

        match choice:
            case "1":
                all_books()
            case "2":
                while True:
                    print("Выберите действие:\n" \
                    "1.Поиск по автору\n" \
                    "2.Поиск по названию\n" \
                    "3.Обратно")
                    choice = input("Введите число: ")
                    match choice:
                        case '1':
                            search_books(True)
                        case '2':
                            search_books(False)
                        case '3':
                            break
            case "3":
                title = input("Название: ")
                author = input("Автор: ")
                year = input("Год: ")
                year = num_int(year)
                add_books(title, author, year)
            case "4":
                num_id = input("ID: ")
                num_id = num_int(num_id)
                change_status(num_id)
            case "5":
                num_id = input("ID: ")
                num_id = num_int(num_id)
                del_books(num_id)
            case "6":
                export_list()
            case "7":
                print("\nВыход.")
                break
menu()