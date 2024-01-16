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
