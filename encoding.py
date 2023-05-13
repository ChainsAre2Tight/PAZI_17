alphabet = 'ABCDEFGHIJKLMNOPQRTSUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'


def base10_to_binary_of_expected_length(num: int, length: int):
    bin_num = str(bin(num))[2:]
    if len(bin_num) > length:
        raise ValueError(f'''Given integer ({
        num}) is to big to be converted to binary of length {length} ({len(bin_num)} > {length})''')
    result = '0' * (length - len(bin_num)) + bin_num
    return result


alphabet_base64 = {
    alphabet[i]: base10_to_binary_of_expected_length(i, 6) for i in range(len(alphabet))
}

alphabet = r'''ABCDEFGHIJKLMNOPQRTSUVWXYZ|\]^_'abcdefghijklmnopqrstuvwxyz'''

alphabet_ascii = {
    alphabet[i]: base10_to_binary_of_expected_length(i + 65, 8) for i in range(len(alphabet))
}

alphabet_unicode = {
    chr(i): base10_to_binary_of_expected_length(i, 16) for i in range(48, 123)
}


def encode(alphabet: dict, message: str) -> str:
    return ''.join(alphabet[i] for i in message)
    # return tuple(alphabet[i] for i in message)

def encode_list(alphabet: dict, message: str) -> list:
    return [alphabet[i] for i in message]


def decode(alphabet: dict, encoded_message: str, block: int) -> str:
    message = ''
    split_encoded_message = [encoded_message[i:i + block] for i in range(0, len(encoded_message), block)]
    for item in split_encoded_message:
        for letter, binary in alphabet.items():
            if binary == item:
                message = message + letter
                # print(letter)
                break
    return message


if __name__ == '__main__':
    # print(encode(alphabet_base64, 'Botnikov'))
    print(decode(alphabet_base64, encoded_message=encode(alphabet_base64, 'Botnikov'), block=6))
