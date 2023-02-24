<div style="display:block;text-align:left"><img align="left" src="https://images.idgesg.net/images/article/2021/12/android-security-100913715-large.jpg?auto=webp&quality=85,70" border="0" style="width:156px;">

# Pattern Lock Cracker
this tool helps in solving android pattern lock bypass in CTFs

### How does the pattern lock works?
Really, the pattern lock is the SHA1 hash sequence of digits (0-8) with length from 3 (4 since Android 2.3.3) to 8.

Since Android does not allows the pattern to repeat "balls" and it does not use a salt when computing the SHA1 hash, 
it really takes a very short period of time to crack the hash and get the pattern.

The gesture board is a 3x3 matrix, and can be repressented as follows (each digit represents a "ball"):
```md
-------------------
| 0 |  | 1 |  | 2 |
-------------------
| 3 |  | 4 |  | 5 |
-------------------
| 6 |  | 7 |  | 8 |
-------------------
```

So if you set the pattern lock to `0 -> 1 -> 2 -> 5 -> 4`, the SHA1 hash will be output of `SHA1("\x00\x01\x02\x05\x04")`, 
and that is the hash to be cracked .

### Where can I find the hash?
The hash is stored at "/data/system/gesture.key", and (From a rooted device) can be downloaded as follows:
```sh
$ android-sdk-linux/platform-tools/adb pull /data/system/gesture.key
0 KB/s (20 bytes in 0.071s)

$ ls -l gesture.key
-rw-r--r-- 1 simran simran 20 ago 21 17:45 gesture.key
$
```

## Usage

Step 1 :
```sh
$ git clone https://github.com/simran-sankhala/Pattern-Lock-Cracker.git

$ cd Pattern-Lock-Cracker
```
Step 2 :
```sh
$ python3 xpl.py ./gesture.key
```

![](poc.png)
