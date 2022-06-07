
# What's SHA?

SHA stands for Secure Hashing Algorithm and is used to convert text into another string of text of a fixed length. The length of a SHA hash depends on which version is being utilized. The number representing the length of the hash string in bits (exp. a SHA-512 hash is 512 bits long). SHA is used in email address hashing, password hashing, blockchain projects, and general security applications and protocols. SHA hashes cannot be "decrypted," as hashes do not encrypt data, and they are not reversible. Hashes are primarily used in authentication systems to be stored in place of plaintext passwords, so there is no need for them to be decryptable or reversible; in fact, it's a good thing they aren't. If a hacker were to get into a password database, they would most likely not be able to do anything malicious if all there is are hashes of passwords. Here is an example of hashed text:

    Original Text: Crimea 2014
  
    SHA-512: faf3624934859414d2b8508886537c03353cce7932dd34116edc5233f0f4e08e893fc2a0a74236733a4139f1362301c4fc48bd6d6f5346af577e1f0cda1c1e3e

# How SHA Works

The SHA-2 hashing algorithms differ slightly. We will use the SHA-512 hashing algorithm as an example, which can be separated into four steps.

## 1 and 2. Appending bits

The plaintext message to be hashed is padded with bits such that its length
is 128 bits less than a multiple of 1024. The padded bits start with a 1 and 
end in a stream of 0s that end once the message is at a satisfactory length.

The remaining bits are added by taking the modulo of the message block by 2^64
and appending that to the end of the message block.

## 3. Setting up default values and round constants

Eight default hash values are initialized by taking the first 64
bits of the fractional parts of the square roots of the first eight prime
numbers.

    h[0..7] := 0x6a09e667f3bcc908, 0xbb67ae8584caa73b, 0x3c6ef372fe94f82b, 0xa54ff53a5f1d36f1, 
               0x510e527fade682d1, 0x9b05688c2b3e6c1f, 0x1f83d9abfb41bd6b, 0x5be0cd19137e2179


An array of 80 "round constants," which contains the first 64 bits of
the fractional parts of the cube roots of the first 80 prime
numbers, is initialized.

    k[0..79] := 0x428a2f98d728ae22, 0x7137449123ef65cd, 0xb5c0fbcfec4d3b2f, 0xe9b5dba58189dbbc, 0x3956c25bf348b538, 
                0x59f111f1b605d019, 0x923f82a4af194f9b, 0xab1c5ed5da6d8118, 0xd807aa98a3030242, 0x12835b0145706fbe, 
                0x243185be4ee4b28c, 0x550c7dc3d5ffb4e2, 0x72be5d74f27b896f, 0x80deb1fe3b1696b1, 0x9bdc06a725c71235, 
                0xc19bf174cf692694, 0xe49b69c19ef14ad2, 0xefbe4786384f25e3, 0x0fc19dc68b8cd5b5, 0x240ca1cc77ac9c65, 
                0x2de92c6f592b0275, 0x4a7484aa6ea6e483, 0x5cb0a9dcbd41fbd4, 0x76f988da831153b5, 0x983e5152ee66dfab, 
                0xa831c66d2db43210, 0xb00327c898fb213f, 0xbf597fc7beef0ee4, 0xc6e00bf33da88fc2, 0xd5a79147930aa725, 
                0x06ca6351e003826f, 0x142929670a0e6e70, 0x27b70a8546d22ffc, 0x2e1b21385c26c926, 0x4d2c6dfc5ac42aed, 
                0x53380d139d95b3df, 0x650a73548baf63de, 0x766a0abb3c77b2a8, 0x81c2c92e47edaee6, 0x92722c851482353b, 
                0xa2bfe8a14cf10364, 0xa81a664bbc423001, 0xc24b8b70d0f89791, 0xc76c51a30654be30, 0xd192e819d6ef5218, 
                0xd69906245565a910, 0xf40e35855771202a, 0x106aa07032bbd1b8, 0x19a4c116b8d2d0c8, 0x1e376c085141ab53, 
                0x2748774cdf8eeb99, 0x34b0bcb5e19b48a8, 0x391c0cb3c5c95a63, 0x4ed8aa4ae3418acb, 0x5b9cca4f7763e373, 
                0x682e6ff3d6b2b8a3, 0x748f82ee5defb2fc, 0x78a5636f43172f60, 0x84c87814a1f0ab72, 0x8cc702081a6439ec, 
                0x90befffa23631e28, 0xa4506cebde82bde9, 0xbef9a3f7b2c67915, 0xc67178f2e372532b, 0xca273eceea26619c, 
                0xd186b8c721c0c207, 0xeada7dd6cde0eb1e, 0xf57d4f7fee6ed178, 0x06f067aa72176fba, 0x0a637dc5a2c898a6, 
                0x113f9804bef90dae, 0x1b710b35131c471b, 0x28db77f523047d84, 0x32caab7b40c72493, 0x3c9ebe0a15c9bebc, 
                0x431d67c49c100d4c, 0x4cc5d4becb3e42b6, 0x597f299cfc657e2a, 0x5fcb6fab3ad6faec, 0x6c44198c4a475817


## 4. Compression

The message is broken into 1024-bit chunks. For each chunk, an 80-entry array
of 64-bit words is created. The chunk is copied into the first 16 words of the
array and these words are extended into the remaining words in the array.

    create an 80-entry message schedule array w[0..79] of 64-bit words
    copy chunk into first 16 words w[0..15] of the message schedule array
    
    Extend the first 16 words into the remaining 64 words w[16..80] of the message schedule array:
    for i from 16 to 79
        s0 := (w[i-15] rightrotate 1) xor (w[i-15] rightrotate 8) xor (w[i-15] rightshift 7)
        s1 := (w[i-2] rightrotate 19) xor (w[i-2] rightrotate 61) xor (w[i-2] rightshift 6)
        w[i] := w[i-16] + s0 + w[i-7] + s1
        
The bits in each default hash value are manipulated through bitwise operations, compressing the chunk. The compressed chunk
is then added to each hash value. The compression portion of the algorithm can be expressed through this diagram:

![sha512](https://user-images.githubusercontent.com/90664097/171306658-59844bd2-55c8-4c1a-87eb-170cfc26708e.png)

     a := h0
     b := h1
     c := h2
     d := h3
     e := h4
     f := h5
     g := h6
     h := h7
     
     for i from 0 to 79
        S1 := (e rightrotate 14) xor (e rightrotate 18) xor (e rightrotate 41)
        ch := (e and f) xor ((not e) and g)
        temp1 := h + S1 + ch + k[i] + w[i]
        S0 := (a rightrotate 28) xor (a rightrotate 34) xor (a rightrotate 39)
        maj := (a and b) xor (a and c) xor (b and c)
        temp2 := S0 + maj
 
        h := g
        g := f
        f := e
        e := d + temp1
        d := c
        c := b
        b := a
        a := temp1 + temp2
        
     h0 := h0 + a
     h1 := h1 + b
     h2 := h2 + c
     h3 := h3 + d
     h4 := h4 + e
     h5 := h5 + f
     h6 := h6 + g
     h7 := h7 + h
   
Remember, all these steps are performed on each chunk. After all the chunks are gone through, the hash is created.

In SHA-256:
* The message is broken into 512-bit chunks.
* The default hash values are 32 bits.
* There are 64 rounds.
* The array of round constants contains 64 32-bit words.
* The round constants are based on the first 64 primes.
* The message is padded such that it is 64 bits less than a multiple of 512.
* The shift and rotate amounts are different.

SHA-224 and SHA-384 are very similar to SHA-256. However, with SHA-224, the initial hash values are different and the message digest omits the eighth hash value. With SHA-384, the initial hash values are also different and the message digest omits the seventh and eighth hash values.

# How Secure is SHA?

The more bits a message digest has, the more difficult it is to break. Thus, SHA-512 is more secure than other hashing algorithms that output message digests that are comprised of fewer bits. SHA-2 was first published in 2001 and is still in use to this day. However, as computer processing becomes more advanced, SHA-2 hashing algorithms become more vulnerable to attacks, similar to what happened with previous SHA incarnations. Indeed, since 2016, digital certificate authorities have not been allowed to issue SHA-1-signed certificates. Nonetheless, SHA-2 is still considered to be the most secure hashing algorithm, even as SHA-3 was released in 2015. SHA-3 has not been made the industry standard because during its release, companies were in the middle of migrating from SHA-1 to SHA-2 and SHA-3 is slower on the software side. However, as computers become more powerful, we will likely see a transition from SHA-2 into SHA-3.
