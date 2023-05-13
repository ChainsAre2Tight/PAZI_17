def pack(s_max: int, sequence: list) -> tuple[bool, str, int]:
    backpack = list()
    is_included = list()
    s_cur = s_max
    for item in sorted(sequence, reverse=True):
        if s_cur - item >= 0:
            s_cur -= item
            backpack.append(item)
            is_included.append('1')
        else:
            is_included.append('0')
    is_included = ''.join(reversed(is_included))  # binary string
    success = s_cur == 0  # можно ли упаковать рюкзак
    return success, \
        is_included if success else None, \
        sum(backpack) if success else None


def create_public_key(private_key: list, a: int, n: int):
    open_key = private_key.copy()
    for i in range(len(open_key)):
        open_key[i] = (open_key[i] * a) % n
    return open_key


def encrypt(message: list, public_key: list):
    encrypted_message = list()

    for item in message:
        backpack = 0
        for index in range(len(item)):
            backpack += public_key[index] * int(item[index])
        encrypted_message.append(backpack)
    return encrypted_message


def decrypt(message: list, n: int, anti_a: int, private_key: list):
    decrypted_message = list()

    for item in message:
        backpack = (item * anti_a) % n
        result_item = pack(s_max=backpack, sequence=private_key)[1]
        decrypted_message.append(result_item)

    return decrypted_message


if __name__ == '__main__':
    print(decrypt(
        message=[155, 365, 558, 155, 924, 1239, 470],
        n=420,
        anti_a=271,
        private_key=[2, 3, 6, 13, 27, 52, 105, 210]
    ))


def check_sequence(sequence: list) -> bool:
    for i in range(1, len(sequence)):
        if sequence[i] <= sum(sequence[:i]):
            return False
    return True


def simple_create_sequence(start: int, length: int, step: int) -> list:
    sequence = [start]
    for item in range(length - 1):
        sequence.append(sum(sequence) + step)
    return sequence


if __name__ == '__main__':
    # print(simple_create_sequence(3, 6, 9))
    # print(simple_create_sequence(5, 8, 6))
    print(simple_create_sequence(2, 16, 1))
