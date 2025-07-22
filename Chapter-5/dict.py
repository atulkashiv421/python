marks = {
    "harry" : 45,
    "subham" : 46,
    "atul": 100
}

print(type(marks))
print(marks["atul"])
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"harry" : 99})
print(marks)
print(marks.get(("harry")))
marks.popitem()
print(marks)
