
#Q3

import re                                          
with open('about.txt','r') as file:
    contents =file.read()
    string = re.sub('[^a-zA-Z\d\s]', '', contents)                                                    
    x=string.split()                              
    ans = max(x,key=x.count)                       
    print("Most frequently used word is:",ans)

