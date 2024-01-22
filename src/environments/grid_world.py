
"""NOTES 
- Start is in (0,0)
- Goal is in the center () - reward +1
    - If achieved, agent is reset to (0,0)
"""

import random

# The following wall positions are as in 
#   https://cs.stanford.edu/people/karpathy/reinforcejs/gridworld_td.html
WALLS = [
    (2, 1), 
    (2, 2), 
    (2, 3), 
    (2, 4),
    (2, 6), 
    (2, 7), 
    (2, 8),
    (2, 2), 
    (3, 4), 
    (4, 4),
    (5, 4), 
    (6, 4),
    (7, 4)        
]

NEGATIVE_STATES = [
    (3,3),
    (4,5),
    (4,6),
    (5,6),
    (5,8),
    (6,8),
    (7,6),
    (7,5),
    (7,3),    
    (4,6)
]

RED_BACKGROUND = '\033[41m'     # Red background for negative states
GREEN_BACKGROUND = '\033[42m'   # Green background for the goal
WHITE_BACKGROUND = '\033[47m'   # White background for other states
GREY_BACKGROUND = '\033[100m'   # Grey background for walls
BLUE_BACKGROUND = '\033[44m'   # Blue background for the agent
RESET = '\033[0m'               # Reset to default


class GridWorld:
    def __init__(self, size=10, walls=WALLS):
        """Initialize the gridworld. The default size is an in REINFORCEjs."""
        self.size = size
        self.walls = walls if walls else []
        self.action_space = self.ActionSpace()
        self.gamma = 0.9  # discount factor
        self.states = [(x, y) for x in range(self.size) for y in range(self.size)]

        self.reset()

    def get_states(self):
        return self.states

    class ActionSpace:
        def __init__(self):
            # Define the action space: 0 = up, 1 = right, 2 = down, 3 = left
            self.actions = [0, 1, 2, 3]
            self.UP = 0
            self.RIGHT = 1
            self.DOWN = 2
            self.LEFT = 3

            self.action_to_direction = {
                0: '↑', 
                1: '→', 
                2: '↓', 
                3: '←'
            }
            self.direction_to_action = {
                '↑': 0, 
                '→': 1, 
                '↓': 2, 
                '←': 3
            }
            self.action_to_description = {
                0: 'UP', 
                1: 'RIGHT', 
                2: 'DOWN', 
                3: 'LEFT'
            }

        def sample(self):
            return random.choice(self.actions)

    def get_actions(self, state):
        return self.action_space.actions

    def reset(self):
        # Start position
        self.x = 0
        self.y = 0

        # Define the goal position
        self.goal_x = 5
        self.goal_y = 5

        return (self.x, self.y)

    def step(self, action):
        """ Perform an action in the environment
            action: 
                0 = up, 
                1 = right, 
                2 = down, 
                3 = left
        """
        new_x, new_y = self.x, self.y  # Set current position as default

        if action == self.action_space.UP and self.x > 0:  # Up
            new_x -= 1
        elif action == self.action_space.RIGHT and self.y < self.size - 1:  # Right
            new_y += 1
        elif action == self.action_space.DOWN and self.x < self.size - 1:  # Down
            new_x += 1
        elif action == self.action_space.LEFT and self.y > 0:  # Left
            new_y -= 1

        # Check if the new position is a wall
        if (new_x, new_y) in self.walls:
            # print(f"{4*' '}Ive tried to walk into a wall.")
            reward = 0  # Reward for hitting a wall
            done = False
        else:
            # Update position if it's not a wall
            self.x, self.y = new_x, new_y
            # Check if the goal is reached
            if (self.x, self.y) == (self.goal_x, self.goal_y):
                reward = 1
            elif (self.x, self.y) in NEGATIVE_STATES:
                reward = -1
            else: 
                reward = 0
            done = (self.x, self.y) == (self.goal_x, self.goal_y)

        return (self.x, self.y), reward, done
    
    def simulate_action(self, state, action):
        """Get the reward for a given state and action, w/o taking the action."""
        x, y = state[0], state[1]  # Set current position as default
        new_x, new_y = x, y  # Set current position as default

        if action == self.action_space.UP and x > 0:  # Up
            new_x -= 1
        elif action == self.action_space.RIGHT and y < self.size - 1:  # Right
            new_y += 1
        elif action == self.action_space.DOWN and x < self.size - 1:  # Down
            new_x += 1
        elif action == self.action_space.LEFT and y > 0:  # Left
            new_y -= 1

        print(f"(new_x, new_y): {(new_x, new_y)}   self.size: {self.size}")

        if (new_x, new_y) in self.walls:
            print(f"{4*' '}Ive tried to walk into a wall after {self.action_space.action_to_description.get(action)}.")
            # New is old since we couldnt move.
            new_x, new_y = x, y 
            reward = 0  # Reward for hitting a wall
            done = False
        else:
            # Update position if it's not a wall
            # self.x, self.y = new_x, new_y
            # Check if the goal is reached
            if (new_x, new_y) == (self.goal_x, self.goal_y):
                reward = 1
            elif (new_x, new_y) in NEGATIVE_STATES:
                reward = -1
            else: 
                reward = 0
            done = (new_x, new_y) == (self.goal_x, self.goal_y)

        return (new_x, new_y), reward, done

    def get_transition_prob(self, state, action):
        return 1.0

    def render(self):
        """
            A : agent
            G : goal
            . : empty space
        """
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) == (self.x, self.y):
                    print(BLUE_BACKGROUND + ' A ' + RESET, end='')
                elif (i, j) == (self.goal_x, self.goal_y):
                    print(GREEN_BACKGROUND + ' G ' + RESET, end='')
                elif (i, j) in WALLS:
                    print(GREY_BACKGROUND + '   ' + RESET, end='')
                elif (i, j) in NEGATIVE_STATES:
                    print(RED_BACKGROUND + ' . ' + RESET, end='')
                else:
                    print(WHITE_BACKGROUND + ' . ' + RESET, end='')
            print()
