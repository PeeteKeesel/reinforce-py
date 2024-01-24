For the[ GridWorld](https://cs.stanford.edu/people/karpathy/reinforcejs/gridworld_dp.html) case (which will be our initial implementation) the setup is described as

* **State space** : GridWorld has `10x10 = 100` distinct states. The start state is the top left cell. The gray cells are walls and cannot be moved to.
* **Actions** : The agent can choose from up to `4` actions to move around. In this example
* **Environment Dynamics** : GridWorld is deterministic, leading to the same new state given each state and action
* **Rewards** : The agent receives `+1` reward when it is in the center square (the one that shows $R$ `1.0`), and `-1` reward in a few states ($R$ `-1.0` is shown for these). The state with `+1.0` reward is the goal state and resets the agent back to start.

Note that the GridWorld states are indexed in the following matter, where a state `(i, j)` has `i` as the vertical and `j` as the horizontal axis.

```
(0,0) (0,1) ... (0,9)
(1,0) (1,1) ... (1,9)
...
(9,0) (9,1) ... (9,9)
```

## Learnings - Value Iteration

* In the GridWorld example when taking an action the _immediate reward_ is _always the same_. This is because in this example we have only assigned a single reward per state, which is the immediate reward for each action taken from this specific state.
  * Initially I made the error of using the reward of the next state as the reward in the Q-value calculation. This being said, I interpreted `r(s,a,s')` wrongly.
* How to handle walls? I decided to calculate `feasible actions` which only returns the actions feasible from a given state. This excludes walls. Another solution would have been to set values of wall states initially to `-np.inf`.
* When updating the value function use the _old_ value function to update a value of a state. Not the _new_ on (if there already is one). This being said, initially I forgot to `copy` and just set `self.values = new_values` such that `self.values` and `new_values` were referring to the same object.
* Value iteration also uses a Q-table. In the `10x10` grid world example the initial Q-table looks as follows:

```
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
```
