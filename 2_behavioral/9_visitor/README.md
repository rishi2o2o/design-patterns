# Visitor Design Pattern

The Visitor Design Pattern is a behavioral design pattern that allows you to add new operations to an existing object structure without modifying its classes. It extracts algorithms from the elements they operate on and places them into external classes called visitors.

This pattern directly adheres to the Open/Closed Principle: your existing entity classes remain closed for modification but open for behavior extension.


## Core Components

The pattern relies on a structural mechanism called double dispatch, where the executed operation depends on both the type of the visitor and the type of the element being visited.

1. Element Interface: Declares an accept(Visitor v) method.

2. Concrete Elements: Classes that implement the element interface. Their accept method simply delegates the call back to the visitor by passing itself (visitor.visit(this)).

3. Visitor Interface: Declares a series of visit methods, overloading or naming one for each type of concrete element.

4. Concrete Visitors: Implementations of the visitor interface that contain the actual business logic or algorithm for each distinct element type.


## When to Use the Visitor Pattern

* Stable Object Structures: When you have an object hierarchy that rarely changes, but you frequently need to add new operations over those classes.

* Unrelated Operations: When you need to perform many unrelated operations across an object structure (e.g., exporting data, auditing, validating, or converting formats) and you want to avoid polluting the core entities.

* Complex Trees: When traversing complex syntax trees or hierarchical structures (like composite patterns or compiler ASTs).


## Real-World Examples

* Compilers: Compilers utilize abstract syntax trees (ASTs) and run different visitors across the tree for type-checking, code optimization, and code generation.

* Document Exporters: A complex document structure (Paragraphs, Images, Tables) can accept a PdfExportVisitor or an HtmlExportVisitor to render itself in various formats.

* File Systems: Traversing directories where a SizeCalculatorVisitor calculates total size and a VirusScannerVisitor checks files for security threats.



