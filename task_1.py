list_1 = ["2", "230", "45 48", "28", "67"]
count_str = 0
count_words = 0
max_len_words = ""

with open("text.txt", 'w') as f:
    for i in list_1:
        f.write(i + "\n")

with open("text.txt", 'r') as f:
    for i in f:
        count_str += 1
        for j in range(len(i.split())):
            count_words += 1
        if len(i) > len(max_len_words):
            max_len_words = i

print("Список: " + str(list_1))
print(f"Количество строк:{count_str}\n"
      f"Количество слов:{count_words}\n"
      f"Самая длинная строка:{max_len_words}")