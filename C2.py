base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
def hexToBytes(hex):
    bytes_arr = []
    i= 0
    while i < len(hex):
        byte = int(hex[i]+hex[i+1],16)
        bytes_arr.append(byte)
        i+=2
    return bytes_arr
    
def xorBytes(byte1, byte2):
    arr = bytearray()
    for b1, b2, in zip (byte1, byte2):
        arr.append(b1^b2)
    return bytes(arr)
    
def bytesToHex(byteArr):
    hexFinal =""
    for byte in byteArr:
        pair = hex(byte)[2:]
        if len(pair)==1:
            pair = '0'+pair
        hexFinal += pair
    return hexFinal
hex1 ="1c0111001f010100061a024b53535009181c"
byteArr1 = hexToBytes(hex1)
hex2 ="686974207468652062756c6c277320657965"
byteArr2 = hexToBytes(hex2)
xorCombo = xorBytes(byteArr1, byteArr2)
result = bytesToHex(xorCombo)
print(result)