import numpy as np
import matplotlib.pyplot as plt

def getSamplar():
    mu=np.random.normal(0,10)
    sd=abs(np.random.normal(5,2))
    getSample=lambda: np.random.normal(mu,sd)
    return getSample

def e_greedy(Q, e):
##################################################
#		Your code here
##################################################
    if (np.random.uniform(low=0, high=1) >= e):
        possible_actions = [key for key, value in Q.items() if value == max(Q.values())]
    else:
        possible_actions = list(Q.keys())
    action = np.random.choice(possible_actions)

    return action

def upperConfidenceBound(Q, N, c):
##################################################
#		Your code here
##################################################  
    if min(N.values()) == 0:
        # print('in min')
        possible_actions = [key for key, value in N.items() if value == 0]
        # print('** {}, {}'.format(t, action))
    else:
        t = sum(N.values())
        highest = max([value + c*((np.log(t)/N[key])**(.5)) for key, value in Q.items()])
        possible_actions = [key for key, value in Q.items() if value + c*((np.log(t)/N[key])**(.5)) == highest]
    action = np.random.choice(possible_actions)

    return action

def updateQN(action, reward, Q, N):
##################################################
#		Your code here
##################################################
    NNew = N.copy()
    NNew[action] = NNew[action] + 1
    # print("Old N {}\nNew N: {}\n".format(N, NNew))
    QNew = Q.copy()
    QNew[action] = QNew[action] + (reward - QNew[action])/NNew[action]
    # print("Old Q {}\nNew Q: {}\n".format(Q, QNew))

    return QNew, NNew

def decideMultipleSteps(Q, N, policy, bandit, maxSteps):
##################################################
#		Your code here
##################################################  
    actionReward = []
    for _ in range(maxSteps):
        action = policy(Q, N)
        reward = bandit(action)
        Q, N = updateQN(action, reward, Q, N)
        actionReward.append((action, reward))
    # print(Q)
    # print(N)
    # print(actionReward)
    return {'Q':Q, 'N':N, 'actionReward':actionReward}

def plotMeanReward(actionReward,label):
    maxSteps=len(actionReward)
    reward=[reward for (action,reward) in actionReward]
    meanReward=[sum(reward[:(i+1)])/(i+1) for i in range(maxSteps)]
    plt.plot(range(maxSteps), meanReward, linewidth=0.9, label=label)
    plt.xlabel('Steps')
    plt.ylabel('Average Reward')

def main():
    np.random.seed(2020)
    K=10
    maxSteps=1000
    Q={k:0 for k in range(K)}
    N={k:0 for k in range(K)}
    testBed={k:getSamplar() for k in range(K)}
    bandit=lambda action: testBed[action]()

    policies={}
    policies["e-greedy-0.5"]=lambda Q, N: e_greedy(Q, 0.5)
    policies["e-greedy-0.1"]=lambda Q, N: e_greedy(Q, 0.1)
    policies["UCB-2"]=lambda Q, N: upperConfidenceBound(Q, N, 2)
    policies["UCB-20"]=lambda Q, N: upperConfidenceBound(Q, N, 20)
    
    allResults = {name: decideMultipleSteps(Q, N, policy, bandit, maxSteps) for (name, policy) in policies.items()}
    for name, result in allResults.items():
        plotMeanReward(allResults[name]['actionReward'], label=name)
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',ncol=2, mode="expand", borderaxespad=0.)
    plt.show()
    


if __name__=='__main__':
    main()
