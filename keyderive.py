from hashlib import pbkdf2_hmac
dk = pbkdf2_hmac('sha256', b'password', b'bad salt' * 2, 16)
print(dk.hex())