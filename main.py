# main.py

import sys
import logging

from argparse import ArgumentParser
from src.environments.grid_world import GridWorld
# from src.agents.q_learning import QLearningAgent
# from src.utils.logger import Logger

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

NUM_EPISODES = 5
NUM_TIMESTEPS = 1000

ACTION_SPACE = [0, 1, 2, 3]
ACTION_ARROW_MAPPING = {0: '↑', 1: '→', 2: '↓', 3: '←'}

# -----------------------------------------------------------------------------
def parse_args():
    parser = ArgumentParser(description='REINFORCEpy - GridWorld')

    parser.add_argument('--seed', type=int, default=42, help='random seed (default: 42)')
    parser.add_argument('--verbose', type=int, default=1, help='verbosity level (default: 1)')
    parser.add_argument('--episodes', type=int, default=1, help='number of episodes (default: 1)')
    parser.add_argument('--timesteps', type=int, default=1_000, help='number of maximal timesteps (default: 1,000)')                                                

    return parser.parse_args()


# -----------------------------------------------------------------------------
def main():
    args = parse_args()

    # --- Run episodes ---
    for episode in range(args.episodes):

        env = GridWorld(size=10)
        state = env.reset()
        done = False

        timestep = 0
        cumulative_reward = 0

        # --- Run timesteps ---
        # Run until done or maximal number of timesteps is reached.
        while not done:

            # Choose an action.
            action = env.action_space.sample()

            # Perform the action.
            state, reward, done = env.step(action)

            cumulative_reward += reward
            
            if args.verbose == 1:
                env.render()
                print(f"s: {state}, a: {ACTION_ARROW_MAPPING.get(action)}, R: {reward}, Sum(R): {cumulative_reward} Done: {done}")

            timestep += 1
            if timestep == NUM_TIMESTEPS: 
                break

        print(f"Episode: {episode}")
        if done:
            print(f"{4*' '}Successfully finished after {timestep} steps. Sum(R): {cumulative_reward}")
        elif not done and (timestep == NUM_TIMESTEPS):
            print(f"{4*' '}Max num of timesteps {timestep} reached. Sum(R): {cumulative_reward}")
        else: 
            print(f"{4*' '}This shouldn't be a condition!")

# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
