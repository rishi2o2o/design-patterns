# Chain of Responsibility Design Pattern

Chain of Responsibility is a behavioral design pattern that allows you to pass a request along a chain of handler objects. When a request is received, each handler decides either to process it or pass it to the next handler in the sequence.


## Why use it?

* Decoupling: It prevents coupling the sender of a request to its specific receiver, allowing multiple objects to handle the request without the sender needing to know who ultimately processes it.

* Flexibility: You can easily add, remove, or reorder handlers at runtime without modifying the client code.

* Single Responsibility: It helps keep your code modular, as each handler focuses on a specific condition or task.


## Real-world examples

* Bank Loan Approvals: A system where an associate can approve loans up to $5000. If a loan is for $10,000, the associate forwards the request to a manager, who can approve up to $15,000, and so on.

* Middleware in Web Frameworks: An HTTP request passes through a sequence of middleware (e.g., authentication, logging, payload parsing). Each middleware handles its job or passes the request to the next step.

* Support Ticket Systems: A ticket is handled by Level 1 support. If they lack the access to fix it, they pass it to Level 2, and so forth.


## Key Components

1. Handler Interface: Defines a standard interface for handling requests and usually includes a reference to the next handler in the chain.

2. Concrete Handlers: The individual classes that contain the logic to process specific types of requests. If the handler can process the request, it does so; otherwise, it passes it to the next object.

3. Client: Initiates the request by passing it to the first handler in the chain.

