Purpose of this CA is to plan, design, develop and deploy a web application using Django framework and AWS services like Cloud9, S3 storage, My SQL instance and ELB. The project idea is to design personal profile web application displaying a home page with general profile owner information, shortcuts with pictures to completed jobs, links to blog posts (list of blog posts and detailed blog posts), link to a LinkedIn profile, a page displaying Trade simulation run results retrieved from MySQL RDS instance. All blog and job posts are performed from the Django Admin page. Authenticated users are added in Admin page. Web application design is performed using a Bootstrap template.
I.	INTRODUCTION
The main idea for this project composition is derived from professional experience and necessity to maintain personal profile giving opportunity to introduce personal and professional person’s overview.
For this purpose, best fit is to design and develop a web application demonstrating knowledge, proof of completed projects (jobs), blog posts, and displaying results from trades simulation run based on other project run results as a cross reference.
To bring this idea to life was decided to develop such application using such Django framework based on AWS services like Cloud9, S3 bucket storage, MySQL RDS instance.
All picture images are being stored in S3 Static and Media locations. User can add, modify and delete records from a database.

II.	PROJECT SPECIFICATION AND REQUIREMENTS

A.	Functional requirements

Main functional requirement of the project is to deliver to web application user possibility to:
-	display information about web site owner
-	display jobs
-	display blogs
-	display Trading Simulation results taken from different project located in MySQL database 
-	add/modify/remove blog and jobs entries
-	manage authorized user.
-	Provide minimum web application security level (use HTTPS) 

The project contains eight pages:
-	A home page displaying the main photo of the portfolio owner
-	Link to external LinkedIn profile
-	Link opening profile owner CV stored in web application Static folder located in AWS S3 bucket
-	Blog aggregated page
-	Blog detail page
-	Jobs detail page
-	Stock trades simulation run aggregated page displaying stock securities, positions, cash
-	Stock trades simulation run detail page providing trades execution information for each trade date within the simulation period
-	Admin page where user can add, modify, remove users, blog records and job records. An unauthorised user cannot open this page to perform web site modifications.

B.	Non-functional requirements

Web application design will use Bootstrap template. Security of application will be provided by AWS Beanstalk, Cloudwatch, Codecommit, RDS and S3 bucket services which will be protecting it from major OWASP top 10 threats. Web application will be using HTTPS hosting. 
Web application performance will be in line with selected EC2 instance power and could be upgraded if required.
Could be used AWS Load balancer and other services enhancing web application network performance.
