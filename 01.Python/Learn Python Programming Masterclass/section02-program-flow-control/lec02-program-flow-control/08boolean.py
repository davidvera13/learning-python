day = "Monday"
temperature = 30
raining = True

# AND > OR
if day == "Saturday" and temperature > 27 and not raining:
    print("Go swimming")
else:
    print("GO learning Python...")

print("-" * 60)
if day == "Monday" and temperature > 27 or not raining:
    print("Go swimming")
else:
    print("GO learning Python...")

print("-" * 60)
if day == "Saturday" and temperature > 27 or not raining:
    print("Go swimming")
else:
    print("GO learning Python...")

print("-" * 60)
# enhance reading and understanding
if (day == "Saturday" and temperature > 27) or not raining:
    print("Go swimming")
else:
    print("GO learning Python...")