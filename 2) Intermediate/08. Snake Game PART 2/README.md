
# **THE  SNAKE GAME - PART 2**

***Goals: Detect Collision with Food, Create a Score Board, Detect Collision with Wall, Detect Collision with Tail***


## **1) Detect collision with food:-**

   Goal 4: Our snake should be able to head a piece of food, which is 
           just going to be a blue circle. And every time it touches the food, the circle moves to a new, 
           random location on the screen.

  The food class is going to know how to render itself as a small circle on the screen. And then every 
  time the snake touches the food, then that food is going to move to a new random location.        

   We want this class, food, to inherit from the turtle class. So that way this food class is going to 
   have all of the capabilities of the turtle class, but it's also going to have some specific things that 
   we're going to tell it how to do so that it behaves like an actual piece of food.    

   CHALLENGE: Make the food class inherit from the turtle class.

   Detect when the snake and the food have come into contact and then to tell the food to move itself to a new
   random location.
   distance() method -> (https://docs.python.org/3/library/turtle.html#turtle.distance)

   what is the distance from the snake's head to the food ?
   At this point, you can check to see if it is less than a certain amount, then it's pretty likely that 
   the snake head is now colliding with the food.

   As soon as I collide with that food, the food should go to a new random location.
   Create a method refresh() which is going to create a new random X, a new random Y, and then get 
   the food to go to that new, random location.

## **2) Create a ScoreBoard and Keep Score:-**

   Goal 5: To write some text in our program that keeps track of the score, of how many pieces of 
   food we've actually managed to eat. Now, the score should update every single time we hit a new 
   piece of food and it's going to stay there and keep updating itself every time we hit a new piece of food.
   The scoreboard is also going to be a turtle.

   write() method: (https://docs.python.org/3/library/turtle.html#turtle.write)
   You can tell it what it should write, what kind of alignment you want, do you want it to be in the center of the screen,
   on the left or right side of the screen? And then what kind of font you want?

   CHALLENGE: Create a new file called a scoreboard.py. And inside this file, create a new scoreboard class.
   This scoreboard class is going to inherit from the turtle class.
   The scoreboard is going to be a turtle which knows how to keep track of the score and how to display it in our program.
   Use clear() method so that you clear the writing every time you update the score.

## **3) Detect Collisions with Wall:-**

   Goal 6: If the snake.head has a X coordinate that is greater than 280, so it's gone too far to the right,
   or if it has a X coordinate that is less than -280, so it's gone too far to the left,
   or if it has a Y coordinate that's greater than 280, so too far to the top,
   or if it has a Y coordinate that is less than -280 so it's gone too far to the bottom, 
   if any of these four situations occur then it basically means that the snake has hit the wall.

   In scoreboard create a new function which is going to be called game_over, 
   it's just going to write 'GAME OVER' onto the screen.

## **4) Detect Collision with Tail:-**

   Goal 7: As a snake gets longer and longer, it's more likely that at some point the head 
   might hit some part of the tail. And in the snake game, this means it's game over.

   We need to add a segment to the snake every single time it hits the food so that it grows in length 
   and we can start detecting collision with the tail.

   Create a function that's going to be called extend. And this extend function is going to add a new segment to the snake.
   Create a function add_segment, and this is going to require the position to add the segment to essentially.
   We already have a for loop for adding new segment in create_snake() method, so we can use this.

   Inside our main.py every time our snake collides with the food, then not only are we going to refresh the food,
   but we're also going to get the snake to extend itself.
   
   If the head collides with any segment in the tail, then this means that we're going to trigger the game over sequence.

   When we loop through each of the segments, the first segment is going to be the snake head. And so we're detecting 
   if the snake head has a distance to the snake head of less than 10, which of course it is going to.
   So we need some sort of way of bypassing the snakehead. 
   HINT - use List Slicing.













