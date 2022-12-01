message = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
message = bytes.fromhex(message)
format = b'crypto{'

key = [a^b for a,b in zip(message[0:7],format)]+[ord('y')]  #KEY = myXORkey
#print(bytes(key))

flag = []
key_len = len(key) # 키 길이 8
for i in range(len(message)):   #message길이 만큼 반복
    flag.append(message[i]^key[i%key_len])    #메시지와 키와 xor연산

flag = "".join(chr(o) for o in flag)    #flag join
print(flag)