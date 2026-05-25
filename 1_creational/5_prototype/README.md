# Prototype Design Pattern

Prototype design pattern is a creational pattern that lets you create new objects by copying (or cloning) an existing object rather than creating new instances from scratch. It is highly useful when the cost of creating a new object is prohibitively expensive or complex (e.g. executing multiple database queries or heavy calculations).

## Key Concepts

* Cloning: Instead of using the new keyword, the object duplicates its own state into a new instance.

* Prototype Interface: A common interface declares a clone() method. Classes that want to be cloned implement this method to return a copy of themselves.

* Shallow Copy vs Deep Copy: Shallow copy copies primitive fields, but keeps references to the same nested objects in memory while deep copy recursively creates independent copies of all nested/reference objects as well.

## When to use it

* Resource-Intensive Creation: Creating an object requires time-consuming tasks like loading massive datasets, resolving complex dependencies, or network calls.

* Avoid Subclassing: You want to avoid creating complex object-creation hierarchies that mirror your object classes.

* Dynamic Configurations: You have an object configured in a specific way and want to duplicate it without hardcoding its properties or state into the code.

## Real-World Example

Consider a GameCharacter class that loads hundreds of weapon textures, audio assets, and stats from a database. Instead of querying the database and parsing files every single time a new enemy spawns, the game loads the first enemy fully into memory (the prototype). When a new enemy appears, it simply clones the prototype enemy and tweaks specific attributes (like spawn location or color), which saves massive amounts of processing power.


