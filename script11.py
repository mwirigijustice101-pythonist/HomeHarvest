
import matplotlib.pyplot as plt
import numpy as np

class RoboticArm:
    def __init__(self, lengths=[5, 4, 3]):
        self.lengths = lengths
        self.angles = [0, 0, 0]  # shoulder, elbow, wrist in radians
        self.gripper_open = True
        self.holding_object = False
        self.object_pos = [6, 2]  # initial block position

    def set_angle(self, joint, angle):
        self.angles[joint] = np.deg2rad(angle)

    def adjust_angle(self, joint, delta):
        self.angles[joint] += np.deg2rad(delta)

    def toggle_gripper(self):
        if self.gripper_open:
            # Try to grab object
            tip = self.get_positions()
            tip_x, tip_y = tip[0][-1], tip[1][-1]
            if np.hypot(tip_x - self.object_pos[0], tip_y - self.object_pos[1]) < 1.0:
                self.holding_object = True
        else:
            # Drop object at current tip
            if self.holding_object:
                tip = self.get_positions()
                self.object_pos = [tip[0][-1], tip[1][-1]]
                self.holding_object = False
        self.gripper_open = not self.gripper_open

    def get_positions(self):
        x, y = [0], [0]
        angle_sum = 0
        for i, length in enumerate(self.lengths):
            angle_sum += self.angles[i]
            x.append(x[-1] + length * np.cos(angle_sum))
            y.append(y[-1] + length * np.sin(angle_sum))
        return x, y

    def draw(self):
        x, y = self.get_positions()
        plt.clf()
        plt.plot(x, y, '-o', linewidth=4, markersize=10)
        # Draw object
        if self.holding_object:
            obj_x, obj_y = x[-1], y[-1]
        else:
            obj_x, obj_y = self.object_pos
        plt.scatter(obj_x, obj_y, s=200, c='red', marker='s', label="Object")
        plt.xlim(-sum(self.lengths), sum(self.lengths))
        plt.ylim(-sum(self.lengths), sum(self.lengths))
        plt.title(f"Robotic Arm (Gripper {'Open' if self.gripper_open else 'Closed'})")
        plt.legend()
        plt.grid(True)

# Create arm
arm = RoboticArm()

# Keyboard controls
def on_key(event):
    if event.key == 'up':
        arm.adjust_angle(0, 5)  # shoulder up
    elif event.key == 'down':
        arm.adjust_angle(0, -5) # shoulder down
    elif event.key == 'left':
        arm.adjust_angle(1, 5)  # elbow left
    elif event.key == 'right':
        arm.adjust_angle(1, -5) # elbow right
    elif event.key == 'w':
        arm.adjust_angle(2, 5)  # wrist up
    elif event.key == 's':
        arm.adjust_angle(2, -5) # wrist down
    elif event.key == 'space':
        arm.toggle_gripper()
    arm.draw()
    plt.draw()

# Setup plot
fig = plt.figure(figsize=(6,6))
cid = fig.canvas.mpl_connect('key_press_event', on_key)
arm.draw()
plt.show()
