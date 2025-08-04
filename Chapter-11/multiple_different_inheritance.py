class first:
    a=1
class second(first):
    b=2
class third(second):
    c=3
n=first()
m=second()
print(n.a)
print(m.a,m.b)
h=third()
print(h.a,h.b,h.c)
