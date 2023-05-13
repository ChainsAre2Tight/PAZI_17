from backpack_alg.packing import encrypt, decrypt, check_sequence, create_public_key
from encoding import encode_list, decode
from encoding import alphabet_base64, alphabet_ascii, alphabet_unicode
from RSA.algorithms import extended_gcd

sequence_z_6 = [3, 12, 24, 48, 96, 192]
sequence_z_8 = [5, 11, 22, 44, 88, 176, 352, 704]
sequence_z_16 = [2, 3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144, 12288, 24576, 49152]

# encoding = alphabet_base64
# encoding = alphabet_ascii
encoding = alphabet_unicode

message = 'Botnikov'

if encoding == alphabet_base64:
    a = 79
    n = 975
    anti_a = 469
    private_key = sequence_z_6
elif encoding == alphabet_ascii:
    a = 173
    n = 1976
    anti_a = 1245
    private_key = sequence_z_8
elif encoding == alphabet_unicode:
    a = 13595
    n = 178948
    anti_a = 29919
    private_key = sequence_z_16
else:
    raise NotImplementedError

if __name__ == '__main__':
    print(check_sequence(sequence_z_6))
    print(a, n, extended_gcd(a, n))

public_key = create_public_key(private_key=private_key, a=a, n=n)
encoded_message = encode_list(encoding, message=message)
encrypted_message = encrypt(message=encoded_message, public_key=public_key)
decrypted_message = decrypt(message=encrypted_message, n=n, anti_a=anti_a, private_key=private_key)
decoded_message = decode(alphabet=encoding, encoded_message=''.join(decrypted_message), block=len(private_key))

if __name__ == '__main__':
    print('Открытый ключ', public_key)  # [237, 948, 921, 867, 759, 543]
    print(f'Закодированное сообщение',
          encoded_message)  # ['000001', '101000', '101101', '100111', '100010', '100100', '101000', '101111']
    print('Зашифрованное сообщение', encrypted_message)  # [543, 1158, 2568, 2406, 996, 1104, 1158, 3327]
    print('Расшифрованное сообщение',
          decrypted_message)  # ['000001', '101000', '101101', '100111', '100010', '100100', '101000', '101111']
    print('Раскодированное сообщение', decoded_message)  # Botnikov
    pass
