# Builder Design Pattern

The Builder design pattern is a creational design pattern that lets you construct complex objects step by step. It separates the object construction logic from its actual representation, allowing you to use the same creation process to produce different variations and configurations of an object.


## The Problem It Solves

When a class has too many optional attributes, developers often resort to two problematic approaches:

1. The Telescoping Constructor Anti-Pattern: Creating multiple overloaded constructors with increasingly longer parameter lists. This is error-prone, hard to read, and difficult to maintain.

2. Excessive Setter Methods: Instantiating an empty object and then calling numerous setter methods. This makes the object mutable, which is dangerous in multithreaded environments.


## Key Components

The classic implementation described by the Gang of Four involves following key actors:

* Product: The complex object that is being built.

* Builder Interface: Defines the abstract steps required to build the product.

* Concrete Builder: Implements the building steps and tracks the product configuration.

* Director (Optional): Controls the execution order of the construction steps to create predefined configurations.


## How It Works (Example)

Imagine ordering a custom Pizza

1. Start: You create a PizzaBuilder.

2. Add Parts: .setCrust("Thin"), .setToppings("Cheese, Peppers").

3. Finalize: Call .build() to receive your completed Pizza object.


## Common Use Cases

* Java: java.lang.StringBuilder.append()

* ORM Frameworks: Building complex SQL queries dynamically (e.g., .select().where().limit()).

* HTTP Clients: Configuring complex requests with headers, timeouts, and body data.


