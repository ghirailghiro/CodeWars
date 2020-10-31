'''
Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)'''

def alphabet_position(text):
    stringToReturn = ""
    
    for i in text:
        ascii= ord(i)
        
        if(97 <= ascii and ascii <= 122):
            stringToReturn += (str(ascii-96)+" ")
        elif (65 <= ascii and ascii <= 90):
            stringToReturn +=(str(ascii-64)+" ")
    stringToReturn = stringToReturn[:-1]     
    return stringToReturn
            
    pass