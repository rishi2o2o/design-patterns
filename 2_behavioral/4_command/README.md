# Command Design Pattern

Command Design Pattern is a behavioral software design pattern that encapsulates a request or an operation as a stand-alone object. This transformation allows you to pass requests as arguments, queue or log them, and easily support undoable operations.

By turning an action into an object, you successfully decouple the object that triggers the action (the sender) from the object that actually knows how to perform it (the receiver).


## Core components

The pattern splits responsibility among four core actors:

1. Command Interface: Declares a single execution method, typically execute().

2. Concrete Command: Contains reference to a receiver and implements the command by delegating task to receiver. 

3. Invoker (Sender): Triggers the command execution method. It does not know how the work is completed, only that the command can execute.

4. Receiver: Contains the actual business logic to perform the task.


## Real-world example: Restaurant orders

A classic way to understand this pattern is by looking at a restaurant workflow:

1. Client (Customer): You place a specific request.

2. Invoker (Waiter): Takes your order on a piece of paper (the command object). The waiter does not need to know how to cook the meal. They just pass the paper along.

3. Command (Order Slip): Encapsulates your meal choice. It can be queued, rearranged, or discarded.

4. Receiver (Chef): Reads the order slip and performs the actual cooking.


## When to use it

* Undo/Redo systems: Storing executed commands in a stack makes rollback logic effortless.

* Macro recording: You can combine individual operations into a unified macro list.

* Task scheduling & Queues: Commands can be safely added to arrays, delayed, or processed on background threads.


## When to avoid

* Simple workflows: For direct CRUD operations or basic actions, this pattern introduces unnecessary boilerplate files and complexity.

* Overly tightly coupled apps: If components must strictly track execution data simultaneously, separating them can overcomplicate state synchronization.


