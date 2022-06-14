# Introduction 
This project set out by QA will involve the following skills...

* Project Management 
* Python Fundamentals 
* Python Testing 
* Git 
* Basic Linux
* Pythin Web Development
* Continuois Integration
* Cloud Fundamentals
* Databases

This is all with the over all objective of creating a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training. This will be able to store infomation on a database using a VM provided by google and this database will have 2 entries which will be linked through a one to many relationship

### CRUD 

CRUD is an abrivation for... 

* Create - To complete this I will have to be able to create new fields in the database and save them, through user input from a front end application. This will be completed in python as the application will be created there, as well as, using the flask package to help with the front end application.
* Read - This will be the ability to read the data from the database and see all the data from the front end application. 
* Update - This will be the ability to update any data that is within the database.
* Delete - Lastly this will be the ability to delete any of the data within the database.

All of which will be displayed within the program connected to this project.

# Scope 

This project comes with a set of requirements that will need to be met to ensure completion. 
These requirements are...

* A Trello Board - That will have full expansion
on user stories, use cases and tasks needed to complete the project.
As well as records of any issues or risks faced.

* A relational database - Used to store all data persistently, and
must have minimum of two tables within it. We are also required to 
model a relationship.

* Clear documentation - from a design phase describing the architecture
you will use for you project as well as a detailed Risk Assessment.

* A functional CRUD application - Created in Python, following best
practices and design principles, that meets the requirements set on
your Trello Board.

* Fully designed test suits - For the application created. As well as 
automated tests for validation of the application. You must
provide high test coverage in your backend and provide consistent
reports and evidence to support a TDD approach.

* A functioning frount-end website and integrated APIs, using Flask

* Code fully integrated into a Version Control System using the
Feature-Branch model which will subsequently be built through a CI
server and deployed to a cloud-based virtual machine.

Once all these requirements have been met the project will be complete.

# Planning 

### Designing the application 
The first part of the planning was to come up with an idea for the project I went with a games database which will have a list of games that you see along with there developers and price. The tables within the application will be the games table and the developers table which will have a one to many relationship. This has been shown on the entity relationship diagram below 
![alt text](https://github.com/ThomasStoyles/QAProject/blob/main/Photos%2C%20Assessments%20and%20Diagrams/ERD.jpg)

### Project Tracking
For the project we had to create a Kanban board, for this I used trello. I used this board to track my progress throughout the application and was able to track what still needs to happen and what has been completed. Within each heading on my trello board was a To-Do list with items that I had to complete before I would have completed the project. Below are images of the trello board to help you see this process.
![alt text](https://github.com/ThomasStoyles/QAProject/blob/main/Photos%2C%20Assessments%20and%20Diagrams/Trello.jpg)

As you can see in the trello board this is about half way through createing my project. The trello board has user stories on it which I created depending on how hard I felt certain tasks will be. I also have had some issues with my project which I will go into more detail about further in this report.


### Risk assessment

Before I could start creating the application I had to create a risk assessment to make sure that any risks that i could come across are identified. This allows me to prepare for the risks, that could happen, and implement ways to avoid/minimalise these risks. Please see the assessment below.

![alt text](https://github.com/ThomasStoyles/QAProject/blob/main/Photos%2C%20Assessments%20and%20Diagrams/Risk%20Assessment.jpg)


# Designs 

When it comes to the CRUD application, I knew that I had to design the appliaction before creating it so I had some plan to follow. Below is a prototype of the application I created before I started the project. As you can see i had included all functionaltiy that a CRUD application needed, with the addition of the navigation bar.
The first image is the addition screen which would allow the user to add into the database a new game field. 

![alt text](https://github.com/ThomasStoyles/QAProject/blob/main/Photos%2C%20Assessments%20and%20Diagrams/Addition%20Page.jpg)

The next image is the read me page which displays all the games within the database alongside there developer this will be where the database relationship happens, with a one to many relationship between the developer and the game. 

![alt text](https://github.com/ThomasStoyles/QAProject/blob/main/Photos%2C%20Assessments%20and%20Diagrams/Read%20page.jpg)


# Testing
After the project had been completed I added tests into the program to make sure that everything in the program was tested and working as intended. This was done through pytest. This was done by creating a new file called test_app and adding a testing database to it so we dont test on the live database. Then i created classes that will be used in all tests, these are to be the base of all tests. Once completed i went through and tested all CRUD functions within the project to make sure that they are all working as intended. Please see a image below for the results of the pytesting

![alt text](https://github.com/ThomasStoyles/QAProject/blob/main/Photos%2C%20Assessments%20and%20Diagrams/Pytest.jpg)

After the pytesting was done I needed to make sure that the test was done automaticlly. To do this I used Jenkins. On jenkins I created a pipeline and used my github link so that jenkins knew which reposatory to test. Once completed I needed to set up a webhook so that when that Github reposatory is updated jenkins runs test in the background. After I had done this I generated the report below on jenkins. 

![alt text](https://github.com/ThomasStoyles/QAProject/blob/main/Photos%2C%20Assessments%20and%20Diagrams/Tests.jpg)

The report shows only 87% accuracy. This is because some of the code can be tested in routes. Mainly being the loop that I created to count how many developers there are in the program and, what ID they should be. This is where the lose of coverage comes from.

To run these tests you can by using the pytest command python3 -m pytest whilst in the application this will run pytest and will show you what the test coverage is across the program. If you wish to gerneate the report you will have to go onto jenkins and create a freestyle project. Then add the github link into where it asks you too and type in the bash commands. Once completed you can test the project and see the report that is generated.


# Challenges

While creating the project I ran into many challenges. These challenges were hard to overcome however was a good learning experiance for me to test myself on my skills and ability to learn.

One of the first challenges I faced was the updating functionality of the CRUD application.

# Versions 
1.0.0 - Updated 12/05/2022
1.0.1 - Updated

# Licensing 


# Contributors
Thomas Stoyles

# Acknowledgements 
I would like to thank Leon, Adam and Earl for all there support when delivering this project.
