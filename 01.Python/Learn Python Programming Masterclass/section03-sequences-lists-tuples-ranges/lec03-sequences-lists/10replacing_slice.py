computer_parts = [
    'computer', 'monitor', 'keyboard', 'mouse', 'mouse mat'
]
print(computer_parts)
computer_parts[3] = 'trackball'
print(computer_parts)

computer_parts[3] = 'mouse'
print(computer_parts[3:])

# we have trackball splitted
computer_parts[3:] = 'trackball'
print(computer_parts)


computer_parts = [
    'computer', 'monitor', 'keyboard', 'mouse', 'mouse mat'
]
computer_parts[3:] = ['trackball']
print(computer_parts)