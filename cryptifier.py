MAX_KEY_SIZE = 26

def cipherOutput(shiftNumber, cipherChoice, encrypt_or_decrypt, inputEntry):  # use all the inputs from the GUI that were imported
    output = ""
    if cipherChoice == 'Caesar':

        if 1 <= int(shiftNumber) <= int(MAX_KEY_SIZE):  # if the shiftNumber is between 1 and 26 it will perform function of a positive shift

            if encrypt_or_decrypt == 'Encrypt':

                for symbol in inputEntry:  # for every character in the input
                    if symbol.isalpha():  # check if the symbol is ascii
                        num = ord(symbol)  # convert the character into its unicode number e.g A='65'
                        num += int(shiftNumber)  # add this number to the shift number
                        if symbol.isupper():  # if the symbol is upper case, and if its unicode number is under Z (last capital),
                            if num > ord('Z'):  # it will add or subtract 26 from the num making the unicode of the character different and hence a different character.
                                num -= 26
                            elif num < ord('A'):
                                num += 26
                        elif symbol.islower():
                            if num > ord('z'):
                                num -= 26
                            elif num < ord('a'):
                                num += 26
                        output += chr(num)  # output the num (which is currently in unicode form), into a readable character.
                    else:
                        output += symbol  # add the character to the output if its not in the alphabet
            elif encrypt_or_decrypt == 'Decrypt':  # runs the same thing as above, however the shift number starts negative as to reverse the process above.
                shiftNumber = -int(shiftNumber)
                output = ''
                for symbol in inputEntry:
                    if symbol.isalpha():
                        num = ord(symbol)
                        num += shiftNumber
                        if symbol.isupper():
                            if num > ord('Z'):
                                num -= 26
                            elif num < ord('A'):
                                num += 26
                        elif symbol.islower():
                            if num > ord('z'):
                                num -= 26
                            elif num < ord('a'):
                                num += 26
                        output += chr(num)
                    else:
                        output += symbol
            
        else:
            if encrypt_or_decrypt == 'Encrypt':  # this section of the code covers the case of a negative shift number same as above, just negative.

                for symbol in inputEntry:
                    if symbol.isalpha():
                        num = ord(symbol)
                        num += int(shiftNumber)
                        if symbol.isupper():
                            if num > ord('Z'):
                                num -= 26
                            elif num < ord('A'):
                                num += 26
                        elif symbol.islower():
                            if num > ord('z'):
                                num -= 26
                            elif num < ord('a'):
                                num += 26
                        output += chr(num)
                    else:
                        output += symbol
            elif encrypt_or_decrypt == 'Decrypt':
                shiftNumber = -int(shiftNumber)
                output = ''
                for symbol in inputEntry:
                    if symbol.isalpha():
                        num = ord(symbol)
                        num += shiftNumber
                        if symbol.isupper():
                            if num > ord('Z'):
                                num -= 26
                            elif num < ord('A'):
                                num += 26
                        elif symbol.islower():
                            if num > ord('z'):
                                num -= 26
                            elif num < ord('a'):
                                num += 26
                        output += chr(num)
                    else:
                        output += symbol

    elif cipherChoice == 'Vernam':
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # letters available to shift by.
        key = 'MARCO'  # Set a designated key.
        translated = []  # stores the encrypted/decrypted message string
        keyIndex = 0  # pointer of which character is being shifted on the list at a given time
        key = key.upper()  # keeps the key upper case.

        if encrypt_or_decrypt == 'Encrypt':
            for symbol in inputEntry:  # for every character in the input
                num = LETTERS.find(symbol.upper())
                if num != -1:  # -1 means symbol.upper() was not found in LETTERS
                    num += LETTERS.find(key[keyIndex]) # add to num every letter that is found in the key.
                    num %= len(LETTERS)  # handle the potential wrap-around
                    if symbol.isupper():  # add the encrypted/decrypted symbol to the end of translated.
                        translated.append(LETTERS[num])
                    elif symbol.islower():
                        translated.append(LETTERS[num].lower())
                    keyIndex += 1  # move to the next letter in the key

                    if keyIndex == len(key):  # when the pointer reaches the end of the key, there is no more to cipher.
                        keyIndex = 0

                else:
                    translated.append(symbol)  # The symbol was not in LETTERS, so add it to translated as is.

            output = ''.join(translated) # add all the ciphered characters to the final variable that will hold the entire cipher.
        elif encrypt_or_decrypt == 'Decrypt':  # same thing as above for decryption, however num is subtracted
            for symbol in inputEntry:
                num = LETTERS.find(symbol.upper())
                if num != -1:
                    num -= LETTERS.find(key[keyIndex])
                    num %= len(LETTERS)

                    if symbol.isupper():
                        translated.append(LETTERS[num])
                    elif symbol.islower():
                        translated.append(LETTERS[num].lower())
                    keyIndex += 1

                    if keyIndex == len(key):
                        keyIndex = 0
                else:
                    translated.append(symbol)
            output = ''.join(translated)

    return output


# Test the code here.
def test():
    """code to test cipherOutput"""
    shiftNumber = 0
    cipherChoice = 'Vernam'
    encrypt_or_decrypt = 'Decrypt'
    inputEntry = 'Test'
    translated = cipherOutput(shiftNumber, cipherChoice, encrypt_or_decrypt, inputEntry)
    print(translated)


if __name__ == "__main__":
    test()
