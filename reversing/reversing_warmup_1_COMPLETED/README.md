# Resources

Points: 50

## Category

Reversing

## Question

>Throughout your journey you will have to run many programs. Can you navigate to /problems/reversing-warmup-1_4_6b2499250c4624337a1948ac374c4934 on the shell server and run this program to retreive the flag?

## Hint

If you are searching online, it might be worth finding how to exeucte a program in command line.

## Solution

Downloaded the file and try to run on my macOS with no success. I had to run a VM with Linux to run the file.

## Automation

```bash
$ wget -c https://2018shell.picoctf.com/static/525cdd5f4b450c39695d047d47da60c9/run
$ chmod +x run
$ ./run > flag.txt
```

### Flag

`picoCTF{welc0m3_t0_r3VeRs1nG}`