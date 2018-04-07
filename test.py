"""
VRC4 Implementation

Authors: Manuel Escobar
        Mauricio Figueroa
        Victor Guiochin

guided from the RC4 from :author: Christopher D. Leary <cdleary@gmail.com>
"""

import textwrap
try:
    import readline
except ImportError:
    pass

def initialize(key):
    k = range(256)
    j = 0
    for i in range(256):
        j = (j + k[i] + key[i%len(key)]) % 256
        k[i], k[j] = k[j], k[i]
    return k

def gen_random_bytes(k):
    i, j = 0, 0
    while True:
        i = (i + 1) % 256
        j = (j + k[i]) % 256
        k[i], k[j] = k[j], k[i]
        yield k[(k[i] + k[j]) % 256]

def run_rc4(k, text):
    cipher_chars =[]
    random_byte_gen = gen_random_bytes(k)
    for char in text:
        byte = ord(char)
        cipher_byte = byte ^ random_byte_gen.next()
        cipher_chars.append(chr(cipher_byte))
    return ''.join(cipher_chars)


def loop_user_query(k):
    quotes = "'\'"
    while True:
        text = raw_input('Enter plain or cipherText')
        if text[0] == text[-1] and text[0] in quotes:
            print 'Unescaping ciphertext...'
            text = text[1:-1].decode('string_escape')
        k_copy = list(k)
        print 'Your RC4 text is:', repr(run_rc4(k_copy, text))
        print

def main():
    key = raw_input("Enter encrytption key: ")
    print
    key = [ord(char) for char in key]
    k = initialize(key)
    #perform cipher until exit
    try:
        loop_user_query(k)
    except EOFError:
        print
        print "Algo salio mal"


if __name__ == '__main__':
    main()
