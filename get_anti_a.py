from main import a, n, encrypted_message, private_key
from backpack_alg.packing import decrypt


def get_anti_a(r: int = 1000):
    for i in range(r):
        if (a * i) % n == 1:
            decrypted = decrypt(message=encrypted_message, n=n, anti_a=i, private_key=private_key)
            if None not in decrypted:
                print(i)


if __name__ == '__main__':
    get_anti_a(1000000)
