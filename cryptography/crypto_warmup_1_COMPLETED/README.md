# Resources

Points: 75

## Category

Cryptography

## Question

>Crpyto can often be done by hand, here's a message you got from a friend, llkjmlmpadkkc with the key of thisisalilkey. Can you use this table to solve it?.

## Hint

Submit your answer in our competition's flag format. For example, if you answer was 'hello', you would submit 'picoCTF{HELLO}' as the flag.

## Solution

This is a vigenere tableu from vigenere [cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)

The key is the X and the message as Y in the table. Challenge is how to automatise.

I found a really nice script https://delayma.wordpress.com/2019/02/01/crypto-warmup-1-picoctf-18/

## Automation

```python
#!/usr/bin/python
import string

letters =  string.ascii_lowercase

ciphertext = 'llkjmlmpadkkc'
key = 'thisisalilkey'


decrypted = ''
for i in range(0,13):
        decrypted +=  letters[letters.index(ciphertext[i]) - letters.index(key[i]) % 26]
print 'picoCTF{'+ decrypted.upper() + '}'
```

### Flag

`picoCTF{SECRETMESSAGE}`