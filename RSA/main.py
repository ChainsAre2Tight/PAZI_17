from RSA.algorithms import easy_phi, check_primes, reverse_modulo_a, easy_reverse_modeulo


def generate_keys(p: int, q: int, e: int = 3) -> dict:
    if not check_primes(p, q):
        raise ValueError('P and Q must be coprime')
    n = p * q
    phi_n = easy_phi(p, q)
    if not (1 < e < phi_n and check_primes(e, phi_n)):
        raise AttributeError('E is incorrect')
    d = easy_reverse_modeulo(a=e, m=phi_n)
    return {
        'public_key': (e, n),
        'private_key': (d, n),
    }


def encrypt_integer(message: int, public_key: tuple[int, int]) -> int:
    e, n = public_key
    encrypted_message = (message ** e) % n
    return encrypted_message


def decrypt_integer(encrypted_message: int, private_key: tuple[int, int]) -> int:
    d, n = private_key
    decrypted_message = (encrypted_message ** d) % n
    return decrypted_message


def encrypt_message(message: list[int], public_key: tuple[int, int]) -> list[int]:
    encrypted_message = [encrypt_integer(integer, public_key=public_key) for integer in message]
    return encrypted_message


def decrypt_message(message: list[int], private_key: tuple[int, int]) -> list[int]:
    decrypted_message = [decrypt_integer(integer, private_key=private_key) for integer in message]
    return decrypted_message
