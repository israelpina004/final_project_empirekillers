
# What's SHA-512?

SHA-512 is a hashing algorithm used to convert text into another string of text of a fixed length. Each SHA-512 string is 512 bits,
or 64 bytes, long, represented by a 128-digit hexadecimal number. It is used in email address hashing, password hashing, and blockchain projects, among other things. SHA-512 hashes cannot be "decrypted," as hashes do not encrypt data, and it is not reversible. Here is an example of hashed text:

  $ Original Text:  Special Military Operation
  $ SHA-512:        6300B1EDB81058D3BD705A9B5981600B6FFC9BE1F9E0CB36F0F6BD4B6EE41E3FAA609D16C0131451AD5EB2C392B284933C87BCDBDA52B32410A29E227DAB49DF

# How SHA-512 Works

The SHA-512 algorithm can be separated into four steps.

## 1 and 2. Appending bits

The plaintext message to be hashed is padded with bits such that its length
is 128 bits less than a multiple of 1024. The padded bits start with a 1 and 
end in a stream of 0s that end once the message is at a satisfactory length.

The remaining bits are added by taking the modulo of the message block by 2^64
and appending that to the end of the message block.

## 3. Setting up default values and round constants

Default hash values are initialized by taking the first 64
bits of the fractional parts of the square roots of the first eight prime
numbers.

An array of 80 "round constants," which contains the first 64 bits of
the fractional parts of the cube roots of the first 80 prime
numbers, is initialized.

## 4. Compression

The message is broken into 1024-bit chunks. For each chunk, an 80-entry array
of 64-bit words is created. The chunk is copied into the first 16 words of the
array and these words are extended into the remaining words in the array
through a xor algorithm.

![xoring](https://user-images.githubusercontent.com/90664097/170178248-ffa48bba-6c1e-4171-847a-9e6234347bfe.png)

The bits in each default hash value are manipulated and used to in turn
manipulate each word in the array, compressing the chunk. The compressed chunk
is then added to each hash value. 

After all the chunks are gone through, the hash is created.
