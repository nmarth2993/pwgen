PATH = 'words_short.txt'
SPECIALS = '!@#$%^&*()+-/:;<=>?{|}~' # note: not all special chars but enough
from string import digits as DIGITS

UPPERCASE_WEIGHT = 1 - .1 # 10% chance for an uppercase character

MIN_INS_LEN = 2
MAX_INS_LEN = 3

PHRASE_LEN = 3

import random

def load_words(path: str) -> list:
    words = []
    with open(path) as wordlist:
        for line in wordlist:
            words.append(line[:-1])
    print(f'[info] loaded {len(words)} words\n')
    return words

def randomcase(s: str) -> str:
    return ''.join([char.upper() if random.random() >= UPPERCASE_WEIGHT else char for char in s])

def genpw(words: list) -> str:
    """
    Generate a passphrase defined by the below steps:
    1. Generate a string of PHRASE_LEN words (lowercase)
        a. To ensure uppercase characters are included, the first word shall contain an uppercase at a random index
    2. Apply random capitalization using UPPERCASE_WEIGHT
    3. Insert INS_MIN_LEN <= N <= INS_MAX_LEN random digits at a random index
    4. Perform the same operation as above, this time inserting random special characters
    """

    # the first word is forced to have a random character to ensure that the password
    # has at least one uppercase character
    first_word = random.choice(words)
    upper_idx = random.randint(0, len(first_word) - 1)
    first_word = first_word[:upper_idx] + first_word[upper_idx].upper() + first_word[upper_idx + 1:]

    # generate N-1 additional words to create the whole phrase
    pwstring = first_word + ''.join(random.choices(words, k=PHRASE_LEN-1))
    # print(f'passphrase: {pwstring}')

    pwstring = randomcase(pwstring)

    strlen = len(pwstring)
    
    digits_idx = random.randint(0, strlen - 1)

    # to somewhat spread out the digits and the special characters, the string is split
    # and the special characters are inserted into a random index on the larger half of the string

    if digits_idx > strlen // 2:
        # add specials on lower half of string
        specials_idx = random.randint(0, digits_idx - 1)
        
        # generate number of chars to insert
        num_chars = random.randint(MIN_INS_LEN, MAX_INS_LEN)

        specials_str = ''.join(random.choices(SPECIALS, k=num_chars))

        # insert the characters
        special_half = pwstring[:specials_idx] + specials_str + pwstring[specials_idx:digits_idx]

        # now inserting the digits string
        # again, generate the string to insert
        num_chars = random.randint(MIN_INS_LEN, MAX_INS_LEN)
        digits_str = ''.join(random.choices(DIGITS, k=num_chars))

        digit_half = digits_str + pwstring[digits_idx:]

        # print("specials lower half; digits higher half")
        pwstring = special_half + digit_half

    else:
        # add specials on higher half of string
        specials_idx = random.randint(digits_idx + 1, strlen - 1)

        # insert special string
        num_chars = random.randint(MIN_INS_LEN, MAX_INS_LEN)
        specials_str = ''.join(random.choices(SPECIALS, k=num_chars))
        special_half = specials_str + pwstring[specials_idx:]

        # insert digits string
        num_chars = random.randint(MIN_INS_LEN, MAX_INS_LEN)
        digits_str = ''.join(random.choices(DIGITS, k=num_chars))
        digit_half = pwstring[:digits_idx] + digits_str + pwstring[digits_idx:specials_idx]

        # print("digits lower half; specials higher half")
        pwstring = digit_half + special_half
    
    # print(f"digit: {digit_half} special: {special_half}")


    return pwstring

if __name__ == '__main__':
    words = load_words(PATH)

    num_pw = input('number of passwords to generate (q to quit): ')

    while num_pw != 'q':
        if not num_pw.isnumeric():
            continue
        
        num_pw = int(num_pw)
        for _ in range(num_pw):
            print(genpw(words))

        num_pw = input('number of passwords to generate (q to quit): ')
