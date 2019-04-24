# Resources

Points: 50

## Category

General Skills

## Question

>We put together a bunch of resources to help you out on our website! If you go over there, you might even find a flag! https://picoctf.com/resources ([link](https://picoctf.com/resources)) 

## Hint

No hints available

## Solution

Just search for picoCTF{ in the source of the html file.

## Automation

1. Download the file

```
$ wget -c https://picoctf.com/resources resources.html
```

2. Script to dump the flag
```bash
#!/bin/bash

cat resources.html | grep -oE picoCTF{.*}
```

### Flag

`picoCTF{xiexie_ni_lai_zheli}`