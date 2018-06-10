# This example makes two movements with the taxi, just to show the env. and actions behaviour

import gym
import numpy as np

env = gym.make("Taxi-v2")
observation=env.reset()
# We see the value returned when reseting the env.
print(observation)

# Available taxi actions
actions=env.action_space
print (actions)

env.render()

# Taxi movements
action=1 # Move up (north) the taxi
observation, reward, done, info = env.step(action)
print (env.step(action))
env.render()

action=2 # Move right (east) the taxi
observation, reward, done, info = env.step(action)
print (env.step(action))

# Show the currrent environment state
env.render()
env.close()
