from main import a, n, encrypted_message, private_key
from backpack_alg.packing import decrypt

if __name__ == '__main__':
    for i in range(1000):
        if (a * i) % n == 1 and None not in decrypt(message=encrypted_message, n=n, anti_a=i, private_key=private_key):
            print(i)
