# datafun-05-sql-project
Created for P5 of Data Fundamentals Course

## Description
This project demonstrates the creation of a SQL database using Python and SQLite3 and some NBA statistics datasets. Jupyter Notebook is used to demonstrate exploratory data analysis of the  dataset using SQLite3 and Pandas to manipulate the relational data from the database.

## How to Install & Run the Project
1. Create repository on GitHub with default README.md, Python .gitignore, and MIT license
2. Copy the repository to a local project folder:  
`git clone https://github.com/matthewpblock/datafun-05-sql-project`  
3. Migrate terminal to the project server
4. Setup a virtual environment:  
`py -m venv .venv`  
5. Activate the virtual environment:  
`.venv\Scripts\activate`  
6. Create requirements.txt
7. Commit changes
8. Update pip & install requirements
```py -m pip install --upgrade pip setuptools wheel  py -m pip install -r requirements.txt```  
9. Set correct interpreter & kernel  

## Folder Structure
- sql_create: Contains SQL scripts to drop and create tables (including foreign keys), and insert records to a table
- sql_features: Contains SQL scripts for data cleaning and feature engineering
- sql_queries: Contains various SQL scripts for aggregation statistics, filtering, sorting, grouping, and joining data
- data: contains source data CSVs, the SQL database, and any outputs
- logs: contains logs of scripted actions ran and errors
  
## References
Lessson specifications: https://github.com/denisecase/datafun-05-spec  
Data from: "Learn to Code with Basketball" by Nathan Braun https://github.com/nathanbraun/code-basketball-files  
