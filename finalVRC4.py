"""
VRC4 Implementation

Authors: Manuel Escobar
        Mauricio Figueroa
        Victor Guiochin
"""
import random

s = [] #vectorS
plainText = raw_input("Message to encrypt: ")
plainTextBytes = []
cipherText = ""
cipherBytes = []
rc4key = raw_input("KEY: ")
rc4keylen = len(rc4key)
rc4keyVector = [] #vectorKeyRC4
rc4Bytes = []
vigenereKeyVector =[]
vigenereBytes = []
finalEncryptionBytes =[]

#initialization of s and rc4keyvector
for i in range(0,256):
    s.append(i)
    rc4keyVector.append(rc4key[i%rc4keylen])

#transform the rc4 key to int for ascii comparison
for i in range(len(s)):
    rc4Bytes.append(ord(rc4keyVector[i]))

#make vigenre key repeat itself till its the saem size as the key
for i in range (len(plainText)):
    vigenereKeyVector.append(rc4key[i%rc4keylen])

#transform the vigenere key to bytes for ascii
for i in range(len(plainText)):
    vigenereBytes.append(ord(vigenereKeyVector[i]))

#transform plaintext characters into array of ints for ascii
for i in range(len(plainText)):
    plainTextBytes.append(ord(plainText[i]))

#initial permutation
j = 0
for i in range (0,256):
    j =(j + s[i] + rc4Bytes[i])%256
    s[i], s[j] = s[j], s[i] #swap

temp, i, j, count = 0 ,0 ,0, 0
rc4KeyStream = []
while count < len(plainText):
     i = (i+1)%256
     j = (j + s[i])%256
     s[i], s[j] = s[j], s[i] #swap
     temp = (s[i] + s[j])%256
     rc4KeyStream.append(s[temp])
     count = count + 1
# XOR encryption done with the rc4 key and the plaintext
for i in range(len(plainText)):
    cipherBytes.append(rc4KeyStream[i] ^ plainTextBytes[i])

#random generaton oj j to break appart into c1 and c2
j = random.randint(0,(len(plainText) - 1))

#vigenere encryption of c1
c1 = []
for i in range(0, j):
    c1.append((cipherBytes[i] + vigenereBytes[i]) % 256)

#vigenere encryption of c2
c2 = []
for i in range(j, len(plainText)):
    c2.append((cipherBytes[i] + vigenereBytes[i]) % 256)

#adding c1 and c2 together to generate c
c =[]
for element in c1:
    c.append(element)
for element in c2:
    c.append(element)

#transform ascii code to leterts
for i in c:
    cipherText = cipherText + str(chr(i))
cipherText = cipherText + str(j)
print("Your encrypted plainText is : " + cipherText)

#--------------------Decryption-----------------------------#
decrypt = raw_input("Do you wish to decrypt your message(y/n)")
if decrypt == "y":
    #decryption of vigenere of first c1
    desencryptedVigenreBytes = [] # this could be consideres as c but for decrytion
    for i in range(0,j):
        desencryptedVigenreBytes.append((c[i] - vigenereBytes[i]) % 256)

    #decryption of vigenere of first c2
    for i in range(j,len(plainText)):
        desencryptedVigenreBytes.append((c[i] - vigenereBytes[i]) % 256)
    # print(desencryptedVigenreBytes)
    # print(cipherBytes)

    #rc4 XOR decryption
    desencryptedRc4Bytes = []
    for i in range(len(plainText)):
        desencryptedRc4Bytes.append(rc4KeyStream[i] ^ cipherBytes[i])

    decipheredText = ""
    for i in desencryptedRc4Bytes:
        decipheredText = decipheredText + str(chr(i))

    print("The desencrypted message is: " + decipheredText )
else:
    pass
