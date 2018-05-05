import gym 
env = gym.make('CartPole-v0')

for i_episode in range(20):
    observation = env.reset()
    recompensa=0
    for t in range(200):
        env.render()
        print(observation)
        action = env.action_space.sample()
        if action==0:
            print ("Value ",action," push left (moves right)")
        else:
            print ("Value ",action," push right (moves left)")
        observation, reward, done, info = env.step(action)
        recompensa=recompensa+reward
        if done:
            print ("Final step that provoke the end of the episode:")
            print(observation)
            print("Episode ",i_episode,"finalished on {} attemts".format(t+1))
            recompensa=recompensa+reward
            print ("Reward obtained: ",recompensa)
            break
    input ("End of the episode, press enter to continue")
env.close()
