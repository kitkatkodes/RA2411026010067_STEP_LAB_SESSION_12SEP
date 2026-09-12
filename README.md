# SOLID Principles in Python - Lab Session

This repository contains the refactored code and written answers for the SOLID Principles Enterprise Banking System lab assignment.

## Project Structure

The project is divided into four sections, each demonstrating a different SOLID principle. The written answers for the wrap-up questions are located in the README files within each specific section folder.

* **Section 1 (Single Responsibility Principle):** Separated the fat `BankAccount` class into dedicated classes for account management, database storage, email notifications, and statement generation.
* **Section 2 (Open/Closed Principle):** Implemented an `InterestPolicy` interface to allow adding new account types (like Salary Accounts) without modifying existing calculation logic.
* **Section 3 (Liskov Substitution Principle):** Fixed the `FixedDepositAccount` inheritance issue by introducing a capability-based `Withdrawable` interface to prevent runtime crashes.
* **Section 4 (Interface Segregation & Dependency Inversion):** Broke down the bloated `BankService` interface into smaller, focused interfaces and decoupled the `Bank` class from concrete database implementations. 

## How to Run
All source code is located in the `src/` directory, organized by section. Each section contains a `main.py` file to test the implementations.
