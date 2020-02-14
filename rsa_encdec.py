import math
import random

def ext_euc(a, b):
    s = 0
    old_s = 1
    t = 1
    old_t = 0
    r = a 
    old_r = b  
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (s, old_s) = ((old_s - (q * s)), s)
        (t, old_t) = ((old_s - (q * t)), t)
    if old_s < 0:
        old_s += old_r
    if old_t < 0:
        old_t += r
    return old_s

def check_if_prime(val):
    if val == 2:
        return True
    if val < 2 or val % 2 == 0:
        return False
    for i in range(3, val):
        if val % i == 0:
            return False
    return True

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    print("Enter p & q :")
    p = int(input())
    q = int(input())
    msg = int(input("Enter value to be encrypted: "))
    if check_if_prime(p) and check_if_prime(q):
        n = p * q
        phi = (p - 1) * (q - 1)
        e = random.randrange(1, phi)
        g = gcd(e, phi)

        while g != 1:
            e = random.randrange(1, phi)
            g = gcd(e, phi)

        d = ext_euc(e, phi)
        print("private key: " + str(d) + " & public key " + str(e))


        c = (pow(msg, e) % n)
        print("Encrypted value is : " + str(c))

        m = pow(c, d) % n
        print("Decrypted value is : " + str(m))
                
if __name__ == '__main__':
    main()



