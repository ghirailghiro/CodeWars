'''
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
'''
def rgb(r, g, b):
    #your code here :)
    hexR = ""
    if (r > 255):
        hexR = "FF"
    elif (r < 0):
        hexR = "00"
    else:
        hexR = str(hex(r)).replace("x", "")
        if(len(hexR) >= 3):
            hexR = hexR[1:]
    hexG = ""
    if (g > 255):
        hexG = "FF"
    elif (g < 0):
        hexG = "00"
    else:
        hexG = str(hex(g)).replace("x", "")
        if(len(hexG) >= 3):
            hexG= hexG[1:]
    hexB = ""
    if (b > 255):
        hexB = "FF"
    elif (b < 0):
        hexB = "00"
    else:
        hexB = str(hex(b)).replace("x", "")
        if(len(hexB) >=3):
            hexB = hexB[1:]
            
    return (hexR+hexG+hexB).upper()
    pass