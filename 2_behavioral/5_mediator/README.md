# Mediator Design Pattern

Mediator Design Pattern is a behavioral pattern that simplifies complex communication between multiple objects by centralizing their interactions into a single "mediator" object. Instead of objects communicating directly with each other (tight coupling), they communicate through the mediator, which routes messages to the appropriate components.


## Core concepts

1. Mediator: Defines the interface for communicating with colleague objects.

2. Concrete Mediator: Implements the mediator interface and coordinates communication between specific colleague objects. It knows all of its colleagues and their interdependencies.

3. Colleagues: The objects that communicate with one another only through the mediator. They do not know about each other.


## Real-World Analogy: Air Traffic Control

Think of airplanes approaching an airport. If every pilot had to communicate with every other pilot to figure out who is landing, taking off, or at what altitude, the system would be chaotic and dangerous. Instead, all pilots communicate solely with the Air Traffic Control Tower (the Mediator). The tower manages and coordinates the paths of all the planes.


## When to use it

* When a set of objects communicate in complex, well-defined, but hard-to-understand ways.

* When objects are difficult to reuse because they are tightly coupled to many other objects.

* When you want to customize the behavior of a system without subclassing numerous individual components.


| Advantages | Trade-offs |
|------------|------------|
| **Loose Coupling:** Reduces dependencies between colleague objects. | **God Object:** The mediator can become overly complex and difficult to maintain if it takes on too much business logic. |
| **Centralized Control:** Makes communication easier to track and change. | **Performance:** Indirection (routing messages through a central object) may introduce minor performance costs. |

