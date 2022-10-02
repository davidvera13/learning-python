# data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191, 350, 360]

#  testing with only low data to remove
# data = [4, 5, 1104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191]

#  testing with only high data to remove
# data = [104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191, 350, 360]

#  testing with no data to remove
# data = [104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191]

# testing with no value in range: the code below work only with sorted values
# data = [1104, 2105, 3110, 5120, 5130, 6130, 7150,
#         -160, -170, -183, -185, -187, -188, -191]
# data.sort()

# data = [1104, 1105, 1110, 1120, 1130, 1130, 1150,
#         1160, 1170, 1183, 1185, 1187, 1188, 1191]

# testing empty list
data = []

min_valid = 100
max_valid = 200

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


