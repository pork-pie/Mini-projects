"""
This is an algorithm I have made that a person can play multi pile nim with, and it will never lose.
The way the game works is you have multiple piles containing different amounts of objects
each turn a player may take a nonzero amount of objects from any of these piles and the game ends
when a player takes the last object which will cause the other player to win. 
This algorithm makes use of the theory presented in this article https://en.wikipedia.org/wiki/Nim#Winning_positions
"""
from functools import reduce

#This is the size of the initial piles 
piles=[200,18,1,12]
print(piles)

#This function determines wether a game of nim is winning or not.
#If it returns 0 you want to go first else you want to go second.
nimsum = reduce(lambda x, y: x ^ y, piles)

#I decided to have each turn be a seperate function, this is the function for the algorithm's turn
def MyTurn(nimsum,piles):
    print("My turn")
    numbertaken = 0

    """
    This loop determines wich pile the algorithm can take the most items from. 
    It does this by finding the values that share the largest bits with the nimsum
    Based on the theory we only need to find a number which shares the biggest bit with the nimsum
    and this value must exist but in doing this we can end the game faster 
    """
    for index,value in enumerate(piles): 

        #This checks how big the bits the nimsum shares with the value are and assigns it if it is large
        if nimsum & value > numbertaken : 
            indexofnumbertaken=index
            numbertaken=nimsum & value

    #This determines how many items we take from that pile
    numbertaken-=numbertaken ^ nimsum

    #This takes those items from the pile
    piles[indexofnumbertaken] -= numbertaken
    if piles[indexofnumbertaken] == 0: piles.pop(indexofnumbertaken)
    print(f"I will take {numbertaken} objects from heap {indexofnumbertaken+1}\n{piles}\nYour turn")
    return piles

#This is the turn of the player 
def YourTurn(piles):
    #This allows the player to input their move
    pileindex=int(input("Which pile will you take from: "))
    numtaken=int(input("How many objects will you take: "))

    #These values are stored to make calculating the nimsum easier 
    oldPileSize=piles[pileindex-1]
    newPileSize=oldPileSize-numtaken

    #This then makes the players move
    if newPileSize: piles[pileindex-1] = newPileSize
    else: piles.pop(pileindex-1)
    print(piles)
    return (piles,newPileSize ^ oldPileSize)
#This is then the code that runs the game. We first determine if the algorithm wants to go first or second
if not nimsum: 
    print("I'll let you go first")
    piles,nimsum=YourTurn(piles)
else:
    print("I guess I'll go first")

#This then repeats the turns until there are no piles left
while piles:
    piles=MyTurn(nimsum,piles)
    piles,nimsum=YourTurn(piles)

#Due to the mathematics implimented the algorithm can't lose 
print("I win")

