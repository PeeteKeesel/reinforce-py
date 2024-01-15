
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



class GridWorld:
    def __init__(self, size=10, walls=WALLS):
        """Initialize the gridworld. The default size is an in REINFORCEjs."""
        self.size = size
        self.walls = walls if walls else []
        self.reset()

    def reset(self):
        # Start position
        self.x = 0
        self.y = 0

        # Define the goal position
        self.goal_x = self.size - 1
        self.goal_y = self.size - 1

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

        if action == 0 and self.y > 0:  # Up
            new_y -= 1
        elif action == 1 and self.x < self.size - 1:  # Right
            new_x += 1
        elif action == 2 and self.y < self.size - 1:  # Down
            new_y += 1
        elif action == 3 and self.x > 0:  # Left
            new_x -= 1

        # Check if the new position is a wall
        print((new_x, new_y))
        print((new_x, new_y) in self.walls)
        print((2,2) in WALLS)
        print((2,3) in WALLS)
        if (new_x, new_y) in self.walls:
            reward = -10  # Negative reward for hitting a wall
            done = False
            print(f"hallo: x={self.x} y={self.y} new_x:{new_x} new_y:{new_y}")
        else:
            # Update position if it's not a wall
            self.x, self.y = new_x, new_y
            # Check if the goal is reached
            reward = 100 if (self.x, self.y) == (self.goal_x, self.goal_y) else -1
            done = (self.x, self.y) == (self.goal_x, self.goal_y)

        return (self.x, self.y), reward, done

    def render(self):
        """
            A : agent
            G : goal
            . : empty space
        """
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) == (self.x, self.y):
                    print('A', end=' ')
                elif (i, j) == (self.goal_x, self.goal_y):
                    print('G', end=' ')
                elif (i, j) in WALLS:
                    print('#', end=' ')
                else:
                    print('.', end=' ')
            print()
