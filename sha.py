import constants as c

def _msg2chunks(message_, chunk_info):
    chunk_len, len_len = chunk_info
    message, leading0s = message_
    message_len = message.bit_length() + leading0s
    if message_len >= 1<<128:
        raise RuntimeError('Big Input ;(')
    message <<= 1; message += 1 # Append a 1
    message_len += 1
    message <<= chunk_len - (message_len % chunk_len)
    if message % chunk_len > chunk_len - len_len:
        message <<= chunk_len
    message += message_len - 1
    message_len = message.bit_length() + leading0s
    if message_len % chunk_len != 0:
        raise RuntimeError('Chunks had bad length of' + str(message_len))
    chunks = [(message >> (chunk_len * i)) & ((1 << chunk_len) - 1)
            for i in range(int(message_len / chunk_len))]
    chunks.reverse()
    return chunks
def _words(chunk, ct, mod, C):
    w = [0 for i in range(ct)]
    for i in range(16):
        mask = 0xffffffff << (512-32*(i+1))
        w[i] = (chunk & mask) >> (512-32*(i+1))
    for i in range(16, ct):
        s0 = (_ror(w[i-15], C[2][0], mod) ^ _ror(w[i-15], C[2][1], mod) ^
                (w[i-15]>>C[2][2]))
        s1 = (_ror(w[i-2], C[3][0], mod) ^ _ror(w[i-2], C[3][1], mod) ^
                (w[i-2]>>C[3][2]))
        w[i] = (w[i-16] + s0 + w[i-7] + s1) % (2**mod)
    return w
def _ror(num, val, mod):
    pre = (num % 2 ** val) * 2**(mod - val)
    post = num >> val
    return pre + post
def _hash(message, algo, debug="no"):
    conversion_codes = {'sha224': (256, 224, 64, 32, (512, 64)), 'sha256': (256, 256, 64, 32, (512, 64)), 'sha384': (512, 384, 80, 64, (1024, 128)), 'sha512': (512, 512, 80, 64, (1024, 128)), 'sha512/224': (512, 224, 80, 64, (1024, 128)), 'sha512/256': (512, 256, 80, 64, (1024, 128))}
    bits, keep, rounds, mod, chunk_info = conversion_codes[algo]
    sh = bits - keep
    chunks = _msg2chunks(message, chunk_info)
    if "chunk" in debug or "all" in debug:
        print([hex(i) for i in chunks])
    h, K, C = c.constants(algo)
    for chunk in chunks:
        xs = h[:]
        w = _words(chunk, rounds, mod, C)
        if "word" in debug or "all" in debug:
            print([hex(i) for i in w])
        for i in range(rounds):
            S1 = (_ror(xs[4], C[1][0], mod)^_ror(xs[4], C[1][1], mod) ^
                    _ror(xs[4], C[1][2], mod))
            ch = (xs[4] & xs[5])^(~xs[4] & xs[6])
            temp = (xs[7] + S1 + ch + K[i] + w[i]) % 2**mod
            xs[3] = (xs[3] + temp) % 2**mod
            S0 = (_ror(xs[0], C[0][0], mod)^_ror(xs[0], C[0][1], mod) ^
                    _ror(xs[0], C[0][2], mod))
            maj = (xs[0] & xs[1])^(xs[0] & xs[2])^(xs[1] & xs[2])
            temp = (temp + S0 + maj) % 2**mod
            xs = [temp] + [xs[i-1] for i in range(1, 8)]
            if "intern" in debug or "all" in debug:
                bytes = chunk_info[1] // 8
                print(str(i).zfill(2) + ': ' +
                        ' '.join([hex(int(i))[2:].zfill(bytes) for i in xs]))
        h = [(h[i] + xs[i]) % 2**mod for i in range(8)]
    digest = sum([h[i] << mod * (7-i) for i in range(8)]) >> sh
    return(digest.to_bytes(int(keep / 8), byteorder='big'))
