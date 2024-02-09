```python
class Bike:
    def __init__(self, speed=0, position=0):
        self.speed = speed
        self.position = position

    def move(self):
        self.position += self.speed

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        if self.speed > 0:
            self.speed -= 1
```