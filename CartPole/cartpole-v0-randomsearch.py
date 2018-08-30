import gym
from gym import wrappers
import numpy as np

def run_episode(env, parameters):
    observation = env.reset()
    totalreward = 0
    for intento in range(200):
        action = 0 if np.matmul(parameters,observation) < 0 else 1
        observation, reward, done, info = env.step(action)
        totalreward += reward
        if done:
            break
    return totalreward

env = gym.make('CartPole-v0')
env = wrappers.Monitor(env, 'CartPole1Results', force=True)

bestparams = None
parameters = None
bestreward = 0

for episodios in range(10000):
    parameters = np.random.rand(4) * 2 - 1
    reward = run_episode(env,parameters)
    print ("Episode ",episodios," finished with reward: ",reward)
    if reward > bestreward:
        bestreward = reward
        bestparams = parameters
        if reward == 200:
            break
input ("Press Enter to test the result of the learning")
for b in range(5000):
    run_episode(env,bestparams)
input ("Finished")
env.close()
