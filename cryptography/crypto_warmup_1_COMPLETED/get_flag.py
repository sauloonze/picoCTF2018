#!/usr/bin/python
import string

letters =  string.ascii_lowercase

ciphertext = 'llkjmlmpadkkc'
key = 'thisisalilkey'


decrypted = ''
for i in range(0,13):
        decrypted +=  letters[letters.index(ciphertext[i]) - letters.index(key[i]) % 26]
print 'picoCTF{'+ decrypted.upper() + '}'