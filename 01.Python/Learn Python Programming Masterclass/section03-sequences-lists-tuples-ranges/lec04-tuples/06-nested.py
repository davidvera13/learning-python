albums = [
    ("Welcome to my nighmare", "Alice Cooper", 1975),
    ("Bad Company", "Bad Company", 1974),
    ("Nightflight", "Budgie", 1981),
    ("More Mayhen", "Imelda May", 2011),
    ("Ride the lightning", "Metallica", 1984),
]

print(len(albums))
print(albums)
print("************")
for album in albums:
    print("Album: {} - Artist: {} - year {}".format(album[0], album[1], album[2]))

print("************")
for album in albums:
    name, artist, year = album
    print("Album: {} - Artist: {} - year {}".format(name, artist, year))

print("************")
for album, artist, year in albums:
    print("Album: {} - Artist: {} - year {}".format(album, artist, year))
