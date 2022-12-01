string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
string_byte = bytes.fromhex(string)
string_int = [i for i in string_byte]

#print(string_int)
for i in range(0,17):
    a = bytes([o^i for o in string_int])
    if(a[:6]==bytes('crypto','utf-8')):
        print(a.decode('utf-8'))