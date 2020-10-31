'''ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.'''

def rot13(message):
    cypherMessage = ""
    for i in message:
        if "a"<=i<="z" or "A"<=i<="Z":
            if "a"<=i<="z":
                if "a"<=chr(ord(i)+13)<="z":
                    cypherMessage += chr(ord(i)+13)
                else:
                    cypherMessage += chr(ord(i)+13-26)
            else:
                if "A"<=chr(ord(i)+13)<="Z":
                    cypherMessage += chr(ord(i)+13)
                else:
                    cypherMessage += chr(ord(i)+13-26)
        else:
            cypherMessage += i
            
    return cypherMessage
