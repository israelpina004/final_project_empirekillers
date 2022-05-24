# How SHA-512 Works

The SHA-512 algorithm can be separated into four steps.

## 1. Appending bits

The plaintext message to be hashed is padded with bits such that its length
is 128 bits less than a multiple of 1024. The padded bits start with a 1 and 
end in a stream of 0s that end once the message is at a satisfactory length.

The remaining bits are added by taking the modulo of the message block by 2^64
and appending that to the end of the message block.

## 2. Setting up default values

Default values for different characters are initialized. (Sample image to be included.)

