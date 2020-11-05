import math
import random
# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    min = 64
    max = 91
    shift = 26
    encrypt = ""
    for letter in plaintext:
        current = ord(letter)
        if current > min and current < max:
            character = ord(letter) + offset
            if character > max - 1:
                character = character - shift
            current = character
        encrypt = encrypt + chr(current)
    
    return encrypt

# Arguments: String, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
    min = 64
    max = 91
    shift = 26
    decrypt = ""
    for letter in ciphertext:
        current = ord(letter)
        if current > min and current < max:
            character = ord(letter) - offset
            if character < min + 1:
                character = character + shift
            current = character
        decrypt = decrypt + chr(current)
    return decrypt


#Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    keyword = vigenere_key(plaintext, keyword)
    encryptList = []
    begNum = 65;
    for character in range(len(plaintext)):
        numValue = (ord(plaintext[character]) + ord(keyword[character])) % 26
        numValue += begNum;
        encryptList.append(chr(numValue))
    encryptedWord = "".join(encryptList)
    return encryptedWord

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    keyword = vigenere_key(ciphertext, keyword)
    decryptList = []
    begNum = 65
    for character in range(len(ciphertext)):
        numValue = (ord(ciphertext[character]) - ord(keyword[character])) % 26
        numValue += begNum
        decryptList.append(chr(numValue))
    decryptedWord = "".join(decryptList)
    return decryptedWord

# Arguments: string, string
# returns: String
def vigenere_key(plaintext, keyword):
    keylist = list(keyword)
    if len(plaintext) == len(keylist):
        return keyword
    if len(plaintext) < len(keyword):
        keylist = keyword[0:len(keyword)-(len(keyword)-len(plaintext))]
        return ("".join(keylist))
    else:
        for character in range(len(plaintext)-len(keylist)):
            keylist.append(keylist[character%len(keylist)])
    newKeyWord = "".join(keylist)
    return newKeyWord

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
    W=[]
    total = 1
    for bit in range(n):
        num = random.randint(total+1,2*total)
        total += num
        W.append(num)
    Q = random.randint(total, 2*total)
    R = random.randint(2, Q-1)
    while(math.gcd(R, Q) != 1):
          R = random.randint(2, Q-1)
    return (tuple(W), Q, R)

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: B - a length-n tuple of integers
def create_public_key(private_key):
    W, Q, R = private_key
    B =[]
    for element in W:
        B.append((R * element) % Q)
    return tuple(B)

# Arguments: string, tuple B
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    encrypted = []
    M = []
    for character in plaintext:
        C = 0
        M = byte_to_bits(ord(character))
        #print(public_key[1])
        for position in range (0, 8):
            x = int(M[position])
            y = int(public_key[position])
            C += (x*y)
        encrypted.append(C)
    return encrypted

# Arguments: integer
# returns: list of 1s and 0s
def byte_to_bits(byte):
    bits = []
    binary = bin(byte)[2:]
    for element in binary:
        bits.append(element)
    if (len(bits) < 8):
        remainder = 8 % len(bits)
        for num in range(0, remainder):
            bits.insert(0,0)
    return bits

# Arguments: list of integers, private key (W, Q, R) with W a tuple.
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    W = private_key[0]
    Q = private_key[1]
    R = private_key[2]
    S = findS(R,Q)
    Decrypted = []
    for character in ciphertext:
        C = character * S % Q
        bitString = []
        for element in reversed(W):
            if element <= C:
                bitString.append("1")
                C = C - element
            else:
                bitString.append("0")
        Decrypted.append(chr(bits_to_byte(reversed(bitString))))
    return "".join(Decrypted)

# Arguments: List of integers, 1s and 0s
# returns: integer
def bits_to_byte(bits):
    bitsAsStrings = []
    byte = 0
    for element in bits:
        bitsAsStrings.append(str(element))
        bitString = "".join(bitsAsStrings)
        byte = int(bitString,2)
    return byte

# Arguments: integer, integer
# Returns: integer
def findS(R, Q):
    for S in range(2,Q - 1):
        if (R * S % Q == 1):
            return S
    return 0

def main():
    pass
if __name__ == "__main__":
    main()