## Intent
Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
Encapsulate the core (or common or engine) components in a Subject abstraction, and the variable (or optional or user interface) components in an Observer hierarchy.
The "View" part of Model-View-Controller.

## Problem
A large monolithic design does not scale well as new graphing or monitoring requirements are levied.****

---

## Check list
Differentiate between the core (or independent) functionality and the optional (or dependent) functionality.
Model the independent functionality with a "subject" abstraction.
Model the dependent functionality with an "observer" hierarchy.
The Subject is coupled only to the Observer base class.
The client configures the number and type of Observers.
Observers register themselves with the Subject.
The Subject broadcasts events to all registered Observers.
The Subject may "push" information at the Observers, or, the Observers may "pull" the information they need from the Subject.

## Rules of thumb
Chain of Responsibility, Command, Mediator, and Observer, address how you can decouple senders and receivers, but with different trade-offs. Chain of Responsibility passes a sender request along a chain of potential receivers. Command normally specifies a sender-receiver connection with a subclass. Mediator has senders and receivers reference each other indirectly. Observer defines a very decoupled interface that allows for multiple receivers to be configured at run-time.
Mediator and Observer are competing patterns. The difference between them is that Observer distributes communication by introducing "observer" and "subject" objects, whereas a Mediator object encapsulates the communication between other objects. We've found it easier to make reusable Observers and Subjects than to make reusable Mediators.
On the other hand, Mediator can leverage Observer for dynamically registering colleagues and communicating with them.