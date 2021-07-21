from hashlib import sha3_512
from string import printable

def base10(obj):
    """
    Converts some hash into base 10.
    """
    target = int(obj, 16)
    return target


def baseQ(n, b):
    """
    Convert base 10 into base b.
    """
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


def getHash(ctr):
    """
    Stringify ctr and sha3 512 hash then hexdigest.
    """
    m = sha3_512()
    string = str(ctr).encode('utf-8')
    m.update(bytes(string))
    ctr_hash = m.hexdigest()
    return ctr_hash


def mixing(original, mixed):
    """
    Mixes some list of values using another list of values.
    """
    index = [i for i in range(len(original))]
    for val, ind in zip(mixed, index):
        old = original[ind]
        original[ind] = original[val]
        original[val] = old
    return original


def decypher(hashing_string):
    """
    Create a list of letters, numbers, and symbols to be used to cypher a text.
    """
    result = printable
    letters = list(result)
    choices = len(letters)
    result_hash = baseQ(base10(getHash(hashing_string)), choices)
    letters = mixing(letters, result_hash)
    return letters


def encrypt(message, key):
    """
    Encrypt a message by converting the message into a base 10 number.
    """
    # Use the key to create the decypher text
    letters = decypher(key)
    choices = len(letters)
    secret = list(message)
    # Find the index of all the letters in the decypher text. 
    b = []
    for s in secret:
        b.append(letters.index(s))
    # Write the list of numbers into base 10
    total = 0
    for value, index in zip(b,[i for i in range(len(b))]):
        total += value*pow(choices, index)
    # Pass the base 10 number as encrypted text
    return total


def decrypt(number, key):
    """
    Decrypt a message by converting the number into base Q and mapping into
    printable letters.
    """
    number = int(number)
    # Use the key to get the decypher text
    letters = decypher(key)
    choices = len(letters)
    # Write the number in base of the number of choices (letters/numbers/etc)
    b = baseQ(number, choices)
    b.reverse()
    # Use decypher text to decrypt the number into words.
    message = ''
    for val in b:
        message += letters[val]
    return message
