
"""
The program is trying to display student grades on a final exam.
A text file called "Final.txt" contains 24 students' grades
It is required to calculate number of grades, the average grade and the grades that are above the average
Then print out output, "Number of grades", "Average grade", "Percentage of grades above average".
"""


"""
infile = open("fileName", 'r')
L = [line.rstrip() for line in infile]
infile.close
input: student's grades
list of grades = len(grades)
average = sum of grades / amount of grades in the list

if grade > average:
"Percentage of grades above average: {0:.2f}%"

main

"""

infile = open("Final.txt", 'r')
grades = [line.rstrip() for line in infile]
infile.close()
for i in range(len(grades)):
    grades[i] = int(grades[i])
average = sum(grades) / len(grades)
num = 0 
for grade in grades:
    if grade > average:
        num += 1

print("Number of grades:", len(grades))
print("Average grade:", average)
print("Percentage of grades above average: {0:.2f}%".format(100 * num / len(grades)))

