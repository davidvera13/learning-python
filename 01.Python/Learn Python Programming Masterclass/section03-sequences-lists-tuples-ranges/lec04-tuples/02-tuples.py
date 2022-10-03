welcome = "Welcome to my nighmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhen", "Imelda May", 2011
metallica = "Ride the lightning", "Metallica", 1984

print(metallica)

# we can use index on tuples
print("> " + metallica[0])
print("> " + metallica[1])
print("> " + str(metallica[2]))

# Tuples don't support item assignment
# tuples are immutable => less memory than list
# metallica[0] = "Master of Puppets"

# tuples can be converted to list and lists are mutable
metallica_list = list(metallica)
metallica_list[1] = "Master of Puppets"
metallica_list[2] = 1986
print(metallica_list)
