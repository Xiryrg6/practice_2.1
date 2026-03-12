points = []
point = 0
try:
    with open("resource/students.txt", 'r') as f1:
        with open("resource/result.txt", 'w') as f2:
            for i in f1:
                temp = i.split()
                stud = temp[0]
                for j in range(1, len(temp)):
                    points.append(temp[j])
                for j in points:
                    point += int(j)
                gpa = float(point / len(points))
                if gpa > 4.0:
                    f2.write(stud + ' ' + str(gpa) + "\n")
                points = []
                point = 0

    best_gpa = ["", 0]
    f = open("result.txt", "r")
    for i in f:
        temp = i.split()
        if float(temp[1]) > best_gpa[1]:
            best_gpa = [temp[0], float(temp[1])]
    print(f"Лучший студент: {best_gpa[0]}:{best_gpa[1]}")
except:
    print("Файл не найден.")