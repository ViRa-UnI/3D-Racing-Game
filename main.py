```python
from bike import Bike
from race import Race
from track import Track

# Shared Variables
game_status = True
winner = None
bikes = [Bike() for _ in range(5)]  # Creating 5 bikes
track = Track()

def check_collision(bike, track):
    for obstacle in track.obstacles:
        if bike.position == obstacle.position:
            return True
    return False

def display_game():
    track.display_track()
    for bike in bikes:
        print(f"Bike at position {bike.position} with speed {bike.speed}")

def main():
    global game_status, winner
    race = Race(bikes, track)
    while game_status:
        for bike in bikes:
            bike.move()
            if check_collision(bike, track):
                game_status = False
                print("Game Over! Bike hit an obstacle.")
                break
            if bike.position >= track.length:
                game_status = False
                winner = bike
                break
        display_game()
    if winner:
        print(f"Congratulations! Bike {winner} has won the race.")

if __name__ == "__main__":
    main()
```