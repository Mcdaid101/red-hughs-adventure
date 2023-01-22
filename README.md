# Red Hugh's Adventure

Red Hugh's Adventure is a Python terminal adventure game which runs in the Code Institute's mock terminal on Heroku.

Players must navigate their way through Dublin castle and escape through an exit while solving puzzles along the way. 

You can find the live site [Here](https://red-hughs-adventure.herokuapp.com/).
####

![Website Mock Up](assets/images/multi_device_mock_up.png)
&nbsp;

# Purpose
I built this website as my third project for the code institutes full stack development and e-commerce applications course. 
I built this website from scratch using the knowledge I gained from the course where I studied the basics of Python.

# Target audience
* Gamers
* Terminal text based adventure game lovers 

## How to play
* This game is constructed like a traditional text adventure game where the player is asked to input what direction they would like to head. 

* For example head north for kitchen, head south for bedroom and head east for bathroom.

* Once the desired input is entered the player will arrive there and be allowed to return to previous locations with items picked up from other ones.

* Items acquired through visiting new locations and solving puzzles are vital to the player's progress and will allow he/she to escape and complete the game. 

* If a player is caught or killed by the guards they will fail the game and be offered another attempt. 

## Features 

1.  The game features 10 different rooms / areas to explore some are possible to return to while others such as the area you began in, are not.

<details><summary>Different Areas</summary>
<p>

![Tunnels](assets/images/tunnels.png)

![watch house](assets/images/watchhouse.png)

![dungeon](assets/images/dungeon.png)

![courtyard](assets/images/courtyard.png)
</p>
</details>
<br>

2.  The player is given multiple choices to explore a different direction in each room / area they venture into. 

3. The game accepts user input to add their name, which is referenced throughout and to move direction and tells the player to enter which word to go which direction. 
<details><summary>Multiple choices for navigation</summary>
<p>

![courtyard](assets/images/courtyard.png)
</p>
</details>
<br>

4. User input can also determine whether the player wants to undertake a certain task or pick up an object. 

<details><summary>Choice of task</summary>
<p>

![wardens office](assets/images/wardens_office%20.png)
</p>
</details>
<br>

5. Validation is implemented on every choice the player can make, if a player enters something other than the game requested, they will be met with text that is coloured red to tell them the only options they can enter to proceed. 

<details><summary>Input validation</summary>
<p>

![courtyard](assets/images/must_enter_name.png)
</p>
</details>
<br>

6. If the player is caught or killed by the guards he will lose, the game will then offer them another chance to play again or to exit the game entirely. 

<details><summary>Game over</summary>
<p>

![courtyard](assets/images/key_failed.png)
</p>
</details>
<br>

7. The delay print function makes the text print out slowly as if it is just appearing on screen one letter at a time mimicking text adventure games which were popular in the 1980's.

8. The text's green color is also chosen to make the game seem like a terminal adventure game from the past, it gives the game a retro and authentic feel.

9. To differentiate between each room unique ASCII art is loaded on entering giving the game a better design. 

10. A progress bar which simulates a new area rendering is added to the bottom of each area when the player inputs which direction he would like to go. 

<details><summary>Loading area bar</summary>
<p>

![courtyard](assets/images/tunnels.png)
</p>
</details>
<br>

## Future Features 

* An OOP combat system when facing the guards 
* Allow players to interact with their fellow prisoner Red Hugh and find out more about him. 
<br>

# Design 

![Flow Chart](assets/images/flow_chart%20.png)

<br>

* I designed this game to make it look like an old 80's style terminal game.
* To do this I created the delay_print() function which printed out the game's script in a typewriter esque way.
* Using the colorama library I gave the text a green colour with Fore.GREEN, to further it's traditional terminal game feel.
* I used Fore.RED to give any validation fails and the game ending screens the colour red. 
* Textualize Rich created the progress bar to simulate the new areas rendering.
* The ASCII art comes from an online Generator and from an ASCII art archive which was very useful and saved me typing out any ASCII images. 
* Regex helped me with input validation to ensure that the players inputs matched the games input directions

<br>

## Issues with design

* Orginally each areas script and ASCII art was loaded with a simple print function but this proved to be too messy and left the code readability very poor along with making it very hard to maintain. I then created two dictionaries to pull the scripts and images from. 
<br>

* To keep the player from having to enter the intro section and have to read the script once again I removed it after the intro sequence was done. Bypassing the intro and having them go straight from the courtyard to the dungeon and vice versa. 
<br>

* To save me printing out the script and image to be loaded in each scene I created the display_scene() function in which I could pass the dictionary key's in as parameters, making my code even more readable and easier to maintain. 

# Technology Used 
<br>

## Languages 
* Python
<br>

## Tools and Frameworks
* Git 
* Github 
* Vs Code IDE in browser
* Textualize rich
* Techsini Multi Device Mockup Generator used in this readme to display an image of the website on different devices 
* Colorama 
* Heroku
* Imported RegEx for validation
* Imported Time, sleep for functions
* Imported OS to run clear screen

# Bugs 

* Originally was getting errors in the Heroku Terminal as I had not added Textualize rich and Colorama to the requirements.txt file, adding them to the file quickly fixed this. 
<br>

* The game would load the return from the castle gates with no key function even when the player had pickpocketed the key successfully, I soon realized I had not initialized the key as a global variable. 
<br>

* No bugs remained after this. 
<br>

# User stories

## First time stories 
* As a first time user: I want to be able to know how to play the game<br>
Testing done to make sure that game instructions on how to navigate to each room display in the terminal  
<details><summary>First time user 1</summary>
<p>

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Game directions | Check Direction options appear in the python terminal | Directions load at end of each scene giving you option to move on to next area or go back the way you came  | Works as expected |
</p>
</details>
<br>
<br>

* As a first time user: I want to be able to navigate through the game.  <br>
 Testing done to ensure that the game is fully functional.
<details><summary>First time user 2</summary>
<p>

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Game Directions | Check that each direction you enter brings you to the said location | The player moves on to the expected room they entered the direction for and it appears in the "you chose to enter: " line | Works as expected |
</p>
</details>
<br>
<br>

* As a first time user: I want to be able to input my name in the Game<br>
 Testing done to ensure that the players Name is asked upon the game's start.
<details><summary>First time user 3</summary>
<p>

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Name input | Load up the game in the Heroku terminal, on the title screen it will ask the player to input their name | The game will welcome you with your name | Works as expected |
</p>
</details>
<br>
<br>

* As a first time user: I want to be able to re-enter my name if I typed nothing and pressed enter by mistake <br>
 Testing done to ensure that when the game will not commence unless the player has entered a name.
<details><summary>First time user 4</summary>
<p>

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Name input |The player must enter a name for the game to commence  | With no name entered the gane will not commence, the terminal will ask the player for their name again until they enter something | Works as expected |
</p>
</details>
<br>
<br>

* As a first time user: I want another attempt at entering a direction if I mispress a key <br>
 Testing done to ensure that the game will repeatedly ask which way the player would like to go until they input one of the directions stated. 
<details><summary>First time user 5</summary>
<p>

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Directions validation |Input something other than the requested input for directions | The game will request you only enter one of the stated input directions | Works as expected |
</p>
</details>
<br>
<br>

* As a first time user: I want different ways of winning the game <br>
Testing done to ensure the multiple ways of winning the game work.
<details><summary>First time user 6</summary>
<p>

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Winning the game | Escaping by either having a sword or gaining the key  | When the player acquires the sword or key variables they can then complete the game | Works as expected |
</p>
</details>
<br>
<br>

* As a first time user: I want to view the ASCII art to differentiate between rooms and enjoy the game<br>
 Testing done to ensure that the game displays the ASCII art.
<details><summary>First time user 7</summary>
<p>

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| ASCII art | Make sure that the ASCII art loads for each area and at the beginning and end of each game  | The ASCII art displays for each new scene and beginning and end of each game | Works as expected |
</p>
</details>
<br>
<br>

*  As a first time user: I want to be able to play the game again if I lose <br>
 Testing done to ensure that once you lose the game you can play again.
<details><summary>First time user 8</summary>
<p>

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Play again option | Once you lose the game you can input yes to have another go | The game will reload and you can play again | Works as expected |
</p>
</details>
<br>
<br>

* As a first time user: I want to be able to see the next room is loading. <br>
Testing done to ensure that the progress bar loads.
<details><summary>First time user 9</summary>
<p>

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Loading area bar | Check that the loading area bar loads upon the end of each scene | Progress bar appears at end of each scene | Works as expected |
</p>
</details>
<br>
<br>

## Returning stories

* As a returning user: I want to be able to play the game again if I win and try win another way<br>
 Testing done to ensure that once you win the game you can play again.
<details><summary>Returning User 1</summary>
<p>

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Play again option | Once you win the game you can replay the game and try complete it another way | Option appears once you have won the game to replay the game and win another way | Works as expected |
</p>
</details>
<br>
<br>

* As a returning user: I want to be able to refuse or accept different tasks / objects <br>
Testing done to ensure that the player can refuse or accept different tasks / objects.
<details><summary>Returning user 2</summary>
<p>

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|refuse or accept tasks and picking up objects | The player can refuse or accept to play the pickpocket game or pick up the sword | Accepting or refusing these tasks/objects have profound impacts on the game's narrative.  | Works as expected |
</p>
</details>
<br>
<br>

## Owner stories 
* As the site owner: I want to be able to maintain the games code easily <br>
Testing done to ensure that the code is easily readable and maintained
<details><summary>Site owner 1</summary>
<p>

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|ASCII art images and game scripts are in a dictionary | placed images and scripts in dictionaries  | Code much more readable and maintainable | Works as expected |
</p>
</details>
<br>
<br>

* As the site owner: I want players to have a new experience each time they play  <br>
Testing done to ensure that players have multiple different ways to win and lose. 
<details><summary>Site owner 2</summary>
<p>

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Different ways to win and lose | Check to see the multiple different ways to win and lose produce the win and lose scenes | Win and lose functions appear at different ways to win and lose  | Works as expected |
</p>
</details>
<br>
<br>

* As the site owner: I want users to get different answers for a challenge to keep them interested and enhance the games replay value.  <br>
Testing done to ensure the warden mini game produces a different answer with each game.
<details><summary>Site owner 3</summary>
<p>

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Pickpocket mini game produces a different each time you play | Ensure the Math.random function works in the pickpocket mini game | The pickpocket game produces a random answer each game | Works as expected |
</p>
</details>
<br>

# Testing and validation

I have manually tested this project by doing the following:

* Passed the project through a pep8 linter and confirmed there is no problems.
* Tested in my gitpod terminal and the Heroku terminal.
* Tested each user story to make sure each one passes. 

Pep8
* No errors were returned from Pep8online.com or from extendsclass.com/pythontester. 


# Deployment 

## Creating this project
This project was created by navigating to the Code Institute's python student template and clicking the 'use this template' button. I then inputted the repository name "red-hughs-adventure" and included all branches. With the repository now created, I used the browser version of Vs Code to create the project. 
<br>

I used the following commands throughout this project:
* Git add . - This added my file to the staging area to be committed
* Git commit -m - This command committed any changes to the local repository along with a message
* Git push - pushed my changes to the github repository and to Heroku 
* git reset --hard HEAD^ - This removed my last commit 
* python3 run.py - This ran my code in the terminal

## Heroku
 This game is deployed on the Code Institute's mock terminal on Heroku

### Steps for deployment 
* Fork or clone this repository
* Created a new heroku app through build app
* Set the buildpacks to Python and NodeJs in that specific order
* Linked the heroku app to the repository via github
* Clicked automatic deploys so each git push would automatically go to the heroku app
* This was ideal for testing so I could see what the game looked like on the Heroku terminal with each git push

# Credits 

## Code 
* The code for the delay_print() function was inspired from a post on stack overflow [here](https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line")
* The code for the progress bar is taken from textualize rich, a python terminal style package [here](https://rich.readthedocs.io/en/stable/introduction.html)
* The colour functions are imported form a python terminal style package called colorama you can find it [here](https://pypi.org/project/colorama/)

## Media 
* Some of the ASCII art was generated [Here](https://patorjk.com/software/taag/#p=testall&h=2&v=2&f=Relief2&t=Courtyard)
* Some of the ASCII art is taken from an ASCII art archive [Here]("https://www.asciiart.eu/")

## Acknowledgements 
* I would like to thank my mentor Ronan Mc Clelland for his help and guidance while I built this project.
* I would like to thank my family for their love and support.
* And finally my girlfriend for her advice on my game's style. 