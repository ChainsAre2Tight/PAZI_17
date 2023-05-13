def Eucledes_algorithm(a, b):
    r_list = sorted([a, b], reverse=True)
    i = 0
    while True:
        temp = r_list[i]
        while temp >= 2 * r_list[i + 1]:
            temp -= r_list[i + 1]
        temp -= r_list[i + 1]
        if temp == 0:
            break
        r_list.append(temp)
        i += 1
    return r_list[-1]


def phi(n: int) -> int:
    result = n
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            while not n % i:
                n /= i
            result -= result / i
    if n > 1:
        result -= result / n
    return result


def easy_phi(p, q):
    return (p - 1) * (q - 1)


def extended_gcd(a: int, b: int):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, (old_t, old_s), (t, s)


def reverse_modulo_a(a, m):
    result = extended_gcd(a, m)
    return max(result[1])


def easy_reverse_modeulo(a, m):
    result = (2 * m + 1) / a
    return result


def check_primes(a: int, b: int) -> bool:
    return extended_gcd(a, b)[0] == 1
