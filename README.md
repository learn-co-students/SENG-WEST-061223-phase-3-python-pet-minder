# SENG-LIVE-WEST-061223 Phase 3 - Python

## Phase Level Objectives

- Understand the principles of Python as a language including principles of object oriented programming
- Understand the characteristics of a relational database
- Perform CRUD actions on a database using SQLAlchemy & Alembic
- Design an API to handle CRUD actions
- Communicate with an API using different HTTP verbs
- Create and present a project with a React frontend and a database-backed API backend


| Lecture                                                                     | Videos     | Starter      | Solution      | Slides |
| --------------------------------------------------------------------------- | ---------- | ------------ | ------------- | ----- |
| 1. (07/24/23) Python Fundamentals                                           | [Video](https://www.youtube.com/watch?v=bQ1IKZ8VkrM) | [Starter](https://github.com/learn-co-students/SENG-WEST-061223-phase-3-python-pet-minder/tree/main/01_python_fundamentals) | [Solution](https://github.com/learn-co-students/SENG-WEST-061223-phase-3-python-pet-minder/tree/01_solution/01_python_fundamentals) | [Slides](https://raw.githack.com/learn-co-students/SENG-WEST-061223-phase-3-python-pet-minder/01_lantz/01_python_fundamentals/assets/export/index.html) |
| 2. (07/25/23) Python Data Structures                                        | [Video](https://www.youtube.com/watch?v=J4q95n55i4Y) | [Starter](https://github.com/learn-co-students/SENG-WEST-061223-phase-3-python-pet-minder/tree/main/02_python_data_structures) | [Solution](https://github.com/learn-co-students/SENG-WEST-061223-phase-3-python-pet-minder/tree/02_solution/02_python_data_structures) | [Slides](https://raw.githack.com/learn-co-students/SENG-WEST-061223-phase-3-python-pet-minder/main/02_python_data_structures/assets/export/index.html#/13) |
| 3. (07/26/23) Object Oriented Programming in Python                         | [Video](https://www.youtube.com/watch?v=IQBU7koMV14) | [Starter](https://github.com/learn-co-students/SENG-WEST-061223-phase-3-python-pet-minder/tree/main/03_oop) | [Solution](https://github.com/learn-co-students/SENG-WEST-061223-phase-3-python-pet-minder/tree/03_solution/03_oop) | [Slides](https://raw.githack.com/learn-co-students/SENG-WEST-061223-phase-3-python-pet-minder/03_lantz/03_oop/assets/export/index.html) |
| 4. (07/27/23) OOP 2: Class Methods, Class Variables, & Object Relationships | [Video](https://www.youtube.com/watch?v=023u7uisv4Q) | [Starter](https://github.com/learn-co-students/SENG-WEST-061223-phase-3-python-pet-minder/tree/main/03_oop) | [Solution](https://github.com/learn-co-students/SENG-WEST-061223-phase-3-python-pet-minder/tree/04_solution/04_OOP_2) | [Slides](https://raw.githack.com/learn-co-students/SENG-WEST-061223-phase-3-python-pet-minder/04_lantz/04_OOP_2/assets/export/index.html) |
| 5. (07/28/23) SQL Fundamentals & Table Relations                            | [Video](https://www.youtube.com/watch?v=s9Wfln3wd1Y) | [Starter](https://github.com/learn-co-students/SENG-WEST-061223-phase-3-python-pet-minder/tree/main/05_SQL) | [Solution](#) | [Slides](https://raw.githack.com/learn-co-students/SENG-WEST-061223-phase-3-python-pet-minder/main/05_SQL/dog_walker/assets/export/index.html) |
| 6. (07/31/23) Object-Relational Mapping                                     | [Video](https://www.youtube.com/watch?v=jOd_jv0W13w) | [Starter](https://github.com/learn-co-students/SENG-WEST-061223-phase-3-python-pet-minder/tree/main/06_orm) | [Solution](https://github.com/learn-co-students/SENG-WEST-061223-phase-3-python-pet-minder/tree/06_example_solution_orm/06_orm) | [Slides](#) |
| 7. (08/01/23) SQLAlchemy & Alembic                                          | [Video](https://www.youtube.com/watch?v=Dh_lmkQxI94) | [Starter](https://github.com/learn-co-students/SENG-WEST-061223-phase-3-python-pet-minder/tree/main/07-SQLAlchemy-and-Alembic) | [Solution](https://github.com/learn-co-students/SENG-WEST-061223-phase-3-python-pet-minder/tree/07_example_solution_SQLAlchemy/07-SQLAlchemy-and-Alembic) | [Slides](https://raw.githack.com/learn-co-students/SENG-WEST-061223-phase-3-python-pet-minder/main/07-SQLAlchemy-and-Alembic/assets/export/index.html) |
| 8. (08/04/23) SQLAlchemy Associations                                       | [Video](https://www.youtube.com/watch?v=5TenIXic7Pw) | [Starter](https://github.com/learn-co-students/SENG-WEST-061223-phase-3-python-pet-minder/tree/08_example_starter_SQLAlchemy_Associations/08-SQLAlchemy-Associations) | [Solution](https://github.com/learn-co-students/SENG-WEST-061223-phase-3-python-pet-minder/tree/08_solution/08-SQLAlchemy-Associations) | [Slides](#) |

## 1: Python Fundamentals
### Lecture Goals:
- Review an introduction to Python and phase trajectory 
- Demonstrate Python package management with `pip`
- Demonstrate debugging in Python with `shell`, `print`, and `ipdb`
- Review Python data types (`str`, `int`, `float`, `complex`, `bol`, `bytes`, `bytearry`, `memoryview`, `None`)
- Demonstrate Python conditionals and control flow
- Demonstrate Python functions
- Review Python variable scope and the global keyword
- Review Python error messages and exceptions 
- Demonstrate handling errors with `try:` and `except:` 
- Stretch Goals
    - Review `pytest`
    - Review the Python Style Guide

### Lecture Topics:
- Python and a Short History
- Package Management with `pip`
- Debugging
    - `print`
    - `ipdb`
    - Python Shell
    - Errors
    - Exceptions
        - `try:` `except:` 
- Python Conditionals and Control Flow
    - `if...else`
    - Comparison Operators
        - `>:` greater than
        - `>=:` greater than or equal to
        - `<:` less than
        - `<=:` less than or equal to
        - `==:` equal to
        - `!=:` not equal to
    - Logical operators
        - `and:` 
        - `or:` 
        - `not:` 
- Conditional Expressions
    - Ternary
- Python Functions
    - Function Definition 
    - Params
    - Default Params
    - Arguments
    - Invoking 
- Error Handling 
    - Reading Errors 
        - Syntax Errors, Logic Errors, and Exceptions
        - `AssertionError`
        - `IndexError` and `KeyError`
        - `NameError`
        - `TypeError`
        - `try:` `except:`
- Stretch Topics
    - `pytest`
        - How to Read Tests 
            - Note: Create tests is not covered in the labs
    - Python Style Guide

## 2: Python Data Structures
### Lecture Goals:
- Demonstrate Sequence types (`list`, `tuple`, `range`)
- Review the different uses for each Sequence type
- Demonstrate standard methods for accessing, updating and deleting values in Lists
- Review Tuples
- Review Ranges 
- Demonstrate Mapping types with Dictionaries
- Demonstrate standard methods for accessing, updating and deleting values in Dictionaries
- Demonstrate Set types with `set()` and `frozenset()`
- Demonstrate `for` and `while` loops
- Demonstrate list compressions 
- Stretch Goals
    - Demonstrate Generator expressions 
    - Demonstrate how to create a `switch` using a Dictionary

### Lecture Topics:
- Sequence Types
    - List
    - Tuple
    - Range
    - Common Sequence Operators 
    - List Methods 
    - Tuples and Immutable vs Mutable 
- Mapping Types
    - Dict 
        - `switch`
- Set Types
    - Set
- Loops
    - `for`
    - `while`
    - List Compression
- Sequence Operators
- Sequence Functions and Methods
- Stretch Topics
    - Generator Expressions 

## 3: Object Oriented Programming in Python
### Lecture Goals:
- Define Object Oriented Programming
- Explain the benefits of Object Oriented Programming
- Explain the principles of Object-Oriented Design
- Demonstrate classes 
- Demonstrate instances 
- Demonstrate `__init__`
- Demonstrate instance method
- Demonstrate the `self` keyword 
- Stretch Goals
    - Demonstrate object properties
    - Demonstrate mass assignment during Class instantiation

### Lecture Topics:
- Object Oriented Programming 
- Benefits of Object Oriented Programming
- Principles of Object-Oriented Design
- Classes 
- Instances
- Initializing with Attributes Using `__init__`
- Instance Methods
- Self
- Stretch Topics
    - Object Properties

## 4: OOP 2: Class Methods, Class Variables, & Object Relationships
### Lecture Goals:
- Demonstrate Decorators 
    - `@decorator`  
- Demonstrate class variables
    - Defining class variables
    - Updating class variables 
- Demonstrate class methods
    - Defining class methods 
    - `@classmethod`
    - `cls` keyword 
- Object Inheritance
- Stretch Goals
    - Super

- Build one-to-many relationships between objects
    - Define one-to-many relationships
    - Discuss their importance and use
    - Emphasize single-source-of-truth
    - Demonstrate building one-way and two-way relationships
- Build many-to-many relationships between objects
    - Define many-to-many relationships
    - Discuss their importance and use
    - Demonstrate building the relationship with and without intermediary class
- Aggregate Methods
    - Write aggregate methods to collect data about objects using their related objects

### Lecture Topics:
- Decorators
- Class Variables
- Class Methods
- Object Inheritance
- Stretch Topic
    - Super

## 5: SQL Fundamentals & Table Relations
### Lecture Goals:
- Explain why we use databases
- Explain what SQL is and why we use it
- Explain the differences between a database, server, and API
- Explain the differences between rows and columns in a table
- Explain the differences between a Foreign Key and a Primary Key
- Explain what a join table is
- Explain what it means to seed a database
- Observe using SQL to communicate with a database
- Explain what an ORM is

### Lecture Topics:
- The Use Value of Databases in Applications
- Domain Modeling
- Join Table
- Mapping Columns and Rows to Classes and Instances
- Primary Keys
- Foreign Keys
- SQL
- ORM

## 6: Object-Relational Mapping
### Lecture Goals:
- Demonstrate configuring an application to connect with sqlite3
- Demonstrate a create table method 
- Review preventative measures for SQL injection
- Demonstrate save and create methods  
    - Save => Persist created instance to DB
    - Create => Instantiate / persist created instance to DB, return new instance 
- Demonstrate query methods to find and retrieve resources 
- Stretch Goal
    - Make a `create_and_find_by` member
    - Make `update` and `delete` members

### Lecture Topics:
- The benefits of ORM
- Connecting ORMs to DBs
- How to Use Data From a Database to Make Python Objects
- Mapping a Database Table to a Python Object
- Turning Database Rows into Python Objects


## 7: SQLAlchemy & Alembic
### Lecture Goals:
- Explain what SQLAlchemy is and how it benefits us as an ORM
    - Demonstrate creating a database with SQLAlchemy 
    - Demonstrate creating a schema
    - Demonstrate creating columns with SQLAlchemy
    - Demonstrate creating column constraints with SQLAlchemy 
    - Demonstrate creating indexes with SQLAlchemy 
    - Demonstrate creating default values 
- Explain Alembic and what it does for us
    - Demonstrate configuring an application to use Alembic 
    - Demonstrate creating migrations using Alembic
    - Demonstrate creating manual migrations using Alembic
    - Demonstrate CRUD in SQLAlcehmy
        - Adding data with .commit
            - `.all`, `.order_by`, `desc`, `limit`, function filter, and loop compression to grab specific columns 
        - Querying data with `.query`
        - Updating data with `.update` and `.commit`
        - Deleting data with `.delete`

### Lecture Topics:
- Creating a Database 
- Creating a Schema 
    - Columns 
    - Constraints
    - Index
    - Default Values
- Alembic
    - Migrations
        - Configuring the Migration Environment
        - Creating Migrations 
        - Manual Migrations 
- CRUD 
    - Sessions 
    - Transactions
    - `__repr__`
    - Creating Records
        - Seeding Data
    - Reading Records
        - Selecting Specific Columns
        - Ordering
        - Limits
        - Filtering 
        - Func
    - Updating Data
    - Deleting Data

## 8: SQLAlchemy Associations
### Lecture Goals:
- Review relationships, Primary keys, and Foreign keys
- Demonstrate creating a table with a Foreign key and referencing another table using `relationship()` and `backref()`
- Demonstrate using Alembic to generate tables with relationships 
- Demonstrate querying methods to view table relationships
- Demonstrate a “one to many” association
- Demonstrate a “many to many” association with a join model 
- Stretch Goal
    - Demonstrate using a CLI to access a backend application

### Lecture Topics:
- Design Database Tables
- One-to-Many 
- Foreign Key Columns 
- `relationship()` and `backref()`
- One-to-One
- Alembic Migrations to Generate Table Relationships
- Relation Query Methods 
- Many-to-Many 
- Stretch Topic
    - Making a CLI

