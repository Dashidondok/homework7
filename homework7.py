grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#print(len(grades))


students_sort = sorted(students)
students_list = list(students_sort)
#print(students_list)

for i in range(len(grades)):
    grades[i] = sum(grades[i])/len(grades[i])

students = {}
for i in range(len(students_list)):
    students[students_list[i]] = grades[i]
print(students)