import hashlib

print(sorted(hashlib.algorithms_guaranteed))
print(sorted(hashlib.algorithms_available))

# using sha256
python_program = """
for i in range(10):
     print(i)
"""

print(python_program)

print("*********************************")
# for c in python_program.encode('utf-8'):
#     print(c, chr(c))



original_hash = hashlib.sha256(python_program.encode('utf-8'))
print(f"SHA256 { original_hash.hexdigest()}")
print(f"SHA512 { hashlib.sha512(python_program.encode('utf-8')).hexdigest() }")

same_hash = hashlib.sha256(python_program.encode('utf-8'))

if original_hash.hexdigest() == same_hash.hexdigest() :
    print("Values are equals")


print(f"Compare same { original_hash.hexdigest() == same_hash.hexdigest()}")

python_program += "print''Hello World')"
new_hash = hashlib.sha256(python_program.encode('utf-8'))

if original_hash.hexdigest() == new_hash.hexdigest() :
    print("Values are equals")
else:
    print('Oops, content was changed...')

print("*********************************")