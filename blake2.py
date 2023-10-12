from hashlib import blake2b
items = [b'Hello', b' ', b'world']
h = blake2b()
for item in items:
	h.update(item)
print(h.hexdigest())