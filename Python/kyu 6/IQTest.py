'''Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

##Examples :

iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd'''

def iq_test(numbers):
    #your code here
    position = 0
    
    listOfNumbers = numbers.split()
    
    numberOfEvan = 0
    numberOfOdd = 0
    
    size = len(listOfNumbers)
    
    for i in listOfNumbers:
        if (int(i) % 2 == 0):
            numberOfEvan += 1
        else:
            numberOfOdd += 1
            
    if(numberOfEvan == 1):
        for j in range(size):
            if (int(listOfNumbers[j]) % 2 == 0):
                position = j
                break
    else:
        for j in range(size):
             if (int(listOfNumbers[j]) % 2 != 0):
                position = j
                break
            
            
    return position+1