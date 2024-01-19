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

ACTION_SPACE = [0, 1, 2, 3]
ACTION_ARROW_MAPPING = {0: '↑', 1: '→', 2: '↓', 3: '←'}

# -----------------------------------------------------------------------------
def parse_args(args=None):
    parser = ArgumentParser(description='REINFORCEpy - GridWorld')

    parser.add_argument('--seed', type=int, default=42, help='random seed (default: 42)')
    parser.add_argument('--verbose', type=int, default=1, help='verbosity level (default: 1)')
    parser.add_argument('--episodes', type=int, default=1, help='number of episodes (default: 1)')
    parser.add_argument('--timesteps', type=int, default=1_000, help='number of maximal timesteps (default: 1,000)')                                                

    return parser.parse_args(args if args is not None else sys.argv[1:])



# -----------------------------------------------------------------------------
def main(args=None):
    args = parse_args(args)

    episodes_actions = []
    episodes_rewards = []

    # --- Run episodes ---
    for episode in range(args.episodes):

        env = GridWorld(size=10)
        state = env.reset()
        done = False

        timestep = 0
        cumulative_reward = 0 # Return
        
        episode_actions = []
        episode_rewards = []

        # --- Run timesteps ---
        # Run until done or maximal number of timesteps is reached.
        while not done:

            # Choose an action.
            action = env.action_space.sample()

            # Perform the action.
            state, reward, done = env.step(action)

            # All actions and rewards of this episode.
            episode_actions.append(action)
            episode_rewards.append(reward)

            cumulative_reward += reward
            
            if args.verbose == 1:
                env.render()
                print(f"s: {state}, a: {ACTION_ARROW_MAPPING.get(action)}, R: {reward}, Sum(R): {cumulative_reward} Done: {done}")

            timestep += 1
            if timestep == args.timesteps: 
                break

        # All actions and rewards of all episodes
        episodes_actions.append(episode_actions)
        episodes_rewards.append(episode_rewards)   

        print(f"Episode: {episode}")
        if done:
            print(f"{4*' '}Successfully finished after {timestep} steps. Sum(R): {cumulative_reward}")
        elif not done and (timestep == args.timesteps):
            print(f"{4*' '}Max num of timesteps {timestep} reached. Sum(R): {cumulative_reward}")
        else: 
            print(f"{4*' '}This shouldn't be a condition!")

    return episodes_actions, episodes_rewards

# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
