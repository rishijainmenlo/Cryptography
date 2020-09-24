# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    encryptedString = ""
    alpha = "ABCDEFGHIJKLMNOPOQSTUVWXYZ"
    begNum = 65
    endNum = 90
    numInAlpha = 26
    
    for character in plaintext:
        if character in alpha:
            numValue = ord(character) - begNum
            if numValue + offset > numInAlpha - 1:
                encryptedString += encrypt_help(numValue, offset)
            else:
                encryptedString += (chr(ord(character) + offset))
        else:
            encryptedString = "No message received"
    return encryptedString

def encrypt_help(numValue, offset):
    eString = ""
    numInAlpha = 26
    begNum = 65
    numValue = (numValue + offset)%numInAlpha
    eString = chr(numValue + begNum)
    return eString

# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
    decryptedString = ""
    alpha = "ABCDEFGHIJKLMNOPOQSTUVWXYZ"
    begNum = 65

    for character in ciphertext:
        if character in alpha:
            numValue = ord(character) - begNum
            if numValue - offset < 0:
                decryptedString += decrypt_help(numValue, offset)
            else:
                decryptedString += (chr(ord(character) - offset))
        else:
            decryptedString = "No message received"
    return decryptedString

def decrypt_help(numValue, offset):
    dString = ""
    numInAlpha = 26
    begNum = 65
    numValue = (numValue - offset)% numInAlpha
    eString = chr(numValue + begNum)
    return eString


# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    encryptList = []
    begNum = 65
    for character in range(len(plaintext)):
        numValue = (ord(plaintext[character]) + ord(keyword[character])) % 26
        numValue += begNum
        encryptList.append(chr(numValue))
    encryptedWord = "".join(encryptList)
    return encryptedWord

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    decryptList = []
    begNum = 65
    for character in range(len(ciphertext)):
        numValue = (ord(ciphertext[character]) - ord(keyword[character])) % 26
        numValue += begNum
        decryptList.append(chr(numValue))
    decryptedWord = "".join(decryptList)
    return decryptedWord

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
    pass

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: tuple B - a length-n tuple of integers
def create_public_key(private_key):
    pass

# Arguments: string, tuple (W, Q, R)
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    pass

# Arguments: list of integers, tuple B - a length-n tuple of integers
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    pass

def main():
    # Testing code here
    plaintext = "ATTACKATDAWN"
    keyword = "LEMON"
   
    string1 = encrypt_caesar("X", 5)
    print("Caesar Encryption: " + string1)
    string2 = decrypt_caesar(string1, 5)
    print("Caesar Decryption: " + string2)

    vigenereKey = vigenere_key(plaintext, keyword)
    print("Vigenere Key: " + vigenereKey)
    string3 = encrypt_vigenere(plaintext, vigenereKey)
    print("Vigenere Encryption: " + string3)
    string4 = decrypt_vigenere(string3, vigenereKey)
    print("Vigenere Decryption: " + string4)

if __name__ == "__main__":
    main()

