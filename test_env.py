import gymnasium as gym

env = gym.make('gymnasium_env/GridWorld-v0')
observation, info = env.reset()

for _ in range(100):
    action = env.action_space.sample()  # Random action
    observation, reward, terminated, truncated, info = env.step(action)
    
    if terminated or truncated:
        print("Episode finished!")
        observation, info = env.reset()

env.close()