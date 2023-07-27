# this is a dictionnary containing vehicles information
# note: for triumph, value is changed, not the order !!!
# key should be unique
vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
    'learjet': '',
}
# 'roadster': 'Triumph Street Triple'

print("*******************")
# adding
vehicles["learjet"] = "Bombardier Learjet 75"
# update value
vehicles['virago'] = "Yamaha XV535"


print("*******************")
for key, value in vehicles.items():
    print(key, value, sep=", ")


# delete value
del vehicles['virago']
# KeyError: 'willCrash'
# del vehicles['willCrash']

print("*******************")
# should throw error: if we use default value, it works
result = vehicles.pop('willCrash', None)
print(result)

result = vehicles.pop('willCrash', 'Oops value not found')
print(result)

plane = vehicles.pop('learjet')
print(plane)

bike = vehicles.pop('Tenere', 'Not found')
print(bike)

print("*******************")
for key, value in vehicles.items():
    print(key, value, sep=", ")



