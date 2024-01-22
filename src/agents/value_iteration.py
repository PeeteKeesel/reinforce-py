

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


class ValueIteration: 
    def __init__(self, mdp, initial_values):
        self.mdp = mdp
        self.values = initial_values

    def value_iteration(self, max_iterations=10, theta=0.001):

        Q_table = np.zeros(
            (
                self.mdp.size, 
                self.mdp.size, 
                len(self.mdp.action_space.actions)
            )
        )

        for i in range(max_iterations):
            print(f"{4*' '}iteration: {i}")
            delta = 0.0

            for state in self.mdp.get_states():
                print(f"{8*' '}state: {state}")
                for action in self.mdp.get_actions(state):
                    print(f"{12*' '}action: {action}")

                    next_state, reward, _ = self.mdp.simulate_action(state, action)

                    V_s = self.values[state]
                    V_s_next = self.values[next_state]

                    # Calculate the Q-value.
                    Q_table[state, action] = self.mdp.get_transition_prob(state, action) * \
                        (
                            reward + \
                            self.mdp.gamma * V_s_next
                        )
                # print(Q_table.shape)
                # print(Q_table[state])
                # print(np.argmax(Q_table[state]))
                best_action = np.argmax(Q_table[state])
                # print(f"best_action: {best_action}")
                # print(f"Q_table: {Q_table}")
                # print(f"state: {state}  best_action: {best_action}")
                # print(f"Q_table[{state}] : {Q_table[state]}")
                # print(f"Q_table[{state}, {best_action}] : {Q_table[state][best_action]}")
                # print()
                max_Q_s_a = Q_table[state][best_action]
                print(f"delta: {delta}, max_Q_s_a: {max_Q_s_a}, V_s: {V_s}")
                delta = max(delta, abs(max_Q_s_a - V_s))

                self.values[state] = max_Q_s_a

                # print(self.values)

            # Change is small enough.
            if delta < theta:
                break

        # print as a table
        temp = np.zeros((10,10))
        for i in range(10):
            for j in range(10):
                temp[i][j] = self.values[(i,j)]
        print(temp)

    def get_best_action(self, state):
        """Get the best action for a given state."""
        return np.argmax(self.values[state])