#write a program to fill in a letter template given below with name and date.

name = '''Dear (nme),
You are selected
(Date)'''

print(name.replace("(nme)","atul").replace("(Date)","24 september 2022"))

print(name.replace("(nme)","Atul").replace("(Date)","24 september 2025"))