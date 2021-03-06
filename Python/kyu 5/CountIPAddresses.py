'''
Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).

All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.

Examples
ips_between("10.0.0.0", "10.0.0.50")  ==   50 
ips_between("10.0.0.0", "10.0.1.0")   ==  256 
ips_between("20.0.0.10", "20.0.1.0")  ==  246
'''

def ips_between(start, end):
    if start > end:
        start,end=end,start
    firstiIP = start.split(".")
    secondiIP = end.split(".")
    sum = 0
    sum += (int(secondiIP[0])-int(firstiIP[0]))*(256*256*256)
    sum += (int(secondiIP[1])-int(firstiIP[1]))*(256*256)
    sum += (int(secondiIP[2])-int(firstiIP[2]))*(256)
    sum += (int(secondiIP[3])-int(firstiIP[3]))
    return abs(sum)