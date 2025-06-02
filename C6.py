def hexToBytes(hex):
    bytes_arr = []
    i= 0
    while i < len(hex):
        byte = int(hex[i]+hex[i+1],16)
        bytes_arr.append(byte)
        i+=2
    return bytes_arr
def b64ToBytes(b64):
    base64Chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    b64 = b64.strip().replace('\n', '').replace('=', '')
    byteArr = []
    buffer =0
    bits = 0
    for char in b64:
        if char not in base64Chars:
            continue
        val = base64Chars.index(char)
        buffer = (buffer<<6) | val
        bits += 6
        if bits >=8:
            bits  -=8
            byte = (buffer >> bits) & 0xFF
            byteArr.append(byte)
    return byteArr
def getScore(text):
    letters= b'ETAOINSHRDLU etaoinshrdlu'
    score =0 
    for char in text:
        if char in letters:
            score +=1
    return score
def findKey(byteArr):
    maxScore =0
    finalText = ""
    for tempKey in range(256):
        char = [byte ^ tempKey for byte in byteArr]
        tempScore = getScore(char)
        if tempScore > maxScore:
            maxScore =tempScore
            key = tempKey
    return key, maxScore
def singleXOR(byteArr, key):
    return [byte^key for byte in byteArr]
def hammingDist(byte1, byte2):
    dist =0
    for b1, b2, in zip (byte1, byte2):
        xor =b1^b2
        dist += bin(xor).count('1')
    return dist
def getKeySize(bytesArr):
    keySizes = []
    for size in range(2,41):
        b = [bytesArr[i:i+size] for i in range(0,size*8, size)]
        if len(b) < 4:
            continue
        distSum =0
        dists = []
        for i in range(len(b)-1):
            dist = hammingDist(b[i], b[i+1])
            dists.append(dist/size)
       # dist = distSum/pairsCount/size
        avg_dist = sum(dists)/len(dists)
        temp = dist/size
  #      print("key", size, "normalized", avg_dist, dist)
        if size > 20:
            keySizes.append((avg_dist, size))
    keySizes.sort()
    return keySizes[0][1]
    #    if temp < maxScore:
     #       maxScore =  temp
     #       maxKeySize = size
    #return maxKeySize

lines = []
with open('6.txt', 'r') as file:
    b64 = file.read()

byteArr = b64ToBytes(b64)
#print(byteArr[:20])
keySize = getKeySize(byteArr)
#print("size", keySize)
blocks = [[] for _ in range (keySize)]
for i , byte in enumerate(byteArr):
    blocks[i%keySize].append(byte)

msg =[]
#for block in blocks:
 #   key, score = findKey(block)
  #  keys.append(key)
   # msg.append(text)
key = [findKey(block)[0] for block in blocks]
decryptKeys = []
for i in range(len(byteArr)):
    byte = byteArr[i]^key[i%len(key)]
    decryptKeys.append(byte)
#print(b64ToBytes(b64))
print(''.join(chr(b) for b in decryptKeys))
#print(key)

#print(base64.b64decode(b64, validate =True))