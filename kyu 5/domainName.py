#Write a function that when given a URL as a string, 
#parses out just the domain name and returns it as a string.
#examples:
#domain_name("http://github.com/carbonfive/raygun") == "github" 
#domain_name("http://www.zombie-bites.com") == "zombie-bites"
#domain_name("https://www.cnet.com") == "cnet"

def domain_name(url):
    stringToReturn = url
    
    if stringToReturn.find("www.") != -1:
        stringToReturn = stringToReturn.replace("www.","")
    if stringToReturn.find("http://") != -1:
        stringToReturn = stringToReturn.replace("http://","")
    if stringToReturn.find("https://") != -1:
        stringToReturn = stringToReturn.replace("https://","")
    
    return stringToReturn[:stringToReturn.find(".")]
    pass