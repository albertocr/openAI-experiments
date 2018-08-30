import gym
from gym import wrappers
import numpy as np

env = gym.make('CartPole-v0')
env = wrappers.Monitor(env, 'CartPole1Results', force=True)

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

noise_scaling = 0.1
parameters = np.random.rand(4) * 2 - 1  
bestreward = 0

for episode in range(10000):
    newparams = parameters + (np.random.rand(4) * 2 - 1)*noise_scaling
    reward = 0
    # reward = run_episode(env, newparams)
    episodes_per_update = 15
    for _ in range(episodes_per_update):  
      run = run_episode(env,newparams)
      reward += run
    print ("Episode ",episode," finished with reward: ",reward)
    if reward > bestreward:
        bestreward = reward
        parameters = newparams
        if reward == 200:
            break
env.close()
