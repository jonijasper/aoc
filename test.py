a = [1,2,3]
b = a.copy()
a.pop()
print(a)
print(b)
a += b
print(a)