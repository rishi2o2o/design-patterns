# Iterator Design Pattern

Iterator design pattern is a behavioral design pattern that lets you traverse elements of a collection sequentially without exposing the collection's underlying data structure or internal representation.


## How it works

Instead of giving outside code direct access to its internal data, the collection (Aggregate) provides a dedicated object called an Iterator.

1. The Collection keeps track of its data and provides a method to create an iterator.

2. The Iterator handles the exact traversal logic (e.g., knowing what the "next" item is, or knowing when the collection has ended).


## Core Components

1. Iterator Interface: Defines the operations required to traverse the collection, such as next() and hasNext().

2. Concrete Iterator: Implements the Iterator interface and keeps track of the current position during traversal.

3. Aggregate (Collection) Interface: Defines the method to create/return an iterator.

4. Concrete Aggregate: Represents the actual data structure that creates an instance of the Concrete Iterator.


## Advantages of using it

* Decoupled Code: You separate the algorithm for navigating through data from the data structure itself.

* Uniform Interface: You can write a single traversal function that works across entirely different collection types (e.g., an array, a tree, or a graph) as long as they provide a standard iterator.


## Real-world example

Imagine you are building a music streaming app, and one of the features of the app is to be able to create a playlist. Users add songs to their playlists, and they should be able to iterate through the playlist to listen to the songs.

We have different ways of iterating over the playlist:

* Sequential iteration: going over the songs in the order they were added to the playlist.

* Shuffled iteration: going over the songs in a shuffled order.

* Favorite song iteration: only going over favorited songs from the playlist.

Instead of writing code for each iteration inside the Playlist class, Iterator pattern allows us to define Playlist iteration code separate from the Playlist data structure.





