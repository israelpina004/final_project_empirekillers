
# What's SHA-512?

SHA-512 is a hashing algorithm used to convert text into another string of text of a fixed length. Each SHA-512 string is 512 bits,
or 64 bytes, long, represented by a 128-digit hexadecimal number. It is used in email address hashing, password hashing, and blockchain projects. SHA-512 hashes cannot be "decrypted," as hashes do not encrypt data, and it is not reversible. Hashes are primarily used in authentication systems to be stored in place of plaintext passwords, so there is no need for them to be decryptable or reversible; in fact, it's a good thing they aren't. If a hacker were to get into a password database, they would not be able to do anything malicious if all there is are hashes of passwords. Here is an example of hashed text:

      Original Text: Special Military Operation
  
      SHA-512: 6300B1EDB81058D3BD705A9B5981600B6FFC9BE1F9E0CB36F0F6BD4B6EE41E3FAA609D16C0131451AD5EB2C392B284933C87BCDBDA52B32410A29E227DAB49DF

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
array and these words are extended into the remaining words in the array.

![algorithm1](https://user-images.githubusercontent.com/90664097/170410750-6dd7db11-45cf-4b68-b395-fc86b4f965ec.png)

The bits in each default hash value are manipulated through bitwise operations and thus
each word in the array is manipulated, compressing the chunk. The compressed chunk
is then added to each hash value. The compression portion of the algorithm can be expressed through this diagram:

![sha512](https://user-images.githubusercontent.com/90664097/171306658-59844bd2-55c8-4c1a-87eb-170cfc26708e.png)

After all the chunks are gone through, the hash is created.

In our program, we have implemented this very algorithm. We defined variables \_k and \_h, which are the array of round constants and the array of initial hash values, respectively.

![code1](https://user-images.githubusercontent.com/90664097/170411404-a225c8e1-c0c3-4ffb-a347-0ff28b418648.png)

We then take a plaintext message, prompted from the user, and append bits to it. The complicated compression step is then performed on the message.

# How Secure is SHA-512?

The more bits a message digest has, the more difficult it is to break. Thus, SHA-512 is more secure than other hashing algorithms that output message digests that are comprised of fewer bits. SHA-2 was first published in 2001 and is still in use to this day. However, as computer processing becomes more advanced, SHA-2 hashing algorithms become more vulnerable to attacks, similar to what happened with previous SHA incarnations. Indeed, since 2016, digital certificate authorities have not been allowed to issue SHA-1-signed certificates. Nonetheless, SHA-2 is still considered to be the most secure hashing algorithm, even as SHA-3 was released in 2015. SHA-3 has not been made the industry standard because during its release, companies were the middle of migrating from SHA-1 to SHA-2 and SHA-3 is slower on the software side. However, as computers become more powerful, we will likely see a transition from SHA-2 into SHA-3.
