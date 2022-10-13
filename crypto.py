from cryptography.fernet import Fernet

def encrypt(data, key):
    f = Fernet()
    return f.encrypt(key)