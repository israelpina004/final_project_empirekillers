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
through a xor algorithm. (Attach pic here?)

The bits in each default hash value are manipulated and used to in turn
manipulate each word in the array, compressing the chunk. The compressed chunk
is then added to each hash value. 

After all the chunks are gone through, the hash is created.
