# SHA Encryption
##### By Steven Rakhmanchik and Israel Pina

## How to run
*(cause lets be honest that's all you're here for)*

### Usage:
```
$ python3 sha.py [bits] [message]            
```
Bits can be:     *224, 256, 384, 512*

Message can be:  *anything*

### Example:
```
$ python3 sha.py 256 "Hello World"
  
  a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e
```

We can check by using this website: *https://emn178.github.io/online-tools/sha512.html*

The hash comes out to be the same:  *a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e*


## "What did you guys make?"

We have replicated the SHA-512 encryption algorithm through a Python program.

### "How can I check if this works?"

Run our program in the terminal with a specific word or phrase and then run "echo "(same word or phrase)" | sha(bits)sum". Replace (bits) with 224, 256, 384, or 512 depending on which SHA version you used with our program. The two outputs should be the same.

### "How does it work?"

See our [PRESENTATION.md file](https://github.com/israelpina004/final_project_empirekillers/blob/master/PRESENTATION.md).

## "What's the homework?"

You can find our homework assignment in the [HOMEWORK.md file](https://github.com/israelpina004/final_project_empirekillers/blob/master/HOMEWORK.md).

*;) we do a little trolling ♡*
