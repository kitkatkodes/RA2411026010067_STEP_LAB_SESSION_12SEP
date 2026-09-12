# Section 3: Liskov Substitution Principle

### Wrap-up Question 5: Why throwing an exception is the wrong fix
Making a class implement a method just to throw an exception is incorrect because it breaks the substitution rule. The rule requires that objects of a subclass must be usable wherever the superclass is expected without crashing the program. If we pass a fixed deposit account to a function expecting a standard withdrawable account, the program will crash, meaning the subclass has failed to fulfill the parent's contract.