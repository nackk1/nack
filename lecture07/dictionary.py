student = {'name' : 'Alice', 'age' : 26, 'major' : 'computer science'}

print(student.key())
print(student.value())
print(student.items())

print(student.get("name"))
print(student.get("grade", "Not Found"))

major = student.pop("major")
print(major)
print(student)

last_item = student.popitem()
print(last_item)
print(student)

student.clear()
print(student)


