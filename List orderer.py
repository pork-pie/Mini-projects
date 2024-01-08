"""
I did this project as I wanted to order a list based on preferance using the minimum amount of binary comparisions, 
sorting lists of colors being my main inspiration.
"""
import math as m

#This is the list I will be sorting
initialList=["red","blue","green","purple","yellow","orange","black","white","pink","brown","grey"]

#Setting the initial parameters for the returned list
sortedListLength=0
sortedList=[]

#This loop takes an element of our initial list and uses a bisection method to place it in our current sorted list 
for item in initialList:

    #We then find the initial midpoint of list, lower bound of list, and upper bound of list
    midpoint=m.floor((sortedListLength-1)/2)
    sortLowerBound=0
    sortUpperBound=sortedListLength

    """
    This while loop checks that the lower bound minus the upper bound is nonzero. 
    If it is zero this means the algorithm has converged onto a point, which is the list entry we should put our item
    """
    while sortLowerBound-sortUpperBound:

        """
        This if-else statement checks weather you prefer the midpoint of our bounded sorted list or 
        the item of the inital list currently being checked
        """
        if input(f"Do you prefer\n1) {item}\nor\n2) {sortedList[midpoint]}\n") == "1":

            """
            If we prefer item to midpoint then the item cannot be in a list position behind the midpoint so 
            the lower bound is greater than the midpoint
            """
            sortLowerBound=midpoint+1
        else:

            """
            If we don't prefer item to midpoint then the item cannot be in a list position ahead of the midpoint so 
            the lower bound is the midpoint, since putting our item in the midpoint position means it goes directly behind the current midpoint
            """
            sortUpperBound=midpoint

        #We then calculate the new midpoint using our new bounds 
        midpoint=m.floor((sortLowerBound+sortUpperBound)/2)

    #If the code has converged we insert the item into the converged index
    sortedList.insert(midpoint,item)

    #Since we have added an item the list length increaces by 1 
    sortedListLength+=1
    
#We return the final list
print(sortedList)

    
    

