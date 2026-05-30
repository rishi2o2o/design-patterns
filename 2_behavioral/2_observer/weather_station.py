from abc import ABC, abstractmethod

class Subject(ABC):
    """The Subject interface handles attaching, detaching, and notifying observers."""
    @abstractmethod
    def attach(self, observer: 'Observer') -> None:
        pass

    @abstractmethod
    def detach(self, observer: 'Observer') -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass

class Observer(ABC):
    """The Observer interface defines the update action used by the Subject."""
    @abstractmethod
    def update(self, temperature: float, humidity: float) -> None:
        pass


# ------------------------------------------------------------------

class WeatherStation(Subject):
    """The Concrete Subject that maintains weather data and alerts observers."""
    def __init__(self) -> None:
        self._observers: list[Observer] = []
        self._temperature: float = 0.0
        self._humidity: float = 0.0

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"WeatherStation: Attached an observer ({type(observer).__name__}).")

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)
        print(f"WeatherStation: Detached an observer ({type(observer).__name__}).")

    def notify(self) -> None:
        print("WeatherStation: Notifying all registered observers...")
        for observer in self._observers:
            observer.update(self._temperature, self._humidity)

    def set_measurements(self, temperature: float, humidity: float) -> None:
        """Simulates changing weather conditions and triggers notifications."""
        print(f"\nWeatherStation: New measurements: {temperature}°C, {humidity}% humidity.")
        self._temperature = temperature
        self._humidity = humidity
        self.notify()


# ------------------------------------------------------------------

class MobileAppDisplay(Observer):
    """Concrete Observer 1: A mobile application rendering user-friendly text."""
    def update(self, temperature: float, humidity: float) -> None:
        print(f"📱 Mobile App Display -> Temp: {temperature}°C | Humidity: {humidity}%")

class WebDashboardDisplay(Observer):
    """Concrete Observer 2: A website dashboard tracking high-precision metrics."""
    def update(self, temperature: float, humidity: float) -> None:
        print(f"💻 Web Dashboard Display -> Logged data: T={temperature}, H={humidity}")



# ------------------------------------------------------------------

if __name__ == "__main__":
    # Create the publisher station
    weather_station = WeatherStation()

    # Create subscribers
    phone_app = MobileAppDisplay()
    web_dashboard = WebDashboardDisplay()

    # Register subscribers
    weather_station.attach(phone_app)
    weather_station.attach(web_dashboard)

    # Simulate weather updates (Both displays get notified)
    weather_station.set_measurements(24.5, 65.0)
    weather_station.set_measurements(26.0, 60.0)

    # Unsubscribe one observer dynamically
    weather_station.detach(phone_app)

    # Simulate another weather update (Only the website gets notified)
    weather_station.set_measurements(28.2, 55.0)


