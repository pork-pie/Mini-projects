import time
"""This function takes a dictionary where the keys are objects and the values are numbers.
It then returns all possible list with each key appearing the number of times indicated by its value
"""

#This function returns all lists of indecies 'number' items can have in a list of length 'length'
def possPositions(number,length):
    result=[]
    diff=length-number
    for i in range(diff+1):
        result.append([i])
    if number>1:
        diff+=2
        for k in range(number-1):  
            temp=[]  
            for i in result:
                for j in range(i[-1]+1,diff+k):                     
                    temp.append(i+[j])
            result=temp
    return result

#This is the main function 
def combos(objects):
    result = [[]]
    length = 0
    
    #This iterates over the key,value pairs 
    for key,value in objects.items():
        
        #We then adjust the list length to include our new values
        length+=value
        
        #We then find all positions we can put our value in our current result
        com = possPositions(value,length)
        temp=[]
        
        #We then insert value in all the posible possitions given by com for every list in result
        for x in result:
            for k in com:
                y=[m for m in x]
                for b in k: 
                    y.insert(b,key)
                temp.append(y)
        result=temp
        
    #We then return our result
    return result

#example input will generate all lists with 2 a's 1 b and 2 c's 
print(combos({"a":2,"b":1,"c":2}))
