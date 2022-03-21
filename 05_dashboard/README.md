## 05. Building an Online Dashboard with Metabase, PostgreSQL and AWS 

<div align="justify">In this project, I built an interactive online dashboard summarizing a sample database of a fictional company (“Northwind Traders”). The Northwind database contains all sales transactions between the company and its customers as well as purchases from suppliers.</div><br>

The project included the following tasks:

### 1. Creating a local SQL database 
Installing Postgresql and DBeaver (GUI for PostgreSQL)
Creating Northwind data .csv tables (create_tables.sql)
ER diagram in DBeaver: adding primary keys and connecting tables with foreign keys 

### 2. Running SQL queries for business analytics 

[data_analysis_northwind.sql](https://github.com/orosz-attila/Spiced-Academy-Data-Science-Projects/blob/master/05_dashboard/data_analysis_northwind.sql)


### 3. Cloud database

Creating an AWS RDS instance, creating a database dump locally, deploying Northwind data to the RDS instance

### 4. Cloud server

Creating a virtual server with AWS EC2 and installing Metabase 

Metabase importing AWS RDS as host 

### 5. Building dashboard with Metabase  


(Due to costs, the server and database have been deleted and dashboard is not available online anymore.)

![animation](05_dashboard/image/northwind_traders_dashboard.png)



<p align="center">
  <img src="https://github.com/orosz-attila/Spiced-Academy-Data-Science-Projects/blob/c72cf4d72887b833f41c583211852dcdf4092abc/05_dashboard/image/northwind_traders_dashboard.png"/>
</p>