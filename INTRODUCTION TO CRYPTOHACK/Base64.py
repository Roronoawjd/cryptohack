import base64

hex_String = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
bytes_String = bytes.fromhex(hex_String)
#print(bytes_String)

base64_encode = base64.b64encode(bytes_String)
print(base64_encode)