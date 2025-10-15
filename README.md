# 247CTF_ExclusiveKey

## Problem Statement

> We XOR encrypted this file, but forgot to save the password. Can you recover the password for us and find the flag?

Along with the Problem Statement, you have to install the `exclusive_key` file which is a data file.

## Solution

Since we already know that the format of the flag is `247CTF{32-hex}` we first XOR the `exclusive_key` file with `247CTF{` as done in [clue.py](https://github.com/paarth2023/247CTF_ExclusiveKey/blob/main/clue.py)

Once we have done the XOR operation we get the following output

![[1.png]]

We can see that `<!DOCTY` which clearly shows that the file is an HTML document and will definitely contain `<!DOCTYP html>` 

***

On performing XOR between `<!DOCTYPE html>` and the `exclusive_key` you get the following output:

![[2.png]]

A little bit of the flag is seen in the rightmost column thus telling us that `<!DOTYPE html> ....` is the right payload to XOR with the file.

***

The next clue that we obtain is from scanning looking at the `xor_results.txt` 

After running 

```bash
strings xor_results | less
``` 

And searching for some familiar strings we come across

![[3.png]]

![[4.png]]

![[5.png]]

![[6.png]]

![[7.png]]

It is clear that `wiki` is repeated over and over for the entire file and it could be speculated that the file is an HTML document belonging to a random Wikipedia web page.

Hence we can select `35` characters after `<!DOCTY` from HTML of any random Wikipedia web page. 

The final payload that we need the XOR with the file is as follows

```
<!DOCTYPE html>\n<html class="client-nojs
```
## Final Answer

![[9.png]]

