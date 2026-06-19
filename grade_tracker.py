#Mini project after Module 5
#Challenge: Making a lightweight, local database using a 2D array to dynamically store, mutate, and mathematically analyze student performance records.

classroom_db = [
    ["Alice", 85],
    ["Bob", 92],
    ["Charlie", 78]
]

#Action: Takes the existing database and adds a new [name, grade] sub-list to the end of it.
new_name = ["Duke", 87]
classroom_db.append(new_name)
print(classroom_db)

#Action: Uses direct index reassignment to overwrite the grade of a specific student.
classroom_db[3][1] = 91
print(classroom_db)

#Action: Extracts only the grades from the 2D array into a temporary flat list. Then, uses global functions (sum, len, max, min) to calculate the class average, the highest score, and the lowest score.
grade_1 = classroom_db[0][1]
grade_2 = classroom_db[1][1]
grade_3 = classroom_db[2][1]
grade_4 = classroom_db[3][1]
new_list = [grade_1, grade_2, grade_3, grade_4]
average_score = (sum(new_list) / len(new_list))
print(f"The average score of the class is: {average_score}")
print(f"The maximum score of the class is: {max(new_list)}")
print(f"The minimum score of the class is: {min(new_list)}")
