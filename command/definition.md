## Intent
Encapsulate a request as an object, thereby letting you parametrize clients with different requests, queue or log requests, and support undoable operations.
Promote "invocation of a method on an object" to full object status
An object-oriented callback

## Problem
Need to issue requests to objects without knowing anything about the operation being requested or the receiver of the request.

--- 


## Check list
Define a Command interface with a method signature like execute().
Create one or more derived classes that encapsulate some subset of the following: a "receiver" object, the method to invoke, the arguments to pass.
Instantiate a Command object for each deferred execution request.
Pass the Command object from the creator (aka sender) to the invoker (aka receiver).
The invoker decides when to execute().

## Rules of thumb
Chain of Responsibility, Command, Mediator, and Observer, address how you can decouple senders and receivers, but with different trade-offs. Command normally specifies a sender-receiver connection with a subclass.
Chain of Responsibility can use Command to represent requests as objects.
Command and Memento act as magic tokens to be passed around and invoked at a later time. In Command, the token represents a request; in Memento, it represents the internal state of an object at a particular time. Polymorphism is important to Command, but not to Memento because its interface is so narrow that a memento can only be passed as a value.
Command can use Memento to maintain the state required for an undo operation.
MacroCommands can be implemented with Composite.
A Command that must be copied before being placed on a history list acts as a Prototype.
Two important aspects of the Command pattern: interface separation (the invoker is isolated from the receiver), time separation (stores a ready-to-go processing request that's to be stated later).