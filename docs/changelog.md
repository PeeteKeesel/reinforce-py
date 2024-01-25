> The objective of this page is to describe the performed changes for this project.

# CHANGELOG

Value Iteration

* [X] (`24.01.2024`) Implement _value iteration_
* [X] (`25.01.2024`) Derive the optimal policy after running value iteration
  * [X] (`25.01.2024`) If there are multiple optimal actions per state, choose randomly
* [ ] Add unit tests for value iteration
* [ ] Compare value iteration with random action selection

Policy Iteration

* [ ] Implement _policy iteration_ algorithm
* [ ] Add unit tests for policy iteration

Other

* [ ] Implement _epsilon-greedy_
  * [ ] Add as argument to `main.py`
* [ ] Try out _optimistic initial values_
* [ ] Plot expected total cumulative reward (y) per episode (x)

Environment

* [ ] Add unit tests for the 10x10 GridWorld
* [X] (`25.01.2024`) Update the arrows in the large rendering using the current optimal policy from the respective `algo`
* [ ] Change coloring of the states according to their value estimates
