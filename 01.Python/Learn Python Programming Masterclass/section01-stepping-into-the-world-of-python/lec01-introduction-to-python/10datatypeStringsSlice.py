parrot = "Norwegian Blue"
print(parrot)

# start, stop, step
print(parrot[0:6])  # take substring from char 0 to 5th (6th is not included)
print(parrot[3:5])  # 2 chars (5-3) => we
print(parrot[0:9])  # Norwegian
print(parrot[:9])   # Norwegian: default start value is 0

print(parrot[10:14])  # Blue
print(parrot[10:])    # Blue


print(parrot[:6] + parrot[6:])  # Norwegian Blue
print(parrot[:])

# nothing printing...
print(parrot[-4:2])

print(parrot[-4:-2])  # bl
print(parrot[-4:12])  # bl

