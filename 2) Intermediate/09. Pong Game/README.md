
# **PONG: THE FAMOUS ARCADE GAME**

***GOALS: (1) Create the Screen***
       ***(2) Create and move a Paddle***
       ***(3) Create another Paddle***
       ***(4) Create the Ball and make it move***
       ***(5) Detect Collision with wall and Bounce***
       ***(6) Detect Collision with Paddle***
       ***(7) Detect when Paddle misses***
       ***(8) Keep Score***


## **1) Set up the main Screen:-**

   Goal 1: Create the starting screen. It's going to be a screen that has a height of 600 pixels and a width of 800
   pixels. It should be black in terms of the background color, and it should stay on the screen until we click on it.

## **2) Create a Paddle that responds to key presses:-**

   Goal 2: The paddle that we're going to create is going to be on the right side. It's going to have a width of 20,
   a height of 100 and be positioned at 350 pixels on the X-axis and then 0 on the Y-axis. 

   To move paddle up: Create our go_up function. And this function is going to take our paddle and move it so that it goes to a
   new position. The new exposition is X not going to change. The only one that's going to change is the Y position.

   turn the animation of paddle off and update the screen after creating paddle turtle
   tracer() and update() in screen class


## **3) Write the paddle class and create the second paddle:-**

   Goal 3: Create paddle.py for the Paddle class. The Paddle class needs to inherit from Turtle.
   Paddle objects need to be initialised with a tuple for the X and Y coordinates.
   The left paddle needs to move up and down using the "w", "s" keys.

   to replace a variable: Edit -> find -> replace

## **4) Write the Ball class and Make the ball Move:-**

   So this ball is going to be created as a separate ball class and the ball object that we're going to 
   create from it will have a width of 20, height of 20, and it's X and Y position will start out at the center of the screen.

   Now when the screen refreshes, the ball is automatically going to move on the screen and it's going to move up
   and also to the right. So it's X and Y positions will change on every refresh of the screen.

   Use time module to slow down the ball

## **5) Add the Ball Bouncing Logic:-**

   CHALLENGE: The screen is 600px tall. Detect Collisions with the top and bottom walls.
   change the ball's movement direction upon Collision.
   HINT: Consider creating 2 attributes in the ball class to track movement.

   The y coordinate decreases while Bouncing.

## **6) How to Detect Collisions with the Paddle:-**

   Normally we measure distance between the ball and the paddle to detect Collisions.
   The problem arrises when the ball hits the edge of the paddle.
   The distance() method measures the center of the ball from the centre of the paddle as the distance.

   We could add on an additional condition. We could check well if the ball has gone past a certain point on the X-axis,
   if it's gone far enough over to the right and it's within a 50 pixel distance of the paddle, 
   then that also means it's made contact with the paddle. 

## **7) How to detect when the ball goes out of Bounds:-**

   CHALLENGE:- Detect if the ball goes out of Bounds at the edge of the screen.
   If yes, reset the ball's position to the centre of the screen.
   The ball should then start moving to the other player.

## **8) Score Keeping and Changing the Ball Speed:-**

   The l_score and r_score methods defines the Score

   Everytime the ball touches the paddle the speed should increase.
   this can be done in sleep() in while loop, but it cannot be negative number
   so we multiply by 0.9 
   