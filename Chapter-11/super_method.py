class first:
    def __init__(self):
        print("my name is nothing")
    a=1
class second(first):
    def __init__(self):
        print("my name is wow")
    b=2
class third(second):
    def __init__(self):
        super().__init__()
        print("my name is nothing")
    c=3
n=first()
# m=second()
# print(n.a)
# print(m.a,m.b)
h=third()
print(h.a,h.b,h.c)
