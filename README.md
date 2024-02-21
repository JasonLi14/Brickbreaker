# CSE3130-Project

Brick breaker. You break bricks, they break you.

## Libraries Needed
This game requires the pygame library.

## How to Start
Run the _main.py_ file.

## How to Play
The main objective of Brick Breaker is to break all the bricks, which is done by colliding the ball with the bricks. In later levels, some bricks may require multiple hits to completely break, as indicated by their different colors. To move the brick, there is a paddle that when the ball collides with it, the ball bounces off. If the ball hits the bottom, a life is lost. 

Press SPACE to play the game. 

To move the paddle, press the A key to move it to the left and the D key to move it to the right.

If you break every brick, you automatically proceed to the next level (NOTE TO MR. ZHANG: if you want to skip a few levels, you can change the LEVEL_NUM variable on line 18 in main.py).

## Extra Features
1. There are twenty-five (automatically generated) levels in the game. I designed the objects specifically so that I could easily change a few numbers during instantiation and increase the difficulty of the game (i.e. increase the amount of bricks). I could have unlimited levels, but after a certain point the margins and padding become difficult to manage, so I capped it at ten for this demonstration.
2. Each brick has a health value and a color that corresponds to its health. This means that some bricks have to be hit multiple times before they disappear. The health is randomly generated with limits based on which level it is.
3. For each level, the player only has three lives. If they lose all three lives, they lose the level and have to restart.

## Reflection 
The main design paradigm I had in mind was that I wanted every feature to be easily customizable. For example, I wanted to be able to change the amount of bricks and still have a functioning layout, I wanted to change the size of the paddle, I wanted to be able to change the speed of the ball each level, etc. This helped with creating a system where more and more levels can be created. However, this also prevented me from effective abstraction. I would keep on adding variables that I did not really need and the level object became very complicated. I did not use every single customization that I could have. For example, I did not find myself changing the speed of the ball every level or the size of the paddle. To better work with abstraction, I will set clearer goals at the start of the development process so that I know what to work for, and what features I do need to implement variables and functions for.

Being able to use inheritance definitely saved me a lot of extra code. I was actually surprised by how little code I had to add, especially since I realized that the player and brick sprites could just inherit most of their attributes and methods from the box sprite. One drawback to my approach was that I often referred to BasicSprite's attributes and methods even though Brick and Player were inheriting from Box, which would require me to refer to two classes at once. In addition, composition proved to be a powerful tool, especially for the level class, since it aligned with how I saw the level class. It helped organize all the individual components, such as each brick and the paddle. However, my organization did lead to me typing out lines such as `LEVEL.getBall().getHeight()`, which impacted readability. 

Following IPO felt a little different in pygame, since I found that I had to do a significant amount of "set up" before I could take the player's inputs. For example, I had to create the level object first. In addition, I designed the program so that the level is created before the player inputs because this would allow me to loop through many levels and pause the game between different levels.

To find examples of composition, aggregation, and encapsulation, look at the level.py file. To find examples of polymorphism and inheritance, look at the brick.py file. 
## Sources (for color feature of bricks):
HSV to RGB color conversion. HSV to RGB conversion | color conversion. (n.d.). 
    https://www.rapidtables.com/convert/color/hsv-to-rgb.html 