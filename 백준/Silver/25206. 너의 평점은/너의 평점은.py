rate_dir = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}

sum = 0
grade_sum = 0

for i in range(20):
    subject, grade, rate = input().split()

    if rate == "P":
        continue

    sum += rate_dir[rate] * float(grade)
    grade_sum += float(grade)

print(sum / grade_sum)