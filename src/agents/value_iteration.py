

import numpy as np
import random
import pdb


class QTable:
    """A class representing a Q-table.

    A data structure used to estimate the rewards (Q-values) for
    state-action pairs. Is updated iteratively as the agent explores
    the environment and learns the optimal policy.
    """

    def __init__(self, size, actions):
        self.size = size
        self.actions = actions
        self.q_table = np.zeros((size, size, len(actions)))

    def get_max_Q(self, state, actions):
        """Gets the maximum Q-value for a given state from the Q-values for
        all actions from that state.
        """
        max_Q = -np.inf
        best_actions = []

        for action in actions:
            Q = self.get_Q_value(state, action)
            if Q > max_Q:
                max_Q = Q
                best_actions = [action]
            elif Q == max_Q:
                best_actions.append(action)

        return random.choice(best_actions), max_Q

    def get_Q_value(self, state, action):
        """Gets the Q-value for a given state-action pair."""
        return self.q_table[state][action]

    def set_Q_value(self, state, action, value):
        """Sets the Q-value for a given state-action pair."""
        self.q_table[state][action] = value


class ValueIteration:
    """
    A class representing the value iteration algorithm.
    
    A model-free, off-policy, iterative algorithm for finding the optimal
    value function and optimal policy for a given Markov Decision Process.
    """
    def __init__(self, mdp, initial_values):
        self.mdp = mdp
        self.values = initial_values
        self.x_dim = self.values.shape[0]
        self.y_dim = self.values.shape[1]

        for wall in self.mdp.walls:
            self.values[wall] = -np.inf

    def value_iteration(self, max_iterations=10, theta=0.001):
        """Run value iteration algorithm to find the optimal value function.

        The optimal value function is the value function that maximizes
        the expected return.

        Args:
            max_iterations (int, optional): 
                Maximum number of iterations. Each iteration update the value
                estimates for all states.
                Defaults to 10.
            theta (float, optional): Convergence threshold. 
                Defaults to 0.001.
        """
        Q_table = QTable(self.mdp.size, self.mdp.action_space.actions)

        # Set all walls to -np.inf.
        for wall in self.mdp.walls:
            for action in self.mdp.action_space.actions:
                Q_table.set_Q_value(wall, action, -np.inf)

        new_values = np.zeros((self.mdp.size, self.mdp.size))
        for wall in self.mdp.walls:
            new_values[wall] = -np.inf

        for i in range(max_iterations):
            delta = 0.0
            for state in self.mdp.get_states():
                feasible_actions = self.mdp.get_feasible_actions(state)
                for action in feasible_actions:
                    next_state, reward, _ = self.mdp.simulate_action(state, action)

                    V_s = self.values[state]
                    V_s_next = (
                        self.values[next_state]
                        if not self.mdp.is_goal_state(state)
                        else 0.0
                    )

                    # Estimate the Q-value (state-action value).
                    Q_table.set_Q_value(
                        state,
                        action,
                        self.mdp.get_transition_prob(state, action)
                            * (
                                reward + 
                                    self.mdp.gamma * V_s_next
                            ),
                    )

                _, max_Q_s_a = Q_table.get_max_Q(state, feasible_actions)
                delta = max(delta, abs(max_Q_s_a - V_s))

                new_values[state] = max_Q_s_a

            # Update the value estimates.
            self.values = new_values.copy()

            # Print values in the 10x10 grid world
            print()
            for i in range(10):
                for j in range(10):
                    value = self.values[(i, j)]
                    formatted_value = f"{value:0.2f}"
                    print(f" {formatted_value} ", end="")
                print()
            print()

            # Check for convergence.
            if delta < theta:
                break

        # Print values in the 10x10 grid world
        print()
        for i in range(10):
            for j in range(10):
                value = self.values[(i, j)]
                formatted_value = f"{value:0.2f}"
                print(f" {formatted_value} ", end="")
            print()
        print()

    def _get_best_actions(self, state):
        """Return a list of best actions for a given state."""
        if self.mdp.is_goal_state(state):
            return [] 
        
        max_V = -np.inf
        best_actions = []

        for action in self.mdp.get_feasible_actions(state):
            nxt_state, _, _ = self.mdp.simulate_action(state, action)
            if nxt_state == state:
                continue
            V_nxt = self.values[nxt_state]
            if V_nxt > max_V:
                max_V = V_nxt
                best_actions = [action]
            elif V_nxt == max_V:
                best_actions.append(action)

        print([self.mdp.action_space.action_to_direction.get(a) for a in best_actions])

        return best_actions

    def get_best_action(self, state):
        """Randomly choose from all the best actions for a given state, if
        there are more then one. Otherwise simply return the best action."""
        return random.choice(self._get_best_actions(state))

    def get_all_best_actions(self, state):
        """Return all the best actions for a given state."""
        return self._get_best_actions(state)

    def derive_policy(self):
        """Derive the optimal policy from the optimal value function after
        value iteration has been run.
        """
        
        # Note that there can be multiple optimal actions per state, namely
        # those with the same value. In this case, we choose one of them at
        # random.
        optimal_policy = {} # np.zeros((self.mdp.size, self.mdp.size, len(self.mdp.action_space.actions)))

        for i in range(self.x_dim):
            for j in range(self.y_dim):
                state = (i, j)
                optimal_actions = self.get_all_best_actions(state)
                optimal_policy[state] = optimal_actions

        print('policy:')
        print(optimal_policy)

        return optimal_policy