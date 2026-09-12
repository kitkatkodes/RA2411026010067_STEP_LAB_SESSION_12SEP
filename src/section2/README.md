# Section 2: Open/Closed Principle

### Question 1: Adding a new account type to an if/else chain
We would have to open the InterestCalculator file and locate the calculate method. We would then need to add another elif condition specifically checking if the accountType equals the new type. Finally, we would have to add the mathematical formula for the new account type directly inside that new block.

### Question 5: Modifying files for the Salary Account requirement
For the Salary Account requirement, I had to create two brand new files for the account and the policy, and I opened the main file to wire them up. Zero existing policy classes had to be changed to add this new feature.