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

print("gcd(a, m) => Enter a and m: ")
a = int(input())
b = int(input())
print(ext_euc(a, b))