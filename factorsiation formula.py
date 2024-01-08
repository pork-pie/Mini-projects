'''
This code takes a number and returns its prime factorisation in the form of a dictionay,
with the keys being the primes that divide the number and the values being the number of times the prime divides the number 
'''
def factorise(inputNumber):
    uppBoundSquared=inputNumber
    factorList={}
    if inputNumber != 1:
        factorPower=1
        factorUppBound=uppBoundSquared**0.5
        while (factorUppBound:=int(factorUppBound))**2==uppBoundSquared:
            uppBoundSquared=factorUppBound
            factorUppBound**=0.5
            factorPower*=2

        if (uppBoundSquared:=int(uppBoundSquared))%2==0:
            timesDivides=factorPower
            uppBoundSquared/=2
            while (uppBoundSquared:=int(uppBoundSquared))%2==0:
                uppBoundSquared/=2
                timesDivides+=factorPower
            factorList[2]=timesDivides
            if uppBoundSquared!=1:
                factorUppBound=uppBoundSquared**0.5
                while (factorUppBound:=int(factorUppBound))**2==uppBoundSquared:
                    uppBoundSquared=factorUppBound
                    factorUppBound**=0.5
                    factorPower*=2
                    
        possibleFactor=3
        while possibleFactor<=factorUppBound:
            if uppBoundSquared%possibleFactor==0:
                timesDivides=factorPower
                uppBoundSquared/=possibleFactor
                while (uppBoundSquared:=int(uppBoundSquared))%possibleFactor==0:
                    uppBoundSquared/=possibleFactor
                    timesDivides+=factorPower
                factorList[possibleFactor]=timesDivides
                if uppBoundSquared!=1:
                    factorUppBound=uppBoundSquared**0.5
                    while (factorUppBound:=int(factorUppBound))**2==uppBoundSquared:
                        uppBoundSquared=factorUppBound
                        factorUppBound**=1/2 
                        factorPower*=2
            possibleFactor=possibleFactor+2
    if uppBoundSquared!=1:
        factorList[uppBoundSquared]=factorPower
    return factorList
                      
        
    