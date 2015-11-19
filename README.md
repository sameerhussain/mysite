# mysite
This is a simple website about polls. This site contains voting your choice on question depending upon the choice you like against the question.

I have written it as simple as it can be in python using Django framework.

To run website:
	- You should have Postgresql running.( atleast 9.3.10 version).
	- You should have Django (1.8) installed,  and python3.4 in your system.
	- To start server,  just go to "mysite" directory,  and run type python3 manage.py runserver. This runs a website at localhost:8000
	- If you want it other way,  you can choose different port by adding port number as an extra argument.
	
Two types of access available:
	* Admin
	* polls
	
	Admin := Here,  you have access to adding questions and deleting them , adding votes and deleting votes,  changing dates and all administrative stuff.
	polls := Here you can access different types of questions, and mark your choice against the question.

