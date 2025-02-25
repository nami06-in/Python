
# **THE  SNAKE GAME - PART 1**

***Goals: Create a Snake, Move the Snake & Control the Snake***


## **1) Screen Set Up & Creating a Snake Body:-**

   Import turtle and screen class, Create object for screen, setup width and height of screen
   Set black background color for the screen, set title for the screen, use exitonclick() method.

   Goal 1: Create three squares which are each going to be turtles, and they're going to be lined up next 
   to each other along the horizontal axis.
   CHALLENGE: Create 3 turtles and possition them along the horizontal axis.
              Each turtle should be a white square.

## **2) Animating the Snake Segments on the Screen:-**

    Create an empty list and append each new Segments.
    Pull the pen up while creating new segment so as not to draw line while moving.

   Goal 2:  Move the snake automatically across the screen without having to do anything.

   tracer() method (https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.tracer) 
   of class screen takes a number as a input, and it turns the animation on or off.
   And when the tracer is turned off, then we can use the update() method to tell our program 
   when to refresh and redraw the screen.

   Initially turn off the tracer by setting it to 0. Untill we call update() method the screen is 
   not going to refresh and it's not going to show us what's been happening in our code.
   
   Use sleep() method from time module to see the movement of snake.
   After calling the sleep() place update() before and after the loop (for seg in segments:).
   
   while turning the turtle, only the 1st square will turn and the second square will continue moving forward.
   So inorder to avoid this, initialy move the third square to the second square possition,
   then move the second square to the first square position, then move the first square up or down.
    
   So the for loop for looping segments should be in reverse order.

## **3) Create a Snake Class and Move to OOP:-**

   All the parts that are related to the snake's behavior and the snake's appearance go into a separate
   class.
   By the end of the whole project, we should end up with three classes; a snake class, a food class,
   and a scoreboard. And all of these classes will be in separate files, managing only one thing.

## **4) Control the Snake with a Keypress:-**

   Goal 3: Control the snake by using the up, down, left, and right arrow keys.
   create 4 functions in the class. 

   Create an attribute for the first square in the contructor.

   Snake can't move back on itself, so avoid this.
   when the head is pointing towards down direction, then we shouldn't allow it to go up. 
   And similarly, when it's pointing up, we shouldn't let it go down, when it's pointing right
   we shouldn't let it go left.













