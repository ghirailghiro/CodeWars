'''
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([False,1,0,1,2,0,1,3,"a"]) # returns[False,1,1,2,1,3,"a",0,0]
'''

def move_zeros(array):
    #your code here
    for i in range(len(array)):
        if type(array[i]) == float:
            array[i] = 0
    numOfZeros = sum(1 for item in array if (item == 0 and type(item) == int))
    
    array = [i for i in array if i is not 0]
    
    return array + [0 for i in range(numOfZeros)]