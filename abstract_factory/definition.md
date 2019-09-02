## Intent
Provide an interface for creating families of related or dependent objects without specifying their concrete classes.
A hierarchy that encapsulates: many possible "platforms", and the construction of a suite of "products".
The new operator considered harmful.

## Problem
If an application is to be portable, it needs to encapsulate platform dependencies.
These "platforms" might include: windowing system, operating system, database, etc.
Too often, this encapsulation is not engineered in advance, and lots of #ifdef case statements with options
for all currently supported platforms begin to procreate like rabbits throughout the code.

---

## Check list
Decide if "platform independence" and creation services are the current source of pain.
Map out a matrix of "platforms" versus "products".
Define a factory interface that consists of a factory method per product.
Define a factory derived class for each platform that encapsulates all references to the new operator.
The client should retire all references to new, and use the factory methods to create the product objects.

## Rules of thumb
Sometimes creational patterns are competitors: there are cases when either Prototype or Abstract Factory could be used profitably. At other times they are complementary: Abstract Factory might store a set of Prototypes from which to clone and return product objects, Builder can use one of the other patterns to implement which components get built. Abstract Factory, Builder, and Prototype can use Singleton in their implementation.
Abstract Factory, Builder, and Prototype define a factory object that's responsible for knowing and creating the class of product objects, and make it a parameter of the system. Abstract Factory has the factory object producing objects of several classes. Builder has the factory object building a complex product incrementally using a correspondingly complex protocol. Prototype has the factory object (aka prototype) building a product by copying a prototype object.
Abstract Factory classes are often implemented with Factory Methods, but they can also be implemented using Prototype.
Abstract Factory can be used as an alternative to Facade to hide platform-specific classes.
Builder focuses on constructing a complex object step by step. Abstract Factory emphasizes a family of product objects (either simple or complex). Builder returns the product as a final step, but as far as the Abstract Factory is concerned, the product gets returned immediately.
Often, designs start out using Factory Method (less complicated, more customizable, subclasses proliferate) and evolve toward Abstract Factory, Prototype, or Builder (more flexible, more complex) as the designer discovers where more flexibility is needed.

