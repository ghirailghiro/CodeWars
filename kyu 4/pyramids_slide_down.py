'''
Lyrics...
Pyramids are amazing! Both in architectural and mathematical sense. If you have a computer, you can mess with pyramids even if you are not in Egypt at the time. For example, let's consider the following problem. Imagine that you have a pyramid built of numbers, like this one here:

   /3/
  \7\ 4 
 2 \4\ 6 
8 5 \9\ 3
Here comes the task...
Let's say that the 'slide down' is the maximum sum of consecutive numbers from the top to the bottom of the pyramid. As you can see, the longest 'slide down' is 3 + 7 + 4 + 9 = 23

Your task is to write a function longestSlideDown (in ruby: longest_slide_down) that takes a pyramid representation as argument and returns its' largest 'slide down'. For example,

longestSlideDown([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]) => 23
By the way...
My tests include some extraordinarily high pyramids so as you can guess, brute-force method is a bad idea unless you have a few centuries to waste. You must come up with something more clever than that.

(c) This task is a lyrical version of the Problem 18 and/or Problem 67 on ProjectEuler. '''

def longest_slide_down(pyramid):
    # TODO: write some code...
    
    m = len(pyramid)
    base  = len(pyramid[m-1])
    matrixOfPy = []
    
    for i in range(m):
        matrixOfPy.append([])
        matrixOfPy[i] = [0]*base
        auxLenIPy = len(pyramid[i])
        for j in range(auxLenIPy):
            matrixOfPy[i][j] = pyramid[i][j]
              
    for i in range(m-2,-1,-1):
        for j in range(i+1):
            if(matrixOfPy[i+1][j] > matrixOfPy[i+1][j+1]):
                matrixOfPy[i][j] += matrixOfPy[i+1][j]
            else:
                matrixOfPy[i][j] += matrixOfPy[i+1][j+1]
            
        
    return matrixOfPy[0][0]
        
    pass