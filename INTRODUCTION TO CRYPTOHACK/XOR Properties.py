KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2_KEY1_XOR = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY2_KEY3_XOR = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAG_KEY1_KEY2_KEY3_XOR = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

def byte_xor(b1,b2):
    return [a^b for a,b in zip(b1,b2)]
def byte_xor_4(b1,b2,b3,b4):
    return bytes([a^b^c^d for a,b,c,d in zip(b1,b2,b3,b4)])
KEY2 = byte_xor(bytes.fromhex(KEY1),bytes.fromhex(KEY2_KEY1_XOR))
KEY3 = byte_xor(KEY2,bytes.fromhex(KEY2_KEY3_XOR))
FLAG = byte_xor_4(bytes.fromhex(KEY1),KEY2,KEY3,bytes.fromhex(FLAG_KEY1_KEY2_KEY3_XOR))
print(FLAG)