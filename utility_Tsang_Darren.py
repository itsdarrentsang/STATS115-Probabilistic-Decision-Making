def expect(xDistribution, function):
   
##################################################
#		Your code here
   expectation = 0
   for key, value in xDistribution.items():
        expectation += function(key) * value
##################################################  
   
   return expectation

def getSPrimeProbability(sPrime, action, s0Distribution, transitionTable):
   
##################################################
#		Your code here

   # without using expect() function
   # sPrimeProbability = 0
   # for key, value in s0Distribution.items():
   #    sPrimeProbability += transitionTable[key][action][sPrime] * value

   sPrimeProbability = expect(s0Distribution, lambda k: transitionTable[k][action][sPrime])

##################################################  

   return sPrimeProbability

def getEU(sPrimeDistributionGivenAction, utilityTable):

##################################################
#		Your code here

   # without using expect() function
   # eu = 0
   # for key, value in sPrimeDistributionGivenAction.items():
   #    eu += value * utilityTable[key]

   eu = expect(sPrimeDistributionGivenAction, lambda k: utilityTable[k])
##################################################  

   return eu


#############################################
###   Complete the main function below
#############################################

def main():
   s0Distribution={0:0.125, 1:0.25, 2:0.0625, 3:0.0625, 4:0.25, 5:0.25}
   utilityTable={0:2000, 1:-500, 2:100, 3:1000, 4:0, 5:-5000}
   # {s0:{a:{s':p}}}, p is the probability of the event (Start from s0, take action a, end up at s')
   transitionTable={0:{0:{0:1,1:0,2:0,3:0,4:0,5:0},\
                        1:{0:0.05,1:0.9,2:0.05,3:0,4:0,5:0},\
                        2:{0:0,1:0.05,2:0.9,3:0.05,4:0,5:0},\
                        3:{0:0,1:0,2:0.05,3:0.9,4:0.05,5:0},\
                        4:{0:0,1:0,2:0,3:0.05,4:0.9,5:0.05},\
                        5:{0:0.05,1:0,2:0,3:0,4:0.05,5:0.9}},\
                     1:{0:{0:0,1:1,2:0,3:0,4:0,5:0},\
                        1:{0:0,1:0.05,2:0.9,3:0.05,4:0,5:0},\
                        2:{0:0,1:0,2:0.05,3:0.9,4:0.05,5:0},\
                        3:{0:0,1:0,2:0,3:0.05,4:0.9,5:0.05},\
                        4:{0:0.05,1:0,2:0,3:0,4:0.05,5:0.9},\
                        5:{0:0.9,1:0.05,2:0,3:0,4:0,5:0.05}},\
                     2:{0:{0:0,1:0,2:1,3:0,4:0,5:0},\
                        1:{0:0,1:0,2:0.05,3:0.9,4:0.05,5:0},\
                        2:{0:0,1:0,2:0,3:0.05,4:0.9,5:0.05},\
                        3:{0:0.05,1:0,2:0,3:0,4:0.05,5:0.9},\
                        4:{0:0.9,1:0.05,2:0,3:0,4:0,5:0.05},\
                        5:{0:0.05,1:0.9,2:0.05,3:0,4:0,5:0}},\
                     3:{0:{0:0,1:0,2:0,3:1,4:0,5:0},\
                        1:{0:0,1:0,2:0,3:0.05,4:0.9,5:0.05},\
                        2:{0:0.05,1:0,2:0,3:0,4:0.05,5:0.9},\
                        3:{0:0.9,1:0.05,2:0,3:0,4:0,5:0.05},\
                        4:{0:0.05,1:0.9,2:0.05,3:0,4:0,5:0},\
                        5:{0:0,1:0.05,2:0.9,3:0.05,4:0,5:0}},\
                     4:{0:{0:0,1:0,2:0,3:0,4:1,5:0},\
                        1:{0:0.05,1:0,2:0,3:0,4:0.05,5:0.9},\
                        2:{0:0.9,1:0.05,2:0,3:0,4:0,5:0.05},\
                        3:{0:0.05,1:0.9,2:0.05,3:0,4:0,5:0},\
                        4:{0:0,1:0.05,2:0.9,3:0.05,4:0,5:0},\
                        5:{0:0,1:0,2:0.05,3:0.9,4:0.05,5:0}},\
                     5:{0:{0:0,1:0,2:0,3:0,4:0,5:1},\
                        1:{0:0.9,1:0.05,2:0,3:0,4:0,5:0.05},\
                        2:{0:0.05,1:0.9,2:0.05,3:0,4:0,5:0},\
                        3:{0:0,1:0.05,2:0.9,3:0.05,4:0,5:0},\
                        4:{0:0,1:0,2:0.05,3:0.9,4:0.05,5:0},\
                        5:{0:0,1:0,2:0,3:0.05,4:0.9,5:0.05}}}
   actionSpace=[0,1,2,3,4,5]
   stateSpace=[0,1,2,3,4,5]

   ##################################################
   #		Your code below
   ##################################################  

   sPrimeDistribution={aS:{sS:getSPrimeProbability(sS, aS, s0Distribution, transitionTable) for sS in stateSpace} for aS in actionSpace}
   EU={key:getEU(value, utilityTable) for key, value in sPrimeDistribution.items()}

   ##################################################
   #		Your code above
   ################################################## 

   print(EU)



if __name__ == '__main__':
   main()