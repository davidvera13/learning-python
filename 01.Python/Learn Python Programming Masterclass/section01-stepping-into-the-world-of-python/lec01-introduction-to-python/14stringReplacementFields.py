# replacement fields
age = 24
print("my age is " + str(age) + " years old")

print("my age is {0} years old".format(age))

print("there are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(31, 'jan', 'mar', 'may', 'jul', 'aug', 'oct', 'dec'))

print('Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May {2}, Jun: {1}, Jul: {2}, Aug: {1}, Sep: {1}, Oct: {2}, Nov: {1}, Dec: {2}'.format(28, 30, 31))

print("""
Jan: {2}, 
Feb: {0}, 
Mar: {2}, 
Apr: {1}, 
May {2}, 
Jun: {1}, 
Jul: {2}, 
Aug: {1}, 
Sep: {1}, 
Oct: {2}, 
Nov: {1}, 
Dec: {2}""".format(28, 30, 31))