## State Design Pattern

The state design pattern is a behavioral design pattern that allows an object to alter its behavior when its internal state changes. It makes the object appear as if it has changed its class, providing a clean, object-oriented alternative to complex if-else or switch-case statements.


## How it works

Instead of one main class handling all logic for every possible state, the state pattern encapsulates state-specific behavior into separate, isolated classes.

The pattern consists of three core components:

1. Context: The main object whose behavior changes. It maintains a reference to a concrete state object that defines its current behavior.

2. State Interface: A common interface or base class that defines the methods available in all states.

3. Concrete States: Multiple classes that implement the State interface. Each class contains the exact behavior required when the Context is in that specific state.

Whenever the context transitions to a new state, it swaps out the active state object, which automatically changes the way the context reacts to method calls.


## Real-World Use Case: Document Lifecycle

Consider a document in a content management system like Google Docs or WordPress. It can be in a Draft, Moderation, or Published state.

* Draft State: Allows authors to edit and delete; does not allow publishing without review.

* Moderation State: Allows reviewers to approve or reject; does not allow direct editing by the author.

* Published State: Makes the document read-only for the public.

Instead of writing massive if (state == "Draft") checks in the Document class, you create a DraftState, ModerationState, and PublishedState class. The Document delegates execution to the current state object.


## Why use state pattern?

* Single Responsibility Principle: It extracts large, messy state-machine logic into distinct, manageable classes.

* Open/Closed Principle: You can introduce new states easily without changing the context class or existing state classes.

* Dynamic Behavior: It allows objects to easily change their behavior at runtime by swapping the state reference.


## State vs Strategy pattern

While both patterns look structurally identical (using composition and delegation), their intent is different. The Strategy pattern usually encapsulates interchangeable algorithms that are typically passed to an object from the outside. In contrast, the State pattern handles the internal condition of an object, and the states themselves often trigger the transitions from one state to another.




