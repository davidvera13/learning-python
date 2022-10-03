a = b = c = d = e = f = 42
print(c)
print(a)
print("*****************")

x, y, z = 1, 2, 31
print(x)
print(y)
print(z)

print("*****************")
print("Unpacking tuple")
# data is a typle
data = 1, 2, 31
x, y, z = data
print(x)
print(y)
print(z)

print("*****************")
print("Unpacking list")
data_list = [1, 2, 31]
p, q, r = data_list
print(p)
print(q)
print(r)

print("*****************")
print("Unpacking list with error")
# ValueError: too many values to unpack (expected 3)
data_list2 = [1, 2, 314]
data_list2.append(0)
s, t, u = data_list2


