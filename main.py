import numpy as np
#rows:students,columns,subjects
marks = np.array([
    [88,92,85,78],
    [76,85,90,89],
    [92,88,95,94],
    [90,95,91,99]
])

#Task 1: total & Average marks per student

total_marks = np.sum(marks,axis = 1)
average_marks = np.mean(marks,axis = 1)

for i in range(len(marks)):
    print(f"student{i+1}: total = {total_marks[i]}, Average = {average_marks[i]}")

#Task 2: find Topper and Lowest Scorer

topper = np.argmax(total_marks)
lowest = np.argmin(total_marks)

print(f"\nTopper: student {topper + 1} with total marks {total_marks[topper]}")
print(f"Lowest Scorer: Student {lowest + 1} with total marks {total_marks[lowest]}")

#Task 3: Students Scoring Above 90 in any subject
above_90 = np.any(marks > 90 , axis = 1)

student_above_90 = np.where(above_90)[0]+1

print(f"\nstudents who scored above 90 in any subject:{student_above_90}")

#Task 4: Subject wise Average Marks
subject_avg = np.mean(marks,axis =0)

subjects = ['math','science','english','computer']

for i,avg in enumerate(subject_avg):
    print(f'Average in {subjects[i]}: {avg}')

