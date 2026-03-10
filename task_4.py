LOGFILE = 'calculator.log'

def last_operations():
    try:
        with open(LOGFILE, 'r') as f:
            lines = f.readlines()
            print("Последние 5 операций:")
            for line in lines[-5:]:
                print(line.strip())
    except FileNotFoundError:
        print("Лог-файл еще не существует.")

def log_operation(expression, result):
    log_line = f"{expression} = {result}\n"
    with open(LOGFILE, 'a') as f:
        f.write(log_line)

def clear_log():
    with open(LOGFILE, 'w') as f:
        pass
    print("Лог-файл очищен.")

def calculator():
    last_operations()
    while True:
        print("\nВыберите действие:\n"
                "1.Выполнить расчет\n"
                "2.Очистить лог-файл\n"
                "3.Выйти")
        choice = input("Введите число: ")

        match choice:
            case '1':
                try:
                    num_1 = float(input("Введите первое число: "))
                    num_2 = float(input("Введите второе число: "))
                    oper = input("Введите операцию (+, -, *, /): ")

                    match oper:
                        case '+':
                            result = num_1 + num_2
                        case '-':
                            result = num_1 - num_2
                        case '*':
                            result = num_1 * num_2
                        case '/':
                            if num_2 == 0:
                                print("Ошибка: деление на ноль.")
                                continue
                            result = num_1 / num_2
                        case _:
                            print("Некорректная операция.")
                            continue

                    print(f"Результат: {result}")
                    log_operation(f"{num_1} {oper} {num_2}", result)

                except ValueError:
                    print("Некорректный ввод чисел.")
            case '2':
                clear_log()
            case '3':
                break
            case _:
                print("Попробуйте снова:")
calculator()