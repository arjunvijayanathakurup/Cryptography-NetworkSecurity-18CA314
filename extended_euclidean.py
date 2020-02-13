import math

def gcd(r, old_r, s, old_s, t, old_t):
    while(r != 0):
        q = math.floor(old_r / r) 

        temp_oldr = old_r
        old_r = r
        tempr = r
        r = temp_oldr - q * tempr 

        temp_olds = old_s
        old_s = s
        temps = s
        s = temp_olds - q * temps

        temp_oldt = old_t
        old_t = t
        tempt = t
        t = temp_oldt - q * tempt
        print(r, old_r)
        
        if r == 0:
            print("Multiplicative inverse is " + str(old_r))
        val = gcd(r, old_r, s, old_s, t, old_t)
        return val

s = 0
old_s = 1
t = 1
old_t = 0
print("gcd(a, b) => Enter a and b: ")
a = int(input())
b = int(input())
gcd(a, b, s, old_s, t, old_t)
