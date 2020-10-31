'''
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
'''
def pig_it(text):
    #your code here
    
    listOfWords = text.split()
    
    listToReturn = [i[1:]+i[0]+"ay" for i in listOfWords]
    stringToReturn = ""
    for j in listToReturn:
        stringToReturn += j +" "
    size = len(stringToReturn)
    if(stringToReturn[size-4] == "!" or stringToReturn[size-4] == "?"):
        stringToReturn = stringToReturn[:-2]
        
    return stringToReturn[:-1]