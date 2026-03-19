import pyglet
import sys

#from pyglet.window.key import R

#this loads the python library so you can use its tools like windows,shapes,and keyboard input.

#craete a window
window = pyglet.window.Window(800,600)
#create a window that is 800 pixels wide and 600 pixels tall.This is where your game will appear.

#create a batch
#batch = pyglet.graphics.Batch()

#set player size and position
player_width, player_height = 100, 100
player_x = player_y = window.width // 4, window.height // 4
player_speed = 10
#Defines:
         #size of the player(100x100 pixels)
         #starting position(1/4 of the way across and down the screen)
         #HP fast it moves when a key is pressed

#import shapes and create player
from pyglet import shapes
player = shapes.Rectangle(player_x, player_y, player_width, player_height, color=(0, 0, 255))  # Blue

player = shapes.Rectangle(player_x, player_y, player_width,player_height)
#shapes.Rectangle draws a blue rectangle ( (0,0, 255)is blue in RGB)
#it uses the position and size we set earlier

Handle keyboard input
@window.event
def on_key_press(symbol, modifiers):
    global player_x, player_y
    if symbol == pyglet.window.key.LEFT:
        player_x -= player_speed
    elif symbol == pyglet.window.key.RIGHT:
        player_x += player_speed
    elif symbol == pyglet.window.key.UP:
        player_y += player_speed
    elif symbol == pyglet.window.key
         player_y -= player_speed
    #this runs when you press a key.
    #global lets us change player_x and player-y from inside the function.
    #symbol checks which key was pressed(e.g.,left arrow).
    #we update the player's position based on the key.

#Draw everything on screen
@window.event
def on_draw():
    window.clear()
    player.x = player_x
    player.y = player_y
    player.draw()
#this runs everytime the screen refreshes.
#windows.clear() erases the old frame
#we update the rectangle's position to match player_x and player_y.
#player.draw() shows the rectangle in the new position.

#Run the game
pyglet.app.run()
#starts the game loop.pyglet now listens for event(like key presses)and keeps the window open

