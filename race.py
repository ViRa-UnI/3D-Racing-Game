```python
from bike import Bike
from track import Track

class Race:
    def __init__(self, participants, track):
        self.participants = participants
        self.track = track
        self.winner = None

    def start(self):
        for bike in self.participants:
            bike.move()

    def end(self):
        for bike in self.participants:
            if bike.position >= self.track.length:
                self.winner = bike
                break

    def check_winner(self):
        if self.winner:
            return f"The winner is {self.winner.name}"
        else:
            return "The race is still on"

    def display_race(self):
        self.track.display_track()
        for bike in self.participants:
            print(f"Bike {bike.name} is at position {bike.position}")
```