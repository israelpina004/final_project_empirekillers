import constants as c
import sys
def msg2chunks(message, bits):
    message_bin = ''

    for i in message.encode():
        message_bin += fill_0s(bin(i)[2:], 8)
    length = len(message_bin)
    message_bin += '1'
    chunks = []
    if bits in (224, 256):
        chunklen = 512
        lenlen = 64
    elif bits in (384, 512):
        chunklen = 1024
        lenlen = 128
    pad_0s = '0' * (chunklen - (len(message_bin) + lenlen) % chunklen)
    chunk_bin = message_bin + pad_0s
    length_bin = fill_0s(bin(length)[2:], lenlen)
    chunk_bin += length_bin
    chunks = []
    if len(chunk_bin) > chunklen:
        for i in range(int(len(chunk_bin) / chunklen)):
            chunks.append(chunk_bin[chunklen*i:chunklen*(i+1)])
    else:
        chunks = [chunk_bin]
    return chunks
def fill_0s(val, places):
    out = ((places - len(val)) * '0') + val
    return out
def _words(chunk_bin, ct, mod, C):
    w = [0 for i in range(ct)]
    for i in range(16):
        start = mod*i
        end = mod*(i+1)
        w[i] = int(chunk_bin[start:end], 2)
    for i in range(16, ct):
        s0 = ror(w[i-15], C[2][0], mod)^ror(w[i-15], C[2][1], mod)^(w[i-15] >> C[2][2])
        s1 = ror(w[i-2], C[3][0], mod)^ror(w[i-2], C[3][1], mod)^(w[i-2] >> C[3][2])
        w[i] = (w[i-16] + s0 + w[i-7] + s1) % 2**mod
    return w
def ror(num, val, mod):
    pre = (num % 2 ** val) * 2**(mod - val)
    post = num >> val
    return pre + post
def sha2hash(message, bits, sh):
    if not bits in (224, 256, 384, 512):
        print('Only standard SHA2 functions are supported')
        sys.exit()
    if bits in (224, 256):
        rounds = 64
        mod = 32
    elif bits in (384, 512):
        rounds = 80
        mod = 64
    chunks = msg2chunks(message, bits)
    h, k, C = c.constants(bits, sh)
    for chunk in chunks:
        xs = h[:]
        w = _words(chunk, rounds, mod, C)
        for i in range(rounds):
            S1 = ror(xs[4], C[1][0], mod)^ror(xs[4], C[1][1], mod)^ror(xs[4], C[1][2], mod)
            ch = (xs[4] & xs[5])^(~xs[4] & xs[6])
            temp = (xs[7] + S1 + ch + k[i] + w[i]) % 2**mod
            xs[3] = (xs[3] + temp) % 2**mod
            S0 = ror(xs[0], C[0][0], mod)^ror(xs[0], C[0][1], mod)^ror(xs[0], C[0][2], mod)
            maj = (xs[0] & xs[1])^(xs[0] & xs[2])^(xs[1] & xs[2])
            temp = (temp + S0 + maj) % 2**mod
            xs = [temp] + [xs[i-1] for i in range(1, 8)]
        h = [(h[i] + xs[i]) % 2**mod for i in range(8)]
    digest = sum([h[i] << mod * (7-i) for i in range(8)]) >> sh
    return(digest)
def main():
    bits = sys.argv[1]
    if bits in ('512/224', '512/256'):
        sh = 512 - int(bits[4:])
        bits = 512
    else:
        bits = int(bits)
        sh = {224:32, 256:0, 384:128, 512:0}[bits]
    try: message = sys.argv[2]
    except IndexError: message = ''
    digest = sha2hash(message, bits, sh)
    ans = hex(digest)
    print(ans[2:len(ans)])
if __name__ == '__main__':
    main()
