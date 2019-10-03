

# Cyber Jawara 2019 Qualifiers

For all source code and binaries see attachments folder

Problems me and my team solved (Including upsolves). In this repo i will only explain binex, crypto, and reversing problems
* Starlight (Binary Exploitation)
* Noir (Binary Exploitation)
* Homelander (Binary Exploitation)
* newbie.exe (Reverse Engineering)
* Haseul (Reverse Engineering)
* Gowon (Reverse Engineering)
* Hyunjin (Reverse Engineering) (upsolve)
* Sanity Check (Cryptography)
* Insanity Check (Cryptography)
* RC4 (Cryptography)
* Cj.docx (Digital Forensics)
* audit.log (Digital Forensics)
* Split (Network)
* Exfiltration (Network) (upsolve)
* Mysterious (Web Hacking)
* Under Construction (Web Hacking)
* Chuu (Web Hacking)
* Heejin (Web Hacking)



### Starlight

Injection in file name, because the program uses snprintf it is possible to truncate the leading ".lang" by using a payload that includes many "./"
Payload i used(python): 
```python
"./"*53 + "../flag.txt"
```


### Noir

Buffer overflow on stack, we are able to increase any value on the stack, in this case the return address. Adding 3 to the return address to the hidden shell function. It is also possible to create a ropchain, ofcourse the chain would take a long time to make.
Payload i used(python): 
```python
"1006\n"*4 + "-1"
```


### Homelander

Service uses ubuntu 18.04, which means it uses libc 2.27! Most possible problem is tcache poisoning, which is exactly what it is.

<!-- image -->

Use after free, 16 total chunks possible to be used, double free, a pwners dream. <br>
First we need a libc leak, just fill the tcache bin with 7 chunks and free another after, than read the chunk, easy enough <br>
After that just write a one_gadget to \_\_free_hook and get shell


### newbie.exe

PE32+ file, thankfully ghidra can decompile it easy (I use ubuntu). It ended up just being reversing this line

<!-- image -->

A few lines of python code did the trick


### Haseul

This time it was an elf file, same static reversing though. A bit harder since the input in dependant on each other, seems like a job z3 would solve easily

<!-- image -->

z3 did it in about 2 seconds


### Gowon

Slight dynamic reversing, \_\_dest is decoded to be a pointer to a function

<!-- image -->

