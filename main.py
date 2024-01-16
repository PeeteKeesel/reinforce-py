# main.py

import sys

from src.environments.grid_world import GridWorld
# from src.agents.q_learning import QLearningAgent
# from src.utils.logger import Logger

NUM_EPISODES = 5
NUM_TIMESTEPS = 1000

ACTION_SPACE = [0, 1, 2, 3]
ACTION_ARROW_MAPPING = {0: '↑', 1: '→', 2: '↓', 3: '←'}

# -----------------------------------------------------------------------------
def main():
    env = GridWorld(size=10)
    state = env.reset()
    done = False

    timestep = 0
    curr_total_reward = 0

    while not done:

        # Choose an action.
        action = env.action_space.sample()

        # Perform the action.
        state, reward, done = env.step(action)

        curr_total_reward += reward
        env.render()
        
        print(f"s: {state}, a: {ACTION_ARROW_MAPPING.get(action)}, R: {reward}, Sum(R): {curr_total_reward} Done: {done}")
        timestep += 1
        if timestep == NUM_TIMESTEPS: 
            break

    if done:
        print(f"Successfully finished after {timestep} steps.")
        print(f"Total reward: {curr_total_reward}")

# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
