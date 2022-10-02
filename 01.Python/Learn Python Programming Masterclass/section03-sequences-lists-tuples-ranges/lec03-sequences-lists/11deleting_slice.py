data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]
print(data)
# remove some data
del data[0:2]
print(data)

del data[14:]
print(data)

print("*****************************")
data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]
print(data)

min_valid = 100
max_valid = 200

# objective : remove values which are not in 100...200 range
# this code is not working: issue with index
for index, value in enumerate(data):
    if (value > min_valid) or (value > max_valid):
        del data[index]

print(data)

print("*****************************")
data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]

# process low values first
stop = 0
for index, value in enumerate(data):
    if value > min_valid:
        stop = index
        break

print(stop)
del data[:stop]

print(data)

# process high values in the list
start = 0
for index in range(len(data) - 1, -1, -1):
    # print(index)
    if data[index] <= max_valid:
        # wa heve the index of the last item to keep,
        # set start tp the position of the first item to delate: 1 elt
        # after the index
        start = index + 1
        break

print(start)
del data[start:]
print(data)
