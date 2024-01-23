# pwgen

Simple password generator script to balance ease of typing and password security.
Inserts non-alphanumeric characters at random indexes to decrease effectiveness of rule-based attacks.

## Usage

```py
python3 pwgen.py
```

The script is a simple python input loop that prompts for a number of passwords to generate.

```
[info] loaded 2330 words

number of passwords to generate (q to quit): 3
sTrinGunc577o*=/vergalaxy
OniOns%|trangeim230press
inpUTu963Ps|(etcanVas

number of passwords to generate (q to quit): q
```

## Notes

The very short wordlist was provided to hashcat with the [One Rule to Rule Them All](https://github.com/NotSoSecure/password_cracking_rules) and none of the ~1000 hashes were cracked.

Brute force methods are not realistic due to C(85, 19) possible combinations (52 alpha, 10 digits, 23 special).

C(85, 19) ≈ 4.25e18

Using a SHA256 hash benchmark of 3270 MH/s on a modern CPU:

4.25e18/3.27e9 ≈ 1.3e9 seconds ≈ 41 years

Wolfram tells me this is a quarter of the orbital period of Neptune[!](https://www.wolframalpha.com/input?i=1.29969418960244648318042813455657492354740061162079510703363+%C3%97+10%5E9+seconds)

And this is only the lower bound (15 character passphrase + 4 extra characters)
