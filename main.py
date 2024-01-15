# main.py

import sys

from src.environments.grid_world import GridWorld
# from src.agents.q_learning import QLearningAgent
# from src.utils.logger import Logger


# -----------------------------------------------------------------------------
def main():
    env = GridWorld(size=10)
    state = env.reset()
    done = False

    i = 0
    actions = [1,1,2,2,2,2]

    while not done:

        # Determine the action (for example, from an RL agent)
        action = actions[i] 

        # Take the action.
        state, reward, done = env.step(action)

        # Render the environment.
        env.render()
        
        print(f"State: {state}, Reward: {reward}, Done: {done}")
        i += 1
        if i == 5: 
            break

# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
