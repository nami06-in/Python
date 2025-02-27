
# **The Turtle Crossing Game**

## **STEP 1: How the Game Play Works:-**

   1. A turtle moves forwards when you press the "Up" key. It can only move forwards, not back, left or right.
   2. Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.
   3. When the turtle hits the top edge of the screen, it moves back to the original position and the player levels up. 
      On the next level, the car speed increases.
   4. When the turtle collides with a car, it's game over and everything stops.

***GOALS: (1) Move the turtle with Keypress***
       ***(2) Create and move the cars***
       ***(3) Detect collision with car***
       ***(4) Detect when turtle reaches the other side***
       ***(5) Create a scoreboard***

## **2) STEP 2: Break Down The Problem:-**

   **Goal 1:** Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle north.
   (NOTE remember to put listen() while using onkey)

   **Goal 2:** Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge of 
   the screen. No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone for our little turtle). 
   Hint: generate a new car only every 6th time the game loop runs.

   **Goal 3:** Detect when the turtle player collides with a car and stop the game if this happens. 

   **Goal 4:** Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y). 
   When this happens, return the turtle to the starting position and increase the speed of the cars. Hint: think about 
   creating an attribute and using the MOVE_INCREMENT to increase the car speed.

   **Goal 5:** Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a 
   successful crossing, the level should increase. When the turtle hits a car, GAME OVER should be displayed in the centre. 
