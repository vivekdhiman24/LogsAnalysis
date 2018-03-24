## Log-Analysis Project

# Project Overview
In this project, you'll work with data that could have come from a real-world web application, with fields representing information that a web server 
would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database,
allowing information to flow from the web server into the report.

## How to Run?

# PreRequisites:
Python3
Vagrant
VirtualBox

# Setup Project:
1. Install Vagrant and VirtualBox
2. Download or Clone fullstack-nanodegree-vm repository.
3. Download the data from here.
4. Unzip this file after downloading it. The file inside is called newsdata.sql.
5. Copy the newsdata.sql file and content of this current repository, by either downloading or cloning it from Here

# Launching the Virtual Machine:
1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
  $ vagrant up
2. Then Log into this using command:
  $ vagrant ssh
3. Change directory to /vagrant and look around with ls.

# Setting up the database and Creating Views:
1. Load the data in local database using the command:
  psql -d news -f newsdata.sql
The database includes three tables:

a.) The authors table includes information about the authors of articles.
b.) The articles table includes the articles themselves.
c.) The log table includes one entry for each time a user has accessed the site.

2. Use psql -d news to connect to database.

3. Create view 'view_articles' using following query:

  create view view_articles as select title, author, count(*) as views from articles,log where (log.path like concat('%', articles.slug, '%') AND 
  (log.status like '%200%')) group by articles.title,articles.author order by views desc;

		
4. Create view 'view_log' using following query:
  
  create view view_log as select day, round( (sum(requests)/(select count(log.status) from log where date(time) = day) *100), 2) as "Error %" from 
  (select date(time) as day, count(log.status) as requests from log where status like '%404%' group by day) as log_perc 
  group by day order by "Error %" desc;

 
# Running the queries: 
1. From the vagrant directory inside the virtual machine,run summary_tool.py using following command:
  vagrant@vagrant:/vagrant$ python3 summary_tool.py
