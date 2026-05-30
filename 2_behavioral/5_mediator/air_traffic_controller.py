# The Mediator Interface
class AirTrafficControl:
    def notify(self, sender, event):
        pass

# The Concrete Mediator
class ControlTower(AirTrafficControl):
    def __init__(self):
        self.planes = []

    def register_plane(self, plane):
        self.planes.append(plane)

    def notify(self, sender, event):
        if event == "land":
            print(f"Tower: {sender.name} is cleared to land.")
            # Coordinate with other planes
            for p in self.planes:
                if p != sender:
                    p.receive("Adjust altitude")

# The Colleague
class Airplane:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator
        self.mediator.register_plane(self)

    def send(self, event):
        print(f"{self.name} sending event: {event}")
        self.mediator.notify(self, event)

    def receive(self, message):
        print(f"{self.name} received message: {message}")

# Usage
if __name__ == "__main__":
    tower = ControlTower()
    plane1 = Airplane("Flight 101", tower)
    plane2 = Airplane("Flight 205", tower)

    plane1.send("land")


