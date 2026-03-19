import pyglet
import sys

#creating windows

window_width, window_height = 400, 300
window = pyglet.window.Window(width=window_width, height=window_height)


#filling the screen with white color
from pyglet.gl import glClearColor

#set beckground color to white (values 0.0 to 1.0)
#glClearColor(5.0, 7.0, 9.0, 0.0)


#Add shapes,text,sprites here (after window creation
from pyglet import text
label = text.Label("Football",
                   x=window.width//2,
                   y=window.height//2,
                   anchor_x="center")
from pyglet import shapes
rectangle = shapes.Rectangle(100,100,200,100,color=(155, 155, 155, 0, 0,0))

@window.event
def on_draw():
    window.clear()
    label.draw()
    rectangle.draw()

def update(dt):
        label.x +=50 * dt #move right

pyglet.clock.schedule_interval(update, 1/40.0)


#add key event
@window.event
def on_key_press(symbol,modifiers):
    if symbol == pyglet.window.key.LEFT:
        label.x -= 20
    elif symbol == pyglet.window.key.RIGHT:
        label.x += 20




pyglet.app.run() #Run last









