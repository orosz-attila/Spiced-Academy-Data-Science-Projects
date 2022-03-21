## 05. Building a Dashboard with Metabase, PostgreSQL and AWS 

<div align="justify">In this project, I built an interactive online dashboard displaying sales data of a fictional company (“Northwind Traders”). The PostgreSQL database was .</div><br>

<p align="center">
  <img src="https://github.com/orosz-attila/Spiced-Academy-Data-Science-Projects/blob/c72cf4d72887b833f41c583211852dcdf4092abc/05_dashboard/image/northwind_traders_dashboard.png"/>
</p>



### 1. Creating a local PostgreSQL database 

#### 1.1. [Installing Postgresql](https://www.postgresql.org/download/) and [DBeaver](https://dbeaver.io/download/) (GUI for PostgreSQL)
<div align="justify"></div><br>  

<div align="justify">On Linux systems peer (password) authentification is disabled by default. You can enable by setting a password for the postgres user. With the command line, login to postgres as superuser:</div><br>  

    sudo -u postgres psql postgres

    ALTER USER postgres WITH PASSWORD 'password';

<div align="justify">Quit psql by typing \q or exit. You should now be able to login to your database with the password (no sudo required):</div><br>  

      psql -h localhost -p 5432 -U postgres -d postgres  

#### 1.2. Creating Northwind SQL database from .csv tables (create_tables.sql)

Creating new database in psql: 

      CREATE DATABASE northwind; 

Creating tables from create_tables.sql

#### 1.3. [ER diagram](https://github.com/orosz-attila/Spiced-Academy-Data-Science-Projects/blob/master/05_dashboard/image/er_diagram_northwind.png) in DBeaver: [adding primary keys and connecting tables with foreign keys](https://dbeaver.com/docs/wiki/New-Table-creation/)  


<p align="center">
  <img src="https://github.com/orosz-attila/Spiced-Academy-Data-Science-Projects/blob/master/05_dashboard/image/er_diagram_northwind.png"/>
</p>

### 2. Running SQL queries for business analytics 

[data_analysis_northwind.sql](https://github.com/orosz-attila/Spiced-Academy-Data-Science-Projects/blob/master/05_dashboard/data_analysis_northwind.sql)


### 3. Cloud database

Creating an AWS RDS instance, creating a database dump locally, deploying Northwind data to the RDS instance

### 4. Cloud server

Creating a virtual server with AWS EC2 and installing Metabase 

Metabase importing AWS RDS as host 

### 5. Building dashboard with Metabase  


(Due to costs, the server and database have been deleted and dashboard is not available online anymore.))
