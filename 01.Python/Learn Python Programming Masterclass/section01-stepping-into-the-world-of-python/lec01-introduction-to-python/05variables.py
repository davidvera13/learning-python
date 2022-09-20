greeting = "Hello "
name = "John Wick"
age = 24

print(greeting + ' ' + name)
print(age)
# TypeError: can only concatenate str (not "int") to str
# print(name + ' is ' + age)
# convert int to string 
print(name + ' is ' + str(age))

# showing data type: class 'str', class 'int'
print(type(greeting))
print(type(age))

age = '2 years old'
print(age)
print(type(age))

print(name + ' is ' + age)