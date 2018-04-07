import random

s = [] #vectorS
plainText = "Hello people"
plainTextBytes = []
cipherText = ""
cipherBytes = []
rc4key = "thisismykey" #<- change this for input
rc4keylen = len(rc4key)
rc4keyVector = [] #vectorKeyRC4
rc4Bytes = []
vigenereKey = "lemon" #<- change this for input
vigenereKeylen = len(vigenereKey)
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
    vigenereKeyVector.append(vigenereKey[i%vigenereKeylen])

#transform the vigenere key to bytes for ascii
for i in range(len(plainText)):
    vigenereBytes.append(ord(vigenereKeyVector[i]))

#transform plaintext characters into array of ints for ascii
for i in range(len(plainText)):
    plainTextBytes.append(ord(plainText[i]))

# print(rc4key)
# print(rc4keyVector)
# print(rc4Bytes)

#initial permutation
j = 0
for i in range (0,256):
    j =(j + s[i] + rc4Bytes[i])%256
    s[i], s[j] = s[j], s[i] #swap
    # print(s[j])

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

#vigenere encryption
for i in range(len(plainText)):
    finalEncryptionBytes.append((cipherBytes[i] + vigenereBytes[i]) % 256)

#transform ascii code to leterts
for i in finalEncryptionBytes:
    cipherText = cipherText + str(chr(i))

print("Your encrypted plainText is : " + cipherText)

#--------------------Decryption-----------------------------#

#decryption of vigenere
desencryptedVigenreBytes = []
for i in range(len(plainText)):
    desencryptedVigenreBytes.append((finalEncryptionBytes[i] - vigenereBytes[i]) % 256)
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








# print(cipherBytes)
print(desencryptedRc4Bytes)
print(plainTextBytes)
# print(finalEncryptionBytes)

#decryption of vigenere
# testBytes = []
# for i in range(len(plainText)):
#     testBytes.append((finalEncryptionBytes[i] - vigenereBytes[i]) % 256)
#
# print(testBytes)



# print(cipherText)







# test to verify that the XOR encryption in rc4 works
# test = []
# for i in range(len(plainText)):
#     test.append(rc4KeyStream[i] ^ cipherBytes[i])
#

# print(cipherBytes)
# print(test)
