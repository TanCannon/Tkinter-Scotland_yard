
# Tkinter - Scotland Yard

A python implementation of the board game 'Scotland Yard'.
This gui replictes the famous Scotland Yard.
"Scotland Yard is a board game in which a team of players controlling different detectives cooperate to track down a player controlling a criminal as they move around a board representing the streets of London." you may have seen its ad on the tv by funskool.

It's my first GUI. Currently i have learned python and i'm trying to see python capabilites or you can say application.
It's made with Tkinter module in python. The program uses a other similar module, customTkinter. Thanks to this guy Tom Schimansky GitHub i got this amazing thing. It just make the old looking tkinter so much modern.

I've designed my Scotland Yard game in Tkinter with the UI divided into three main sections: the left frame, which shows moves and ticket options, the bottom frame for the start and quit buttons, and the map frame, where the actual map is displayed. To handle the images—like player pieces, the map itself, and the path highlighters—I’ve used the Pillow library since it works well with Tkinter.

For setting up stations and their possible routes, I’ve manually written coordinates into two text files. One file defines station objects with possible paths (bus, taxi, underground), and the other places sky-blue highlighters on stations where players can move. I use the linecache module to read these coordinates from the files and segregate the information accordingly.

I’ve written three key classes:
stop: This class handles possible routes from a given station.
player: It stores details about each player, like their current location and how many tickets they have for each transport type.
Mr_X: This class inherits from player and represents the criminal that the detectives are trying to catch.

The game starts with the main() function, which sets up the player classes and objects. Then, the next() function highlights the possible moves a player can make by placing interactive highlighters on the map. When one of these highlighters is clicked, it triggers the move() function, which creates a dropdown menu on the left frame showing available tickets for travel. Once a ticket is selected and "travel" is pressed, the player’s position is updated using update_player().

To keep track of everything, I store various objects in lists, which I can easily access based on the player's turn. I’ve also added an auto-scroll feature to the map, which shifts the view to the current player’s location at the start of each turn. This keeps the focus on the player who’s actively making a move.


## Demo video

[![Watch the video](https://img.icons8.com/color/48/000000/video.png)](https://drive.google.com/file/d/1LGmJzA69A8PCcSUymUGDJFFAYqjqFXUq/view?usp=sharing)

## Screenshots

Screenshot(25)

![App Screenshot](https://github.com/TanCannon/Tkinter-Scotland_yard/blob/main/Screenshots/Screenshot%20(25).png)

Screenshot(31)

![App Screenshot](https://github.com/TanCannon/Tkinter-Scotland_yard/blob/main/Screenshots/Screenshot%20(31).png)

More screenshots [here](https://github.com/TanCannon/Tkinter-Scotland_yard/tree/main/Screenshots)

## Installation

Download the [Scotland_Yard_exe.zip](https://github.com/TanCannon/Tkinter-Scotland_yard/releases)

Unzip it in your laptop and look for the Scotland yard exe in it . That's the application.
Have fun!😊
    
## Documentation

[Game rules](https://github.com/TanCannon/Tkinter-Scotland_yard/blob/main/Rules.pdf)

## Issues

The game window is not responsive yet it works okay till a 5 inch laptop further I have no idea😅.

The code is ain't efficient yet.

## Future Goals

I will want to add animation to player pieces and other stuff.

Add sounds too.

A continue functionality.

Map zooming option.

And the most important responsive.

