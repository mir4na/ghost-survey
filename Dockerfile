FROM ubuntu:20.04 AS builder

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /build
COPY chall.c chall.c

RUN gcc -o chall chall.c -fno-stack-protector -no-pie -Wl,-z,norelro


FROM ubuntu:20.04

RUN apt-get update \
    && apt-get install -y --no-install-recommends socat \
    && useradd -m ctf \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /home/ctf

COPY --from=builder /build/chall chall
COPY flag.txt flag.txt

RUN chmod 755 chall

USER ctf

EXPOSE 9001

CMD ["socat", "TCP-LISTEN:9001,reuseaddr,fork", "EXEC:/home/ctf/chall,stderr"]
