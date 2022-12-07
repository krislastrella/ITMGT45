#!/usr/bin/env python
# coding: utf-8

# In[21]:


def shift_letter(letter, shift):
    '''Shift Letter. 
    4 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.
    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "
    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.
    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 
    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if letter == " ":
        return " "
    else:
        unicode = ord(letter)
        index = unicode - 65
        newindex = (index + shift) % 26
        newunicode=newindex+65
        representation = chr(newunicode)
        return representation


# In[23]:


def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    6 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.
    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 
    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    encryptedmessage =""
    for letter in message.upper():
        if letter.isupper():
            unicode = ord(letter)
            index = unicode - 65
            newindex = (index + shift) % 26
            newunicode=newindex+65
            representation = chr(newunicode)
            encryptedmessage = encryptedmessage + representation
        else: 
            encryptedmessage += letter
    return encryptedmessage
caesar_cipher("MEAMORE", 42)


# In[28]:


def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    4 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.
    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "
    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.
    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if letter == " ":
        return " "
    else:
        unicode = ord(letter)
        unicode2 = ord(letter_shift)
        if unicode == unicode2:
            return letter
        elif unicode < unicode2:
            shift = unicode2-unicode
            index = unicode - 65
            newindex = (index + shift) % 26
            newunicode=newindex+65
            representation = chr(newunicode)
            return representation
        else:
            shift = unicode2-unicode
            index = unicode - 65
            newindex = (index + shift) % 26
            newunicode=newindex+65
            representation = chr(newunicode)
            return representation
shift_by_letter(" ", "B")


# In[9]:


def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    6 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.
    Example:
    vigenere_cipher("A C", "KEY") -> "K A"
    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".
    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.
    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    message = message.upper()
    key = key.upper()
    keylen = len(key)
    keyunicode = [ord(i) for i in key]
    messageunicode = [ord(i) for i in message]
    encryptedmessage = ''
    for i in range(len(message)):
        if   65 <= ord(message[i]) <=90:
            new = (messageunicode[i] + keyunicode[i % keylen]) % 26
            encryptedmessage += chr(new + 65)
        else:
            encryptedmessage += message[i]
    return encryptedmessage
vigenere_cipher("A C", "KEY")

