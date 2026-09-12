# Section 1: Single Responsibility Principle

### Question 1: Reasons to Change
Based on the Single Responsibility Principle, the original class has at least four distinct reasons to change:
1. Changes to the database storage or persistence layer.
2. Changes to the email provider or notification logic.
3. Changes to the way transaction statements are formatted or printed.
4. Changes to the core banking rules like minimum balance requirements.

### Question 2: Job Description
The BankAccount class should be solely responsible for tracking a customer balance by processing valid deposits and withdrawals.

### Question 5: Wrap-up
The refactoring process resulted in four distinct classes. Testing is now much easier because you can write unit tests for the core account balance logic without needing to set up a database connection or a mock email server. If the statement text formatting breaks, you know exactly which single file to check without any risk of breaking the withdrawal logic.