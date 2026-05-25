# Singleton Pattern

The Singleton design pattern is a software design pattern that restricts the instantiation of a class to exactly one object.

It ensures two main things:

1. Single Instance: Only one instance of the class exists in the entire application.

2. Global Access: A central point of access is provided to retrieve that instance.


## When to use it

Developers use Singletons to manage shared resources efficiently and to coordinate system-wide actions. Common use cases include:

* Database Connections: Reusing a single connection pool to prevent resource overload.

* Configuration Settings: Sharing the same application settings across multiple components. 

* Logging Services: Directing all log messages to a single output stream.


## How it works

Implementing the pattern typically requires three steps to disable normal object creation:

1. Private Constructor: Prevents other classes from using the new keyword to create instances.

2. Private Static Variable: Holds the single instance of the class.

3. Public Static Method: Provides a global access point to check if the instance exists. If it does not exist, it creates one; if it does, it returns the existing one.

