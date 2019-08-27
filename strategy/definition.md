## Intent
Define a family of algorithms, encapsulate each one, and make them interchangeable.
Strategy lets the algorithm vary independently from the clients that use it.
 
Capture the abstraction in an interface, bury implementation details in derived classes.

## Problem
One of the dominant strategies of object-oriented design is the "open-closed principle".

Figure demonstrates how this is routinely achieved - encapsulate interface details in a base class,
and bury implementation details in derived classes. Clients can then couple themselves to an interface,
and not have to experience the upheaval associated with change: no impact when the number of derived classes changes,
and no impact when the implementation of a derived class changes.

---

## Check list
Identify an algorithm (i.e. a behavior) that the client would prefer to access through a "flex point".
Specify the signature for that algorithm in an interface.
Bury the alternative implementation details in derived classes.
Clients of the algorithm couple themselves to the interface.

## Rules of thumb
Strategy is like Template Method except in its granularity.
State is like Strategy except in its intent.
Strategy lets you change the guts of an object. Decorator lets you change the skin.
State, Strategy, Bridge (and to some degree Adapter) have similar solution structures. They all share elements of the 'handle/body' idiom. They differ in intent - that is, they solve different problems.
Strategy has 2 different implementations, the first is similar to State. The difference is in binding times (Strategy is a bind-once pattern, whereas State is more dynamic).
Strategy objects often make good Flyweights.