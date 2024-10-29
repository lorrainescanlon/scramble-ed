


# Scramble Ed

## Code Institute - Portfolio Project 3 - Python Essentials

This website was created to demonstrate my ability to develop a command-line  application using Python.

Scramble Ed is an interactive terminal based word guessing game. The user tries to unscramble an Ed Sheeran song title before they run out of time or use up their lives.

### A live demo of the website can be found [here](https://scramble-ed-298bb66f3eff.herokuapp.com/)

## Demo
![How the website looks on different devices](docs/images/amiresponsive.PNG)


# Table of Contents
- [Scramble Ed](#scramble-ed)
  - [Code Institute - Portfolio Project 3 - Python Essentials.](#code-institute---portfolio-project3-python-essentials)
- [Table of Contents](#table-of-contents)
  - [Demo](#demo)
    - [A live demo website can be found here](#a-live-demo-of-the-website-can-be-found-here)
  - [UX](#ux)
    - [How to Play](#how-to-play)
  - [User Stories](#user-stories)
    - [Strategy](#strategy)
    - [Scope](#scope)
  - [Planning](#planning)
    [Design](#design)
  - [Technologies](#technologies)
  - [Features](#features)
    - [Existing Features](#existing-features)
    - [Future Features](#future-features) 
  - [Testing](#testing)
    - [Validator Testing](#validator-testing)
    - [Bugs](#bugs-encountered)
  - [Deployment](#deployment)
  - [Credits](#credits)
    - [media](#media)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)




## UX
This appliaction is aimed at people who have an interest in word games and pop music. It aims to appeal to people of all ages as users can easily interact with the content and navigation is led by the application.



## User stories
- As a user I want the purpose of the website to be clear and immediate. This is achieved through the title banner and instructions visible on the landing page.
- As a user I want the site design to be engaging and fun. I believe this has been achieved with the use of colour and ascii art.
- As a user I want to easily navigate between the different areas on the site. Navigation is logical and follows the course of the game.
- As a user I want to see what I've scored. This is achieved through the use of a score board that loads at the end of the game.
 

### Strategy
The goal is to create a fun and engaging word game. The focus is on presenting the content clearly and ensuring that the game is easy to follow. 

### Scope
To include features that enhance the user experience and provide value to the user. Features such as the ascii art and scoreboard achieve this.




## Planning

Excel spreadsheet on googledrive

## Design
The website is desinged with a sequential structure which the user can navigate through with ease.

The user is presented with a landing page with an ascii heading 'Scramble Ed' and the rules of the quiz. The landing page allows the user to input a username to start the quiz. From here the user is taken through the steps in the game with the option to quit at various intervals. 

The design is limited as the application runs in a console window. 
- Ascii art has been used to display the game title, scoreboard heading and guitar images. 
- Different colour text has been used to enhance the user experience.
- The scrambled word appears to the console using a typewritter effect.


## Technologies
- Python - To create the application.




## Features 
The following features are included on the website.
### Existing Features

- __Home Page__
  - The home page includes a text heading telling the user that this is a Flag Quiz. 
  - This section lists the game rules and contains a form where the the user is asked to enter a username of their choice.
  - The form uses validation, the user must enter a username in order to continue.
  - When the user clicks the play button, form validation takes place. If the user has entered a username then the quiz page 
    is loaded otherwise they are prompted to enter a username to continue.

![Home Page](docs/images/homepage.jpg)

- __Quiz Page__
  - The quiz page displays the flag and 4 answer choices to the user. 
  - It displays a flag number counter.
  - It also displays the users current score.
  - When the user selects their answer, a correct answer is indicated by the answer button turning green and 
    an incorrect answer is indicated by the button turning red.
  - Once a choice is selected, the flag and answer choices refresh. The flag counter increases and if the user answered correctly their score also increases by 1.
  - The flag is removed from the array if it is guessed correctly to eliminate repetition. 
  - The Quit button returns the user to the homepage.

![Quiz Page](docs/images/quizpage.jpg)
![Correct Answer](docs/images/quizpagecorrect.jpg)   
![Incorrect Answer](docs/images/quizpageincorrect.jpg)

- __Game Over__
  - The game over page loads when the answer to the last flag has been selected.
  - It displays a message telling the user their final score.
  - A table is also used to display the current top 5 scores.
  - A play again button allows the user to restart a new game.

![Game Over](docs/images/gameover.jpg)    

### Future Features
- An additional bonus question to the end of each round with a true or flase question based on the region in particular. A higher score could be awarded for a 
  correct bonus answer.
- Display a breakdown of scores by rounds on the game over page to show users what regions they need to improve their knowledge on.
- Improve the timer function. 
- Maybe gain extra score points for time left over.


## Testing
- This application has been tested on different browsers such as Chrome, Firefox and Microsoft Edge.
- This page has been tested on laptop and mobile devices.
- Responsiveness and functionality have been tested on all screen sizes using the dev tools device toolbar.
- The username input field has been tested successfully. 
- All pages passed lighthouse testing for performance, accessibility, best practices and search engine optimization. 

### Validator Testing 
- All code has passed through the [Code Institute Python Linter](https://pep8ci.herokuapp.com/)

## Bugs Encountered
- On earlier tests I noticed that some titles were returned readable after being scrambled. Like bam bam and lego house. I added and if statement to the split and scramble function to return the scrambled title only if it was not equal to the title otherwise run the function again.
- When validating the code in the Python Linter I ran into some console errors relating to the use of escape sequence characters in the ascii art I had used. 
W605 invalid escape sequence '\_' 
Putting an r before the images solved this problem.
- I also encountered errors where I had exceeded 80 characters per line. 
E501: line too long. I resolved these by breaking up the lines with \ where appropriate. I also shortened variable names I had given to apply colours as these  were used in a lot of my strings.
- The timer function doesn't currently perform how a user might expect. The function is called at various points when the user interacts with the game but does not interrupt play when time runs out. I would need to run the timer function along with other functions simultaneously to achive this. I believe there is a way using threading, unfortunately this was beyond my skills at this time but would be something I would like to implement in the future. 

### Unfixed Bugs
- 

## Deployment
- The site was deployed to Heroku, the steps used were as follows: 
  - Create and login to your heroku account. 
  - On your heroku dashboard, click the new button and 'create new app' from the dropdown menu.
  - Enter the name of the app 'scramble-ed', select region as 'Europe' and click the 'Create app' button
  - On the app screen select the 'Settings' tab.
  - Find the 'Config Vars' section and enter the following: 
  KEY :Port and VALUE: 8000
  - Now find the 'Buildpacks' section and add the 'Python' and 'Node.js' buildpacks. They need to be added in order, Python first and the Node.js.
  - Scroll back to the top of this page and find the Deploy tab. 
  - On this page find 'Deployment method' and select 'GitHub'.
  - In the 'Connect to Github' section enter the name of your repository and click 'Connect'.
  - On the deploy page select your preferred deployment type I choose 'Enable Automatic Deploys'.
  - The app will be built on your next push to github.
  - Once created the app appears on your heroku dashboard. 
  - Click on app and your dashboard and 'Open app' from the app page. 
  - The app opens in a console loaded in a browser window.


## Credits 
The following is a list of resources that were used for this website.

### Media
- ASCII art by Harry Mason at [ASCII Art Archive](https://www.asciiart.eu/)

### Code
 - Template used was [Python Essentials Template](https://github.com/Code-Institute-Org/python-essentials-template) provided by the Code Institute
 - I used the following discussion to help create my function to scramble the song title strings [Stack Overflow](https://stackoverflow.com/questions/6181304/are-there-any-ways-to-scramble-strings-in-python) 
 - I used the following article as a basis for my typewritter function. [Python in Plain English](https://python.plainenglish.io-typewriter-animation-using-python-7f4275e812bf)
 - I used code at the following source to create my clear function. [Geeks for Geeks](https://www.geeksforgeeks.org/clear-screen-python/)
 - ASCII art by Harry Mason at [ASCII Art Archive](https://www.asciiart.eu/)
 - I used code found at the following thread to create my colour class [Stack Overflow](https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal)


### Acknowledgements
- I am gratefull to the Code Institute tutor support team for helping and guiding me in the right direction.
- A special thanks to my mentor Medale Oluwafemi for his guidance and great advice.



[def]: 
