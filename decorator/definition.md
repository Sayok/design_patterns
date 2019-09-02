## Intent
Attach additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.
Client-specified embellishment of a core object by recursively wrapping it.
Wrapping a gift, putting it in a box, and wrapping the box.

## Problem
You want to add behavior or state to individual objects at run-time.
Inheritance is not feasible because it is static and applies to an entire class.

---

## Check list
Ensure the context is: a single core (or non-optional) component, several optional embellishments or wrappers, and an interface that is common to all.
Create a "Lowest Common Denominator" interface that makes all classes interchangeable.
Create a second level base class (Decorator) to support the optional wrapper classes.
The Core class and Decorator class inherit from the LCD interface.
The Decorator class declares a composition relationship to the LCD interface, and this data member is initialized in its constructor.
The Decorator class delegates to the LCD object.
Define a Decorator derived class for each optional embellishment.
Decorator derived classes implement their wrapper functionality - and - delegate to the Decorator base class.
The client configures the type and ordering of Core and Decorator objects.

## Rules of thumb
Adapter provides a different interface to its subject. Proxy provides the same interface. Decorator provides an enhanced interface.
Adapter changes an object's interface, Decorator enhances an object's responsibilities. Decorator is thus more transparent to the client. As a consequence, Decorator supports recursive composition, which isn't possible with pure Adapters.
Composite and Decorator have similar structure diagrams, reflecting the fact that both rely on recursive composition to organize an open-ended number of objects.
A Decorator can be viewed as a degenerate Composite with only one component. However, a Decorator adds additional responsibilities - it isn't intended for object aggregation.
Decorator is designed to let you add responsibilities to objects without subclassing. Composite's focus is not on embellishment but on representation. These intents are distinct but complementary. Consequently, Composite and Decorator are often used in concert.
Composite could use Chain of Responsibility to let components access global properties through their parent. It could also use Decorator to override these properties on parts of the composition.
Decorator and Proxy have different purposes but similar structures. Both describe how to provide a level of indirection to another object, and the implementations keep a reference to the object to which they forward requests.
Decorator lets you change the skin of an object. Strategy lets you change the guts.