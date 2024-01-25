RSA Factoring Challenge: Algorithm and Scripting
Prime Factorization, How does HTTPS provide security and Why RSA
Files: factors, rsa
General Understanding of RSA

1. Twin prime numbers: difference between them is 2
(2 being the smallest and only even prime number)
2. Semi-prime numbers: their divisors/factors are 1, itself,
and either one prime number (squares of prime numbers: 25 (1, 5, 25),
49 (1, 7, 49), 9(1, 3, 9), 4(1, 2, 4), 121(1, 11, 121), etc)
or different prime numbers (91 (1, 7, 13, 91), 85 (1, 5, 17, 85),
77 (1, 7, 11, 77), 65 (1, 5, 13, 65), etc)
3. Co-prime numbers: pair of prime numbers that share no common factor
other than 1. The greatest common divisor between the pair is 1
4. Formula to derive prime numbers: 6n+1 or 6n-1 with the exception of
its result being the multiple of a prime (semi-prime: multiple of prime numbers)
5. 65537: a special prime number in RSA, normally used as an encryption key value
6. Greatest common divisor (gcd()): the largest number to divide two numbers
7. 'p' and 'q': two very large different prime numbers that are asymmetric
8. 'n': the product of 'p' and 'q'. n = p * q
9. n(): Euler totient function (n() = (p-1) * (q-1))
10. e: encryption key value (1 < e < n()). It is a prime number
between 1 and n() where gcd(n(), e) = 1.
11. public key: (e, n). to encrypt data/message (m) to be sent
from sender to receiver into a ciphertext
12. ciphertext, c: c =  m^e mod n
13. d: decryption key value. a prime number value that multiples e such that
the result is passed as a modulo of n() and it finally results to 1
14. private key: (d, n). to decrypt ciphertext to be received
by receiver from sender into a deciphered text/message (m)
15. deciphered text/message, m: m = c^d mod n
16. Final RSA formula: e*d = 1 (mod n())

n = p * q
where p and q are the prime factors of n
n() = (p-1) * (q-1)
n() is the euler-totient function
where n() are total number of co-prime numbers of n

e * d = 1 mod n() :-> the remainder of the division of the
product of ('e' and 'd') and n() is 1.
'e' must satisfy:
2 < e < n(), prime, co-prime of n()
'd' is the multiplicative inverse of 'e'

p, q = prime numbers
n = semi-prime numbers
c = cipher
m = message
e = encryption key/public key
d = decryption key/private key
s = digital signature

Verify Signature: B to verify A's signed message
A signs the message with his/her private key
s = m ^ d mod n

B verifies it with A's public key
m = s ^ e mod n

Decrypt Encryption: B to  decrypt A's encrypted message
A encrypts the message with B's public key
c = m ^ e mod n

B decrypts it with his/her private key
m = c ^ d mod n
