import whatsapp_clone as tk
from threading import Thread
import queue

class Signal:
    def __init__(self):
        self.callbacks = []

    def connect(self, func):
        self.callbacks.append(func)

    def emit(self, *args, **kwargs):
        for callback in self.callbacks:
            callback(*args, **kwargs)

# Example usage
def update_label(text):
    label.config(text=text)

signal = Signal()
signal.connect(update_label)

def background_task():
    # Simulate work
    result = "Data processed"
    # Safely update GUI from background thread
    root.after(0, lambda: signal.emit(result))

root = tk.tk()
label = tk.Label(root, text="Ready")
label.pack()

button = tk.Button(root, text="Run Task", command=lambda: Thread(target=background_task).start())
button.pack()

root.mainloop()