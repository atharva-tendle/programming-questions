# get number of students and the subjects
n, x = map(int, input().split())

# create a list of subject grades
subjects = []
# add the grades for all subjects
for _ in range(x):
    subjects.append(list(map(float, input().split())))

# return the average grades for each student
for s_grades in zip(*subjects):
    print(sum(s_grades)/len(s_grades))
