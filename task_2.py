points = []
point = 0
f1 = open("students.txt", 'r')
f2 = open("result.txt", 'w')
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
f2.close()
f1.close()

best_gpa = ["", 0]
f = open("result.txt", "r")
for i in f:
    temp = i.split()
    if float(temp[1]) > best_gpa[1]:
        best_gpa = [temp[0], float(temp[1])]
print(f"Лучший студент: {best_gpa[0]}:{best_gpa[1]}")