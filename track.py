```python
from obstacles import Obstacle

class Track:
    def __init__(self, length, obstacles):
        self.length = length
        self.obstacles = obstacles

    def display_track(self):
        track_representation = '-' * self.length
        for obstacle in self.obstacles:
            track_representation = track_representation[:obstacle.position] + 'X' + track_representation[obstacle.position + 1:]
        print(track_representation)

if __name__ == "__main__":
    obstacles = [Obstacle(5, 1), Obstacle(15, 1), Obstacle(25, 1)]
    track = Track(30, obstacles)
    track.display_track()
```