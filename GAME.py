import pyglet
from pyglet import shapes

window = pyglet.window.Window(800, 600)

# Create a batch
batch = pyglet.graphics.Batch()

# Player settings
player_width, player_height = 100, 100
player_x, player_y = window.width // 4, window.height // 4
player_speed = 10

# Create player with batch
player = shapes.Rectangle(player_x, player_y, player_width, player_height, color=(0, 0, 255), batch=batch)

@window.event
def on_draw():
    window.clear()
    batch.draw()  # Draw all in batch

pyglet.app.run()