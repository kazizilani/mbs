MBS — Mock Banking System
A simple CLI-based mock mobile banking system built with Python.

MBS is a small educational project designed to demonstrate how Object-Oriented Programming (OOP) concepts can be applied to a real-world-style application. The system models common mobile banking operations through an interactive command-line interface.

Note: This project is a mock banking application for learning and demonstration purposes. It is not intended for handling real financial transactions or sensitive banking information.

Features
The application provides a command-line interface for interacting with the mock banking system.

The project is structured around several core responsibilities:

User interaction through a command-line menu.

Banking/business logic separated from the user interface.

Database-related functionality organized under the db/ directory.

Reusable utilities contained in the utils/ directory.

Interfaces and menu controllers organized under the interfaces/ directory.

Object-oriented design to keep different parts of the application modular and easier to maintain.

Project Structure
mbs/
├── app.py
├── db/
│   └── ...
├── interfaces/
│   └── ...
├── utils/
│   └── ...
└── README.md

app.py
app.py is the entry point of the application.

Its main responsibility is to initialize the application's main menu and hand control over to the menu controller:

from interfaces.main_menu import MainMenu

MainMenu().MenuController()

Keeping the entry point this small allows the application logic to remain separated from the code responsible for starting the program.

interfaces/
The interfaces/ package contains the components responsible for interacting with the user.

The main menu acts as the entry point for the CLI experience and controls the flow between the different operations available to the user.

This separation keeps presentation and user interaction concerns away from the underlying banking logic.

db/
The db/ package contains the project's database-related components.

Keeping persistence-related code in its own package makes it possible to change or extend how data is stored without having to tightly couple database operations to the CLI interface.

utils/
The utils/ package contains reusable helper functionality used by different parts of the application.

Putting common functionality here helps avoid duplicating code throughout the project.

Architecture
MBS follows a simple separation-of-concerns approach:

             ┌─────────────┐
             │   app.py    │
             │ Entry Point │
             └──────┬──────┘
                    │
                    ▼
          ┌───────────────────┐
          │   Main Menu /     │
          │     Interfaces    │
          └─────────┬─────────┘
                    │
             ┌──────┴───────┐
             ▼              ▼
       ┌───────────┐  ┌────────────┐
       │  Banking  │  │ Utilities  │
       │   Logic   │  │   / Helpers│
       └─────┬─────┘  └────────────┘
             │
             ▼
       ┌───────────┐
       │    db/    │
       │ Persistence│
       └───────────┘

The goal is to keep each part of the application responsible for a specific concern rather than placing the entire application inside a single Python file.

Object-Oriented Programming
One of the main purposes of this project is to demonstrate practical OOP.

The application can be understood as a collection of objects representing different parts of a banking system and its user interface.

The project demonstrates concepts such as:

Classes and objects — representing application entities and components.

Encapsulation — keeping related data and behavior together.

Abstraction — hiding implementation details behind interfaces and methods.

Separation of concerns — keeping UI, business logic, persistence, and utilities separate.

Composition — allowing different objects to work together to form the application.

This makes the project useful as a small example for developers learning how to move from procedural scripts toward a more structured OOP design.

Getting Started
Prerequisites
Make sure you have Python installed on your system.

You can check your Python installation with:

python --version

or:

python3 --version

Clone the Repository
git clone https://github.com/kazizilani/mbs.git
cd mbs

Run the Application
Start the application with:

python app.py

If your system uses python3:

python3 app.py

The application will launch the main menu in your terminal.

Example Usage
After starting the application, interact with the available options through the command-line menu.

A typical flow looks like:

$ python app.py

=========================
     Mock Banking System
=========================

1. ...
2. ...
3. ...
4. Exit

Select an option:

The exact menu options depend on the current implementation.

Design Goals
MBS is intentionally kept relatively small.

The primary goals are:

Demonstrate practical Python OOP.

Show how a CLI application can be divided into multiple modules.

Keep user-interface code separate from application logic.

Provide a simple environment for experimenting with banking-related domain models.

Make the codebase approachable for developers who are learning software design.

Why This Project?
A banking system is a useful example domain because it naturally contains multiple entities, operations, and rules.

For example, a banking application can involve:

User
 ├── Account
 │    ├── Balance
 │    ├── Deposit
 │    └── Withdrawal
 │
 └── Transactions
      ├── Transfer
      └── Transaction History

Modeling these concepts as objects provides a practical way to understand how OOP can be applied beyond simple classroom examples.

Limitations
This is an educational/mock application and should not be treated as production banking software.

In particular:

It should not be used to process real financial transactions.

It should not store real banking credentials.

It does not provide the security guarantees expected from a production financial application.

Authentication, authorization, encryption, auditing, concurrency, and other production concerns would require significantly more work.

Future Improvements
Possible improvements include:

Add proper user authentication.

Add account creation and management.

Add deposit and withdrawal operations.

Add money transfers between accounts.

Add transaction history.

Improve input validation and error handling.

Introduce automated tests.

Add configuration management.

Improve persistence and database abstraction.

Add logging.

Add type hints throughout the codebase.

Add documentation for individual classes and modules.

Introduce a proper service layer between the CLI and database.

Add a REST API or web interface as an alternative frontend.

Contributing
Contributions and suggestions are welcome.

A typical contribution workflow is:

# Fork the repository

# Clone your fork
git clone https://github.com/<your-username>/mbs.git

# Create a feature branch
git checkout -b feature/my-feature

# Make your changes

# Commit your changes
git add .
git commit -m "Add my feature"

# Push the branch
git push origin feature/my-feature

Then open a pull request against the main repository.

License
Add the project's license information here if/when a license is chosen.

Author
Kaz Izilani

Repository: https://github.com/kazizilani/mbs

Project Status
MBS is a small educational project focused on demonstrating Python and object-oriented programming concepts through a mock banking application.
