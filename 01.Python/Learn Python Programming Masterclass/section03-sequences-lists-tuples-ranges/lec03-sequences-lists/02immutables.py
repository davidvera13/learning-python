# because boolean are immutable,we were not able to change the value of true
# to false. Instead, the variable is recreated to a new value => id is different
result = True
another_result = result
print(id(result))
print(id(another_result))
result = False
print(id(result))
print(id(another_result))


# iùmutable
print()
output = "Correct"
another_output = output

print(id(output))
print(id(another_output))
output += "ish"
print(id(output))
print(id(another_output))
