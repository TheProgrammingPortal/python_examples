# importing the library
from cryptography.fernet import Fernet

# generating a key
key = Fernet.generate_key()
print(key)

# encoding string message
msg = "Welcome to Channel".encode()

# creating Fernet class object with the same key
f_obj = Fernet(key)

# encrypting string message with the key
encrpted_msg = f_obj.encrypt(msg)
print(encrpted_msg)

# decrypting string message with the key
decrypted_msg = f_obj.decrypt(encrpted_msg)
print(decrypted_msg)




