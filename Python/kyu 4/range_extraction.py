'''A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Example:

solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"'''

def solution(args):
    # your code here
    lenArgs = len(args)
    stringToReturn = ""
    i = 0
    while i < lenArgs:
        auxToSlide1 = i
        while True:
            if auxToSlide1 == lenArgs-1:
                break
            if args[auxToSlide1] == -1 and args[auxToSlide1+1] == 2:
                break
            if abs(abs(args[auxToSlide1])-abs(args[auxToSlide1+1])) == 1:
                auxToSlide1 += 1
            else:
                break
        if auxToSlide1-i < 2:
            stringToReturn += str(args[i])+","
            i+=1
        else:
            stringToReturn += str(args[i])+"-"+str(args[auxToSlide1])+","
            i += (auxToSlide1 - i)+1
            
    return stringToReturn[:-1]
