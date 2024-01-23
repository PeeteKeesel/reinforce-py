

"""
Q-table 
    - there are 4 actions
    - there are 10x10 states
[
    [0. 0. 0. 0.], 
    [0. 0. 0. 0.],
    [0. 0. 0. 0.],
    ...
    [0. 0. 0. 0.],
] \in R^{10x10x4}
"""

import numpy as np
import random
import pdb


class QTable:
    def __init__(self, size, actions):
        self.size = size
        self.actions = actions
        self.q_table = np.zeros((size, size, len(actions)))

    def get_max_Q(self, state, actions):
        """Get the maximum Q-value for a given state."""
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
        """Get the Q-value for a given state-action pair."""
        return self.q_table[state][action]

    def set_Q_value(self, state, action, value):
        """Set the Q-value for a given state-action pair."""
        self.q_table[state][action] = value

class ValueIteration: 
    def __init__(self, mdp, initial_values):
        self.mdp = mdp
        self.values = initial_values

    def value_iteration(self, max_iterations=10, theta=0.001):

        Q_table = QTable(self.mdp.size, self.mdp.action_space.actions)
        new_values = np.zeros((self.mdp.size, self.mdp.size))

        for i in range(max_iterations):
            print(f"{4*' '}iteration: {i}")
            delta = 0.0

            for state in self.mdp.get_states():
                print(f"{8*' '}state: {state}")
                # pdb.set_trace()
                for action in self.mdp.get_actions(state):
                    print(f"{12*' '}action: {action}")

                    next_state, reward, _ = self.mdp.simulate_action(state, action)
                    print(f"REWARD: {reward}")
                    V_s = self.values[state]
                    V_s_next = self.values[next_state]

                    # Calculate the Q-value.
                    Q_table.set_Q_value(
                        state, 
                        action, 
                        self.mdp.get_transition_prob(state, action) * \
                        (
                            reward + \
                            self.mdp.gamma * V_s_next
                        )
                    )

                max_a, max_Q_s_a = Q_table.get_max_Q(state, self.mdp.action_space.actions)
                print(f"max_a: {max_a}, delta: {delta}, max_Q_s_a: {max_Q_s_a}, V_s: {V_s}")
                delta = max(delta, abs(max_Q_s_a - V_s))

                new_values[state] = max_Q_s_a

                # pdb.set_trace()

            # pdb.set_trace()

            # Update the values.
            self.values = new_values

            # Check for convergence.
            if delta < theta:
                break

        # Print values in the 10x10 grid world
        print()
        for i in range(10):
            for j in range(10):
                value = self.values[(i,j)]
                formatted_value = f'{value:0.2f}'
                print(f' {formatted_value} ', end='')
            print()
        print()

    def get_best_action(self, state):
        """Get the best action for a given state."""
        print()
        for i in range(10):
            for j in range(10):
                # temp[i][j] = self.values[(i,j)]
                value = self.values[(i,j)]
                formatted_value = f'{value:.2f}'
                print(f' {formatted_value} ', end='')
            print()
        print()
        print(f"self.values[{state}]: {self.values[state]}") 

        # Check all feasible actions from here and return the best one.
        max_V = -np.inf
        best_actions = []

        for action in self.mdp.get_actions(state):
            nxt_state, _, _ = self.mdp.simulate_action(state, action)
            if nxt_state == state:
                print(self.mdp.action_space.action_to_direction.get(action))
                continue
            V_nxt = self.values[nxt_state]
            print(f"self.values[{nxt_state}]: {self.values[nxt_state]}")
            if V_nxt > max_V:
                max_V = V_nxt
                best_actions = [action]
            elif V_nxt == max_V:
                best_actions.append(action)

        print([self.mdp.action_space.action_to_direction.get(a) for a in best_actions])

        return random.choice(best_actions)