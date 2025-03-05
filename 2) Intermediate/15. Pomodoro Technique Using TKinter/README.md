
# **POMODORO  GUI  APPLICATION**

***Pomodoro Rule:-***
                ***25 min work  (reps = 1)  check_mark -> 0 (for loop will not work)*** <br />
                ***5 min break  (reps = 2)  check_mark -> 1*** <br /><br />
                ***25 min work  (reps = 3)  check_mark -> 1*** <br />
                ***5 min break  (reps = 4)  check_mark -> 2*** <br /><br />
                ***25 min work  (reps = 5)  check_mark -> 2*** <br />
                ***5 min break  (reps = 6)  check_mark -> 3*** <br /><br />
                ***25 min work  (reps = 7)  check_mark -> 3*** <br />
                ***20 min break  (reps = 8)  check_mark -> 4*** <br /><br />

## **1) How to work with the Canvas Widget and Add Images to TKinter:-**

   Canvas Widget: It allows you to layer things one on top of the others. So you could draw something and 
   then you can draw something on top of that. And what it allows us to do in our case is to place an image 
   onto our program and then to place some text straight on top of that.

   PhotoImage: this class comes from  and it's basically a way to read through a file and to get hold of a particular 
   image at a particular file location.

   If the image is a little bit cut off then change the size in canvas.create_image.
   color pallette: https://colorhunt.co/

   Fill both window as well as canvas with yellow background color, but still there will be a 
   white border on the canvas, to remove this use the attribute "highlightthickness"

## **2) CHALLENGE: Complete the Application's User Interface(UI):-**

   HINT: To color a piece of text in a label, 'fg' attribute is used.
         Copy Paste the checkmark symbol from wikipedia.
         Use grid() instead of pack.
   complete UI according to this image: UI image.jpg
   Reffer Other_Tkinter_Widgets.py

   To get rid of border in button use highlightthickness".

## **3) Add a Count Down Mechanism:-**

   There is a method called after() in window object. 
   after(): It's a method that takes an amount of time that it should wait and then after that amount of time, 
   it simply calls a particular function that you tell it to call passing in any arguments that you want to give it.

   To change the text inside the tomato to the count time, assign the canvas.create_text to a variable.
   To change a canvas element call the method itemconfig().
   Call the count_down() after creating canvas, inorder to avoid error. This function will be called by start_timer()
   inorder to tie it with start button.

   CHALLENGE: Call the start_timer() when the start button get's pressed.

   Now we need to put the timer in 00:00 format i.e min:sec format.
   We know that 5min = 5 * 60 seconds.

   Inorder to get minutes from seconds divide by 60.
   Inorder to get how much is left after cleanly divided use %, i.e reminder.

   Difference between math.floor() and round():
     round(3.8) = 4 
     math.floor(3.8) = 3 
   floor() is useful when you need to discard the decimal part completely.
   round() is used for typical rounding scenarios.

## **4) Dynamic Typing Explained:-**

   Dynamic Typing: Change a variable's data type by changing the content in that variable.
   a = 3 (type - int)
   a = "Hello" (type - str)

   Python allows you to change the data type of a variable just by assigning it to a different type of value.
   https://stackoverflow.com/questions/11328920/is-python-strongly-typed

## **5) Setting Different Time Sessions and Values:-**

   CHALLENGE: Use the reps variable to count down the appropriate number of seconds.
   When you run the program the timer needs to switch between counting down the 
   work time and the break time (test with 1 minute rather than 25 minutes)

## **6) Adding Checkmarks and Resetting the Application:**

   CHALLENGE: Add one checkmark for every 2 reps.
   
   To cancel the timer set up, use after_cancel() method, so set after() method inside a variable.
   Since this variable is used inside function declare it globaly with initial value none.
