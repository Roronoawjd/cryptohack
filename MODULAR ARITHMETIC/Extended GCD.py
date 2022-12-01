def extended_gcd(p,q):   #q가 p보다 클 때
    if p == 0:
        return(q, 0, 1)
    else:
        (gcd, u, v) = extended_gcd(q % p,p)
        return (gcd, v-(q//p)*u, u)

p = 26513
q = 32321

gcd , u , v = extended_gcd(p,q)
print("GCD : {}".format(gcd))
print("u,v : {},{}".format(u,v))
print("FLAG : crypto{{{},{}}}".format(u,v))

