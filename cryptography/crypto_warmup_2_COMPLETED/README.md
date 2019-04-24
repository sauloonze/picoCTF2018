# Resources

Points: 75

## Category

Cryptography

## Question

>Cryptography doesn't have to be complicated, have you ever heard of something called rot13? cvpbPGS{guvf_vf_pelcgb!}

## Hint

This can be solved online if you don't want to do it by hand!

## Solution

A lot of decode available to rot13. I have found a python script.

## Automation

```python
#!/usr/bin/python

import string 

utf8 = string.maketrans("NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm","ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz") 

print(string.translate("cvpbPGS{guvf_vf_pelcgb!}", utf8))
```

### Flag

`picoCTF{this_is_crypto!}`