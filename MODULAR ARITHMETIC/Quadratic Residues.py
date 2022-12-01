import math
p = 29
ints = [14, 6, 11]

a = [i for i in range (1,p) if math.gcd(p,i)==1]
for a2 in a :
    a2 = a2**2
    if a2 < 29:
        for i in ints:
            if a2 == i:
                print("Quadratic Residue value : {}, a value : {}".format(i, int(math.sqrt(a2))))
    else:
        a2_mod = a2%p
        for i in ints:
            if a2_mod == i:
                print("Quadratic Residue value : {}, a value : {}".format(i, int(math.sqrt(a2))))