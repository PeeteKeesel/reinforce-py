# main.py

import sys
import logging
import numpy as np

from argparse import ArgumentParser
from src.environments.grid_world import GridWorld
from src.agents.value_iteration import ValueIteration
# from src.utils.logger import Logger

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

ACTION_SPACE = [0, 1, 2, 3]
ACTION_ARROW_MAPPING = {0: '↑', 1: '→', 2: '↓', 3: '←'}

import random

random.seed(1)

# -----------------------------------------------------------------------------
def parse_args(args=None):
    parser = ArgumentParser(description='REINFORCEpy - GridWorld')

    parser.add_argument('--seed', type=int, default=42, help='random seed (default: 42)')
    parser.add_argument('--verbose', type=int, default=1, help='verbosity level (default: 1)')
    parser.add_argument('--episodes', type=int, default=1, help='number of episodes (default: 1)')
    parser.add_argument('--timesteps', type=int, default=1_000, help='number of maximal timesteps (default: 1,000)')
    parser.add_argument('--grid_size', type=int, default=10, help='size of the gridworld (default: 10)')
    parser.add_argument('--algo', type=str, default='value_iteration', help='algorithm (default: value_iteration)')
    parser.add_argument('--render_large', type=bool, default=False, help='render large gridworld (default: False)')
    parser.add_argument('--render_with_values', type=bool, default=False, help='render gridworld with value estimates (default: False)')

    return parser.parse_args(args if args is not None else sys.argv[1:])



# -----------------------------------------------------------------------------
def main(args=None):
    args = parse_args(args)

    episodes_actions = []
    episodes_rewards = []

    # --- Run episodes ---
    for episode in range(args.episodes):

        env = GridWorld(size=args.grid_size)
        state = env.reset()
        done = False

        timestep = 0
        cumulative_reward = 0 # Return
        
        episode_actions = []
        episode_rewards = []


        # ----------------------- #
        # RANDOM ACTION SELECTION #
        # ----------------------- #
        if args.algo == 'random':
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

        # ----------------------- #
        # VALUE ITERATION #
        # ----------------------- #
        elif args.algo == 'value_iteration':
            

            # Initialize the value function.
            # values = {(x, y): 0 for x in range(args.grid_size) for y in range(args.grid_size)}
            values = np.zeros((args.grid_size, args.grid_size))

            env.render(large=args.render_large, values=values)

            # values[(args.grid_size - 1, args.grid_size - 1)] = 0
            print(values)

            # Initialize the value iteration algorithm.
            value_iteration = ValueIteration(mdp=env, 
                                             initial_values=values)

            # Run the value iteration algorithm.
            value_iteration.value_iteration(max_iterations=100, theta=0.001)

            curr_trajectory = []

            # Run until done or maximal number of timesteps is reached.
            while not done:

                # Choose an action.
                action = value_iteration.get_best_action(state)
                print("best action: ", env.action_space.action_to_direction.get(action))

                # Perform the action.
                state, reward, done = env.step(action)

                # All actions and rewards of this episode.
                episode_actions.append(action)
                episode_rewards.append(reward)

                cumulative_reward += reward
                
                if args.verbose == 1:
                    env.render(large=args.render_large, values=value_iteration.values)
                    print(f"s: {state}, a: {ACTION_ARROW_MAPPING.get(action)}, R: {reward}, Sum(R): {cumulative_reward} Done: {done}")

                if done:
                    break

                timestep += 1
                if timestep == args.timesteps: 
                    break

            print(f"episode_actions: {[env.action_space.action_to_direction.get(a) for a in episode_actions]}")

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
