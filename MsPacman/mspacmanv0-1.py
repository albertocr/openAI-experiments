# This programme solves the taxi v2 by using Q-Tables
import gym
import numpy as np

env = gym.make("MsPacman-v0")

state=env.reset()

# Info about the environment
# print ("shape of the state: " + str(state.shape))
# print ("state: " + str(state))
# env.render()
# print("action space: " + str(env.action_space.n))
# print ("action menaning: " + str(env.env.get_action_meanings()))

reward, info, done = None, None, None
while done != True:
    state, reward, done, info = env.step(env.action_space.sample())
    env.render()

env.close()
