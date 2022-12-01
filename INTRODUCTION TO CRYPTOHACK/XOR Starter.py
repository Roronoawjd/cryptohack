string ="label"
integer = 13
unicode_string = [ord(c) for c in string]
print(unicode_string)
xor_unicode = [integer^i for i in unicode_string]
print(xor_unicode)
xor_string = "".join(chr(o) for o in xor_unicode)
print(xor_string)
flag = "crypto{"+ xor_string +"}"
print("flag : "+flag)