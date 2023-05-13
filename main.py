from backpack_alg.packing import encrypt, decrypt, check_sequence, create_public_key
from encoding import encode_list, decode
from encoding import alphabet_base64
from RSA.algorithms import extended_gcd

sequence_z_6 = [3, 12, 24, 48, 96, 192]
sequence_z_8 = [5, 11, 22, 44, 88, 176, 352, 704]
sequence_z_16 = [2, 3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144, 12288, 24576, 49152]

a = 79
n = 975
anti_a = 469
message = 'Botnikov'
private_key = sequence_z_6
encoding = alphabet_base64

if __name__ == '__main__':
    print(check_sequence(sequence_z_6))
    print(a, n, extended_gcd(a, n))

public_key = create_public_key(private_key=private_key, a=a, n=n)
encoded_message = encode_list(encoding, message=message)
encrypted_message = encrypt(message=encoded_message, public_key=public_key)
decrypted_message = decrypt(message=encrypted_message, n=n, anti_a=anti_a, private_key=private_key)
decoded_message = decode(alphabet=encoding, encoded_message=''.join(decrypted_message), block=len(private_key))

if __name__ == '__main__':
    print(public_key)  # [237, 948, 921, 867, 759, 543]
    print(encoded_message)  # ['000001', '101000', '101101', '100111', '100010', '100100', '101000', '101111']
    print(encrypted_message)  # [543, 1158, 2568, 2406, 996, 1104, 1158, 3327]
    print(decrypted_message)  # ['000001', '101000', '101101', '100111', '100010', '100100', '101000', '101111']
    print(decoded_message)  # Botnikov
    pass
