# Observer Design Pattern

Observer design pattern is a behavioral pattern where one object (the Subject) maintains a list of dependent objects (the Observers) and automatically notifies them of any state changes. It establishes a "one-to-many" relationship so that when the subject's data updates, all dependents are dynamically updated.


## Core Components

1. Subject (Publisher/Observable): Holds the actual data or state. It keeps a list of registered observers and provides methods for them to subscribe (attach) or unsubscribe (detach).

2. Observer (Subscriber/Listener): Defines an interface or abstract class that includes an update method. This ensures that any object that wants to be notified can receive the broadcast.

3. ConcreteSubject: A specific implementation of the Subject. When its state changes, it loops through its registered observers and triggers the update method.

4. ConcreteObserver: A specific implementation of the Observer that performs custom logic or acts upon receiving an update (e.g., refreshing a user interface).


## Real-world example

Consider a Weather Station (the Subject) and multiple Display Devices (the Observers) such as a mobile app, a TV screen, and a web dashboard.

1. The display devices "subscribe" to the Weather Station.

2. The Weather Station continuously monitors the temperature.

3. When the temperature changes, the Weather Station sends a broadcast (calls the update method) to all subscribed devices.

4. The mobile app updates its graphical display, while the TV updates a text ticker, reacting independently based on their own internal logic.


## Advantages of using it

* Loose Coupling: The subject doesn't need to know the specific details of the observers; it only knows they implement a standard interface. This makes the code modular and easier to maintain.

* Dynamic Updates: You can add or remove observers at runtime without changing the subject's code.

* Event-Driven Architecture: It perfectly facilitates publish-subscribe (pub-sub) systems, allowing your application to react to events (e.g., a stock price change, a button click, or a new video upload).


