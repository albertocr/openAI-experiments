# This programme solves the taxi v2 by using Q-Tables
import gym
import numpy as np

env = gym.make("Taxi-v2")

# Variables initialization
Q=np.zeros([env.observation_space.n, env.action_space.n])
alpha=0.2

def run_episode(observation1, movement):   
    observation2, reward, done, info = env.step(movement) 
    Q[observation1,movement] += alpha * (reward + np.max(Q[observation2]) - Q[observation1,movement])
    return done,reward, observation2

for episode in range (0,2000):
    out_done=None
    reward = 0
    rewardstore=0
    observation = env.reset()
    print("Initial state:")
    # print(env.render()) # Shows initial state
    while out_done != True:
        action = np.argmax(Q[observation])
        #print(env.render()) # Shows intermediate states
        out_done, out_totrwd, out_observation = run_episode(observation,action) 
        rewardstore += out_totrwd
        print ("intermediate reward: " + str(rewardstore))
        observation = out_observation
    print("Final state:")
    # print(env.render()) # Shows final state
    print('Episode ', episode,' Reward: ', rewardstore)
env.close()
