# this is a dictionnary containing vehicles information
vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
}


print("*******************")
for key, value in vehicles.items():
    print(key, value, sep=", ")

# adding item
vehicles["starfighter"] = "Lockeed F-104"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "glider"

print("*******************")
for key, value in vehicles.items():
    print(key, value, sep=", ")
