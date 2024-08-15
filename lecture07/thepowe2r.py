attendance_week = [
    ["Alice","Bob","Charlie","David"],
    ["Alice","Charlie","David"],
    ["Alice","Bob","David"],
    ["Alive","David","Eve"],
    ["Bob,"charlie","David"]
]

attendance_sets = [set(day) for day in attendance_week]
print(attendance_set)

present_every_day = set.intersection(*attendance_set)
print("Present every day: ", present_every_day)


all_studens = set.union(*attendance_set)
absent_at_least_one_day = all_studens - present_every_day
print("Absent at least one day: ", absent_at_least_one_day)

firs_day_present = attendance_sets[0]

last_day_present = attendance_sets[-1]
frist_day_but_not_last = list(firs_day_present - last_day_present)
print("Present on first day but absent on last day: ", frist_day_but_not_last)

unique_students_count = len(all_students)
print("TOtal unique students: ", unique_students_count)