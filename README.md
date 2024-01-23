# 🤖 REINFORCEpy

Implementation of the [REINFORCEjs library](https://github.com/karpathy/reinforcejs/tree/master) from Kaparthy in Python. The original library has been implemented in JavaScript. The objective of this repository is to implement the RL algorithms and the demos in Python.

> Note that this is not a 1-to-1 implementation in Python. The idea is simply trying to develop similar algorithms and demos as shown in Kaparthy's library.

The current version looks as follows:

![version_0_0_1](imgs/version_0_0_1.png)


# 🏃 How to Run?

There are multiple parameters which can be chosen to set when running the `main.py`. An example call would look like this: 

```bash
python main.py \
    --seed=42 \
    --verbose=1 \
    --episodes=2 \
    --timesteps=10 \
    --grid_size=10 \
    --algo=value_iteration \
    --render_large=True \
    --render_with_values=True
```

All supported arguments are listed below: 

```
usage: 
  main.py [--seed] [--verbose] [--episodes] [--timesteps] [--grid_size] [--algo] 
          [--render_large] [--render_with_values]
```

| Argument | Help | Default | 
|----------|------|---------|
| `--seed` | random seed | $42$ |
| `--verbose` | verbosity level | $1$ | 
| `--episodes` | number of episodes | $1$ | 
| `--timesteps` | maximal number of timesteps | $1,000$ | 
| `--grid_size` | size of the gridworld | $10$ | 
| `--algo` | learning algorithm | `value_iteration` | 
| `--render_large` | render large gridworld | `False` | 
| `--render_with_values` | render gridworld with value estimates | `False` | 

## 📝 ToDo's

- [x] Implement the GridWorld environment
- [x] Implement random action selection
  - [ ] Add unit tests for random action selection
- [ ] Implement Value Iteration
  - [ ] Add unit tests for value iteration
- [ ] Implement Policy Iteration
  - [ ] Add unit tests for policy iteration
- [ ] Implement unit-test structure to easily add tests
- [ ] Implement [GridWorld DP](https://cs.stanford.edu/people/karpathy/reinforcejs/gridworld_dp.html)
