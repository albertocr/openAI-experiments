import gym
import numpy as np
import matplotlib.pyplot as plt

env = gym.make("Taxi-v2")

#Inicializacion de variables
Q=np.zeros([env.observation_space.n, env.action_space.n])
steps=0
alpha=0.2

episodes=[]
stepstotal=[]
rewards=[]

def run_episode(observation1, movement):   
    observation2, reward, done, info = env.step(movement) 
    Q[observation1,movement] += alpha * (reward + np.max(Q[observation2]) - Q[observation1,movement])   
    return done,reward, observation2

for episode in range (0,2000):
    episodes.append(episode)
    steps=0
    out_done=None
    reward = 0
    rewardstore=0
    observation = env.reset()
    print("OBSERVATION: ",observation)
    print("Initial state:")
    print(env.render()) # Shows initial state
    while out_done != True:
        steps+=1
        action = np.argmax(Q[observation])
        print("State ",observation,"value matrix Q: ",Q[observation])
        print("Maximum value on position ",action+1," of the list")
        print("Action: ",action)
        print(env.render()) 
        input("->")
        print(chr(27) + "[2J") # Deletes screen 
        out_done, out_totalreward, out_observation = run_episode(observation,action) 
        rewardstore += out_totalreward
        observation = out_observation
    rewards.append(rewardstore)
    stepstotal.append(steps)  
    print("Final state:")
    print(env.render()) # Shows end state
    print('Episode ',episode,' Reward:  ',rewardstore)
    
# Plot with steps by episode
plt.axis([0,2000,0,100])
plt.xlabel('Episodes')
plt.ylabel('Steps done')
plt.plot(episodes,stepstotal,color='blue')
plt.show()

# Plot with reward by episode
plt.axis([0,2000,-200,100])
plt.xlabel('Episodes')
plt.ylabel('Value reward')
plt.plot(episodes,rewards,color='red')
plt.show() 
