#!/usr/bin/python

import string 

utf8 = string.maketrans("NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm","ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz") 

print(string.translate("cvpbPGS{guvf_vf_pelcgb!}", utf8))

