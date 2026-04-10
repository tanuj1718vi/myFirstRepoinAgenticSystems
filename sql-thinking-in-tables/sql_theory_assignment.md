1. Importance of Databases in AI Systems 

Databases are important in AI systems because they store large amounts of data in an organized way. AI needs data to learn and make decisions, and databases help manage this data efficiently.

Types of Data Stored:

User data (name, preferences)
Transaction data (orders, payments)
Sensor data (location, temperature)
Activity data (clicks, history)

Why Structured Storage is Needed:

Easy to find and use data
Faster processing for AI
Avoids errors and duplication
Keeps data organized

Example:

Shopping apps use databases to store user history, and AI uses this data to recommend products.

2.Relational Database Mental Model 

A relational database stores data in the form of tables. Each table is like a grid with rows and columns.

Table:
A table represents a single entity (object).

Rows:
Each row represents one record (one item).
Example: One row = one student

Columns:
Each column represents an attribute (property).
Example: name, age, marks

Why One Table = One Entity:
Keeps data clean and organized
Avoids confusion and duplication
Makes data easy to manage and query

3.Primary Key

A primary key is a column in a table that uniquely identifies each record.

Why Primary Key Must Be Unique:
No two rows can have the same value
Helps avoid duplicate records

Why Primary Key Must Be Non-Null:
It must always have a value
So every record can be identified

How It Helps:
Easily find specific data
Keeps data accurate and organized
Identifies each record clearly

4.Database Schema

A database schema is the structure or design of a database. It tells how data is organized.

What a Schema Defines:
Table names
Column names
Data types (INT, VARCHAR, etc.)
Relationships between tables

Why Schema is Important:
Keeps data organized
Maintains consistency in structure
Prevents errors
Helps developers understand the database

5.Relationships Between Tables

In relational databases, tables are connected using relationships so that related data can be linked together.

Foreign Key:
A foreign key is a column in one table that refers to the primary key of another table.

Example:
Users Table
user_id	name
1	Aman
2	Neha
Orders Table
order_id	user_id
101	1
102	2

Here, user_id in Orders is a foreign key that connects to user_id in Users.

How They Work:
One user can have many orders
Orders are linked to users using user_id