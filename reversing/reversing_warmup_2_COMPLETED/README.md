# Resources

Points: 50

## Category

Reversing

## Question

>Can you decode the following string dGg0dF93NHNfczFtcEwz from base64 format to ASCII?

## Hint

Submit your answer in our competition's flag format. For example, if you answer was 'hello', you would submit 'picoCTF{hello}' as the flag.

## Solution

Downloaded the file and try to run on my macOS with no success. I had to run a VM with Linux to run the file.

## Automation

```python
#!/usr/bin/python
import base64
print "picoCTF{%s}" % base64.b64decode('dGg0dF93NHNfczFtcEwz')
```

### Flag

`picoCTF{th4t_w4s_s1mpL3}`