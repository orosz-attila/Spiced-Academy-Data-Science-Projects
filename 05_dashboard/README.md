## 05. Building a Dashboard with Metabase, PostgreSQL and AWS 

<div align="justify">In this project, I built an interactive online dashboard displaying sales data of a fictional company (Northwind Traders). The database was created from .csv files with PostgreSQL and hosted in a cloud database (AWS RDS). The dashboard was created with Metabase that was installed on a virtual server (AWS RC2) and connected to the cloud database.</div><br>

<div align="justify">(Due to costs, the AWS database and virtual server have been deleted and dashboard is not available online anymore.)</div><br>

<p align="center">
  <img src="https://github.com/orosz-attila/Spiced-Academy-Data-Science-Projects/blob/c72cf4d72887b833f41c583211852dcdf4092abc/05_dashboard/image/northwind_traders_dashboard.png"/>
</p>

<br>

## Description

### 1. Creating a local PostgreSQL database 

#### 1.1. [Installing Postgresql](https://www.postgresql.org/download/) and [DBeaver](https://dbeaver.io/download/) (GUI for PostgreSQL)

- <div align="justify">On Linux systems peer (password) authentification is disabled by default. You can enable it by setting a password for the postgres user. With the command line, login to postgres as superuser:</div><br>  

      sudo -u postgres psql postgres

      ALTER USER postgres WITH PASSWORD 'password';

- <div align="justify">Quit psql by typing \q or exit. You should now be able to login to your database with the password (no sudo required):</div><br>  

      psql -h localhost -p 5432 -U postgres -d postgres  
<br>

#### 1.2. Creating Northwind SQL database from .csv tables (create_tables.sql)

- Creating new database in psql: 

      CREATE DATABASE northwind; 

- Creating tables from file [create_tables.sql](https://github.com/orosz-attila/Spiced-Academy-Data-Science-Projects/blob/master/05_dashboard/create_tables.sql): 

      psql -h 5432 -U postgres -d northwind -f create_tables.sql

      psql -h 5432 -U postgres -d northwind -f countries.sql 
<br>

#### 1.3. Creating [entity-relationship diagram](https://github.com/orosz-attila/Spiced-Academy-Data-Science-Projects/blob/master/05_dashboard/image/er_diagram_northwind.png) with DBeaver: [adding primary keys and connecting tables with foreign keys](https://dbeaver.com/docs/wiki/New-Table-creation/)  


<p align="center">
  <img src="https://github.com/orosz-attila/Spiced-Academy-Data-Science-Projects/blob/master/05_dashboard/image/er_diagram_northwind.png"/>
</p>
<br>


### 2. Business Analytics with SQL queries 

- See [data_analysis_northwind.sql](https://github.com/orosz-attila/Spiced-Academy-Data-Science-Projects/blob/master/05_dashboard/data_analysis_northwind.sql)

<br>


### 3. Cloud database

#### 3.1. Setting up an AWS RDS (Relational Database Service) instance

- See step-by-step description in [aws_rds_installation.sh]() 

#### 3.2. Creating Northwind database on the RDS instance

- Connecting to the PostgreSQL cloud database in bash (password is the master password entered at the setting up of the RDS instance):

      psql -h <aws rds endpoint> -U postgres; 

- Creating a database with PostgreSQL: 

      CREATE DATABASE northwind

- Exit the cloud PostgerSQL. Copy tables from local Postgresql database to the cloud database: 

      psql -h <aws rds endpoint> -U postgres -d northwind -f create_tables.sql

      psql -h <aws rds endpoint> -U postgres -d northwind -f countries.sql 

- Enter again to cloud POstgresql. Connect to Northwind and checking whether all tables have been copied: 

      psql -h <aws rds endpoint> -U postgres
    
      \c northwind

      \dt

<br>

### 4. Cloud server

  #### 4.1.Creating a virtual server with AWS EC2 and installing Metabase. 

See step-by-step description in [aws_ec2_installation.sh](https://github.com/orosz-attila/Spiced-Academy-Data-Science-Projects/blob/master/05_dashboard/aws_ec2_installation.sh) 

  #### 4.2. Connecting AWS RDS as host in Metabase setting

For connecting the Northwind cloud database to the Metabase, you should enter the url of the RDS instance as host in database settings of Metabase.  

<br>

### 5. Building interactive dashboard with Metabase  

Creating visualizations for the dashboard of Northind Traders sales data: 

- Total revenue by countries (map)
- Number of Customers (card)
- Number of orders (card)
- Best selling products (barchart, by descending order)
- Total revenue by countries (pie chart, descending order, displaying amount and percentage)
- Number of orders of all products stacked by countries (barchart)
- Orders per week over time stacked by product categories (barchart)

Adding filters to the dashboard: 

- countries filter: filters data for visualizations by the selected country



- date filter: filters date for the visualization by selected date: 



Click behaviour setting: 
- if a country is selected in one visualization, the others display only the data of the selected country:  