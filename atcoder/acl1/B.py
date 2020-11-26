def make_prime_factors_compress(n: int) -> list:
    prime_factors = []
    for k in range(2, int(n ** 0.5) + 1):
        cnt = 0
        while n % k == 0:
            cnt += 1
            n = n // k
        if cnt != 0:
            prime_factors.append((k, cnt))
    if n != 1:
        prime_factors.append((n, 1))
    return prime_factors


def extended_gcd(a, b):
    """ax + by = gcd(a, b)の整数解(x, y)を求める"""
    if b == 0:
        return a, 1, 0
    else:
        g, y, x = extended_gcd(b, a % b)
        y -= (a // b) * x
        return g, x, y


n = int(input())
primes = make_prime_factors_compress(n)


if n == 1:
    print(1)
    exit()

if primes[0][0] == 2:
    primes[0] = (primes[0][0], primes[0][1] + 1)
else:
    primes.append((2, 1))

m = len(primes)
ans = 10 ** 20
for bit_state in range(1 << m):
    k0 = 1
    k1 = 1
    for i in range(m):
        pri, cnt = primes[i]
        if (bit_state >> i) & 1:
            k1 *= pri ** cnt
        else:
            k0 *= pri ** cnt
    if k1 == 1 or k0 == 1:
        continue
    _, a, b = extended_gcd(k1, k0)
    ans = min(ans, abs(k0 * b))

print(ans)