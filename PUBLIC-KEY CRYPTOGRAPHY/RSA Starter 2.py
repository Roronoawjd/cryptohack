Message = 12
e = 65537
p = 17
q = 23
N = p*q

enc = pow(Message,e,N)
print(enc)

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
N=(p-1)*(q-1)
print(N)