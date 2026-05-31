# Template Method Design Pattern

Template Method Design Pattern is a behavioral software design pattern that defines the skeleton of an algorithm in a base class while allowing subclasses to override specific steps without changing the overall structure.

It acts like a structural blueprint or recipe: the sequence of operations is strictly locked down by the parent class, but individual steps can be customized by the child classes.


## Key components

* Abstract Class: Defines the core template method and declares the individual steps as abstract or default helper methods.

* Template Method: The primary method that outlines the exact execution sequence. It is often marked final or non-virtual to prevent child classes from changing the execution order.

* Abstract Steps: Placeholder methods with no implementation in the base class; subclasses must implement them.

* Hook Steps: Methods that contain a default or empty implementation. Subclasses can optionally override them to inject additional behavior.

* Concrete Subclasses: Classes that implement or override the required steps to provide specific behaviors while trusting the base class to run them in order.


## Real-world example

A classic example is building a data-parsing pipeline where the process (Open -> Extract -> Parse -> Close) always remains identical, but the file formats vary.


## Pros and cons of using this pattern

| Pros | Cons |
|-------------------|----------------------|
| **Maximizes Code Reuse:** Eliminates duplicate boilerplate code by anchoring common logic in the superclass. | **Rigid Architecture:** Modifying the fundamental steps of the overarching algorithm can break all existing subclasses. |
| **Inversion of Control:** Often referred to as the "Hollywood Principle" ("Don't call us, we'll call you") because the parent framework manages when to call the subclass logic. | **Inheritance Overhead:** Requires strict object-oriented inheritance. Languages with single-inheritance restrictions consume their one base slot here. |
| **Controlled Customization:** Offers localized extendability exclusively inside permitted "hook" or abstract methods, preserving core security. | **Complex Maintenance:** As the number of steps grows, debugging the execution flow split across parents and children gets difficult. |


## Template method vs. Strategy pattern

These behavioral patterns are frequently confused because they both manage interchangeable algorithms, but they operate at different levels:

* Template Method: Relies on inheritance. It alters parts of an internal algorithm at compile time by extending a class.

* Strategy Pattern: Relies on composition and delegation. It alters the entire algorithm at runtime by passing an object variant to a client.


