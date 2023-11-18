# 0x0F. Python - Object-relational mapping

In this project, I linked two amazing worlds: Database and Python!
In the first part, I used the module MySQLdb to connect to a MySQL database and execute your SQL queries. In the second part, I used the module SQLAlchemy an Object Relational Mapper (ORM).
The purpose of an ORM is to abstract the storage to the usage. With an ORM, the biggest concern will be "What can I do with my objects" and not "How this object is stored? where? when?". No SQL queries only Python code. Last thing, the codebase won't be "storage type" dependent, giving the ability to change storage easily without re-writing the entire project.

This project helped to understand:
- How to connect to a MySQL database from a Python script
- How to SELECT rows in a MySQL table from a Python script
- How to INSERT rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table
- How to create a Python Virtual Environment

The project consist of the following tasks:
TASKS | DESCRIPTION
--- | ---
`0-select_states.py` | A script that lists all states from the database
`1-filter_states.py` | Script that lists all states with a name starting with N from the database
`2-my_filter_states.py` | A script that takes in an argument and display all values in the states table where name matches the argument
`3-my_safe_filter_states.py` | A script that takes in argument and displays all values in states table of database when it matches an argument with MySQL injections
`4-cities_by_state.py` | A script that lists all cities from the database
`5-filter_cities.py` | A script that takes in the name of a state as an argument and lists all cities of that state using database
`model_state.py` | A python file that contains the class definition of a State and an instance Base class
`7-model_state_fetch_all.py` | A script that lists all State objects from the database
`8-model_state_fetch_first.py` | A script that prints the first State object from the database
`9-model_state_filter_a.py` | Lists all State objects that contain the letter a from the database
