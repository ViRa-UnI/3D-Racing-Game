```python
class Obstacle:
    def __init__(self, position, size):
        self.position = position
        self.size = size

    def display_obstacle(self):
        obstacle_representation = "O" * self.size
        print(f"Obstacle at position {self.position}: {obstacle_representation}")
```