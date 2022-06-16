
### Table of contents

[Introduction](#Introduction)

[CRUD](#CRUD)

[Scope](#Scope)

[Planning](#Planning)

[Designs](#Designs)

[Testing](#Testing)

[CI-DI Pipeline](#CI-DI-Pipeline)

[Known app issues](#Known-app-issues)

[Challenges](#Challenges)

[Future updates](#Future_updates)

[Licensing](#Licensing )

[Contributors](#Contributors)

[Acknowledgements](#Acknowledgements)



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

# CRUD 

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

The report shows only 87% accuracy. Therefore I added Cobertura to my jenkins tests to try and find the issue with the code. This allowed me to see all lines that wasn not being tested. After fixing some tests I was able to get the tests up to a 91% coverage as seen below.

![alt text](https://github.com/ThomasStoyles/QAProject/blob/main/Photos%2C%20Assessments%20and%20Diagrams/Tests2.jpg)

To run these tests you can by using the pytest command python3 -m pytest whilst in the application this will run pytest and will show you what the test coverage is across the program. If you wish to gerneate the report you will have to go onto jenkins and create a freestyle project. Then add the github link into where it asks you too and type in the bash commands. Once completed you can test the project and see the report that is generated.

# CI-DI Pipeline
Here is a diagram of the CI/DI pipeline that was implemented for this project.
![alt text](https://github.com/ThomasStoyles/QAProject/blob/main/Photos%2C%20Assessments%20and%20Diagrams/CIDI.jpg)

Please see a copy of a successful Jenkins build log. Please click [here](https://github.com/ThomasStoyles/QAProject/blob/main/Photos%2C%20Assessments%20and%20Diagrams/Jenkins%20build%20log)
# Known app issues
No known issues

# Challenges

While creating the project I ran into many challenges. These challenges were hard to overcome however was a good learning experiance for me to test myself on my skills and ability to learn.

One of the first challenges I faced was the updating functionality of the CRUD application. Part of the sepcification of the project is to have a update function which will allow users to update the database so that any incorrect infomation can be chnaged without having to reinput it. The issue I had when creating this is that the when you saved the changes it did not update the database. This caused multiple versions of the same game to be saved just with diffrent values and names. To fix this I simply changed the route of the update route so that it used the ID of the game and then updated the ID rather than creating a new field to replace the old one. 

Another challenge was jenkins. When I started to use jenkins I had never used it before so this was a new concept to me therefore I had many challeneges that i had to overcome. One of these challenges was getting the webhook set up in jenkins. A webhook allows jenkins to run tests that you have definined when you push a new update to github. The issue I faced was when pushing to github the tests in jenkins was not running correctly. To fix this I recreated my pipeline in jenkins with the correct bash commands and chnaged the webhook link on github and I was able to get the webhook working. 

The next challenge is the database was not saving the data when the data was inputted. When you entered data into the forms it did not save that data to the database therefore if you tried to add a new game or developer the data was not saved. Luckily this was quite an easy fix once i figured out what was missing from the db.session function. I had simply not added a get data function and missed a commit function this meant that the data was not being pulled by the app.routes and then the data was not commited to the database so it was never saved just added. To fix this I firstly added add.price.data function for all variables. Then i added the db.session.commit function so that it was saved to the database.

# Future updates
For the future of this project there are other implementations that can be completed...
 - Create a nicer GUI
 - Add validation functions so you can have the same developer more than once 
 - Create a database for the stores in which you can buy the games from

# Versions 
1.0.0 - Updated 12/05/2022

1.0.1 - Updated 15/05/2022

1.2.0 - Updated 29/05/2022

2.0.0 - Updated 12/06/2022


# Licensing 


# Contributors
Thomas Stoyles

# Acknowledgements 
I would like to thank Leon, Adam and Earl for all there support when delivering this project.
