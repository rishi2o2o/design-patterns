# Strategy Design Pattern

Strategy Design Pattern is a behavioral design pattern that allows you to define a family of algorithms, encapsulate each one, and make them interchangeable at runtime.


The pattern typically consists of three main parts:

* Strategy Interface: A common interface that defines how all supported algorithms should behave.

* Concrete Strategies: Different classes that implement the interface, each providing a specific version of the algorithm (e.g., Credit Card vs. PayPal).

* Context: The main class that uses a strategy. It maintains a reference to a strategy object and delegates the work to it.


## Real-World example

Payment Processing: An e-commerce site can use different "strategies" for payment, such as Credit Card, PayPal, or Bitcoin. The checkout system remains the same; only the payment method changes.


## Why use it?

* Open/Closed Principle: You can add new algorithms (strategies) without modifying the existing context code.

* Eliminate Conditionals: It helps get rid of massive if-else or switch blocks used to select different behaviors.

* Interchangeability: You can swap behaviors at runtime based on user input or environment factors.