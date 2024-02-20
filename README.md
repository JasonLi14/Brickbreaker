# CSE3130-Project

Brick breaker. You break bricks, they break you.

## Libraries Needed
This game requires the pygame library.

## Extra Features
1. There are ten (automatically generated) levels in the game. I designed the objects specifically so that I could easily change a few numbers during instantiation and increase the difficulty of the game (i.e. increase the amount of bricks). I could have unlimited levels, but after a certain point the margins and padding become difficult to manage, so I capped it at ten for this demonstration.
2. Each brick has a health value and a color that corresponds to its health.

## Reflection 
The main design paradigm I had in mind was that I wanted every feature to be easily customizable. For example, I wanted to be able to change the amount of bricks and still have a functioning layout, I wanted to change the size of the paddle, I wanted to be able to change the speed of the ball each level, etc. This helped with creating a system where more and more levels can be created. However, this also prevented me from effective abstraction. I would keep on adding variables that I did not really need and the level object became very complicated. I did not use every single customization that I could have. For example, I did not find myself changing the speed of the ball every level or the size of the paddle. To better work with abstraction, I will set clearer goals at the start of the development process so I know what to work for, and what features I do need to implement variables and functions for.

## Sources (for color feature of bricks):
HSV to RGB color conversion. HSV to RGB conversion | color conversion. (n.d.). 
    https://www.rapidtables.com/convert/color/hsv-to-rgb.html 