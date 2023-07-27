data = [
    ("orange", "a sweet, orange, citrus fruit"),
    ("apple", "good for making cider"),
    ("lemon", "a sour, yellow citrus fruit"),
    ("grape", "a small, sweet fruit growing in bunches"),
    ("melon", "sweet and juicy"),
]

print(data)
# create a list of 10 items
keys = [""] * 10
print(keys)
values = keys.copy()


def simple_hash(s: str) -> int:
    """A ridiculously simple hashing function"""
    basic_hash = ord(s[0])
    return basic_hash % 10


def get(k: str) -> str:
    """Retuen the value for a key, or None if the key doesn't exist"""
    hash_code = simple_hash(k)
    if values[hash_code]:
        return values[hash_code]
    else:
        return None



for key, value in data:
    h = simple_hash(key)
    adv_hash = hash(key)
    print(key,h, adv_hash)
    keys[h] = key
    values[h] = value


print(keys)
print(values)

value = get("lemon")
print(value)

# collision
value = get("banana")
print(value)
value = get("cat")
print(value)

# no collidion ... returns None
value = get("d")
print(value)