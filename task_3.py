import csv

FILENAME = 'resource/products.csv'

def read_data():
    goods = []
    try:
        with open(FILENAME, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['Цена'] = float(row['Цена'])
                row['Количество'] = int(row['Количество'])
                goods.append(row)
    except FileNotFoundError:
        print("Файл не найден.")
    return goods

def save(goods):
    with open(FILENAME, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['Название', 'Цена', 'Количество']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for product in goods:
            product['Цена'] = str(product['Цена'])
            product['Количество'] = str(product['Количество'])
            writer.writerow(product)

def add(goods):
    name = input("Введите название товара: ")
    price = float(input("Введите цену: "))
    count = int(input("Введите количество: "))
    new_product = {'Название': name, 'Цена': price, 'Количество': count}
    goods.append(new_product)
    print("Товар добавлен.")

def search(goods):
    name = input("Введите название товара для поиска: ")
    flag = False
    for product in goods:
        if product['Название'].lower() == name.lower():
            print(f"\nНайден товар: {product['Название']}, Цена: {product['Цена']}, Количество: {product['Количество']}")
            flag = True
            break
    if not flag:
        print("\nТовар не найден.")

def count(goods):
    summ = 0
    for product in goods:
        summ += product['Цена'] * product['Количество']
    print(f"\nОбщая стоимость всех товаров на складе: {summ}")

def menu():
    goods = read_data()
    while True:
        print("\nВыберите действие:\n"
                "1. Добавить товар\n"
                "2. Поиск товара по названию\n"
                "3. Расчет общей стоимости\n"
                "4. Сохранить и выйти")
        choice = input("Введите номер действия: ")

        match choice:
            case '1':
                add(goods)
            case '2':
                search(goods)
            case '3':
                count(goods)
            case '4':
                save(goods)
                print("\nДанные сохранены. Выход.")
                break
            case _:
                print("\nНекорректный ввод, попробуйте снова.")
menu()