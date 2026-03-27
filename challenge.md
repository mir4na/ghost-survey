Title: Ghost Survey

Description:
An intern built a tiny survey app for a haunted museum. It runs fine in casual tests, but real visitors keep crashing it in weird ways. Your job is to figure out what the program is really doing and recover the flag.

nc 34.10.217.112 9001

Attachment: https://drive.google.com/drive/folders/130nQfCcQHTW3whe8vGzSpyEJ1HVxjo-R?usp=sharing
- chall.c (source)
- chall (binary)
- ld-2.31.so (loader)
- libc-2.31.so (runtime)

Build:
```
gcc -o chall chall.c -fno-stack-protector -no-pie -Wl,-z,norelro
```

Rules:
- 64-bit Linux.
- ASLR on.
- No PIE, no stack protector.
