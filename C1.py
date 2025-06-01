import base64
base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
def hexToBytes(hex):
    bytes_arr = []
    i= 0
    while i < len(hex):
        byte = int(hex[i]+hex[i+1],16)
        bytes_arr.append(byte)
        i+=2
    return bytes_arr
def bytesToBase64(bytes_arr):
    bitstream=0
    bitLen =0
    b64 = []
    for byte in bytes_arr:
        bitstream  = (bitstream << 8)|byte
        bitLen+=8
        
        while bitLen >=6:
            shift = bitLen-6
            index = (bitstream >>shift) & 0b111111
            b64.append(base64[index])
            bitLen-=6
            bitstream &= (1<<bitLen)-1
    if bitLen >0:
        index = (bitstream <<(6-bitLen)) & 0b111111
        b64.append(base64[index])
    return ''.join(b64)

hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
#print(hexToBytes(hex))
bytes_arr = hexToBytes(hex)
print(bytesToBase64(bytes_arr))