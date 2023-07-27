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


# using key to get value
my_car = vehicles['fiesta']
print(my_car)

commuter = vehicles['virago']
print(my_car)


# using get method
learner = vehicles.get('er5')
print(learner)

error = vehicles.get('ER5')
print(error)

exception_thrown = vehicles['ER5']
print(exception_thrown)

