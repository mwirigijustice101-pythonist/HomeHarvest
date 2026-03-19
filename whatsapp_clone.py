import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import time
import random
import os
import threading
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import colorchooser
import socket
import json
import uuid


class WhatsAppClone:
    def __init__(self, root):
        self.root = root
        self.root.title("WhatsApp Clone")
        self.root.geometry("400x600")

        # Define colors
        self.bg_color = "#f0f0f0"  # Light gray background
        self.chat_bg = "#ffffff"  # White chat background
        self.sent_bg = "#d3e9ff"  # Light blue for sent messages
        self.received_bg = "#f0f0f0"  # Light gray for received messages
        self.text_color = "#333333"  # Dark gray text
        self.sent_text = "#000000"  # Black text for sent messages
        self.received_text = "#000000"  # Black text for received messages
        self.entry_bg = "#ffffff"  # White entry background
        self.entry_text = "#000000"  # Black entry text
        self.button_bg = "#25d366"  # WhatsApp green
        self.button_text = "#ffffff"  # White button text
        self.contact_bg = "#f0f0f0"  # Light gray for contacts
        self.contact_text = "#000000"  # Black text for contacts
        self.timestamp_color = "#888888"  # Gray timestamps
        self.status_color = "#000000"  # Black status text
        self.status_bg = "#ffffff"  # White status background
        self.dark_mode = False

        # Set background color
        self.root.configure(bg=self.bg_color)

        # Load WhatsApp logo
        try:
            logo = Image.open("whatsapp_logo.png")  # Make sure you have a logo file
            logo = logo.resize((50, 50), Image.LANCZOS)
            self.logo_image = ImageTk.PhotoImage(logo)
            self.logo_label = tk.Label(self.root, image=self.logo_image, bg=self.bg_color)
            self.logo_label.pack(pady=10)
        except:
            # If logo not found, create a simple label
            self.logo_label = tk.Label(self.root, text="WhatsApp Clone", font=("Arial", 16, "bold"), bg=self.bg_color)
            self.logo_label.pack(pady=10)

        # Status frame
        self.status_frame = tk.Frame(self.root, bg=self.bg_color)
        self.status_frame.pack(pady=5, padx=10, fill=tk.X)

        # Status label
        self.status_label = tk.Label(self.status_frame, text="Status", font=("Arial", 12, "bold"), bg=self.status_bg,
                                     fg=self.status_color)
        self.status_label.pack(pady=5)

        # Status button
        self.status_button = tk.Button(self.status_frame, text="Update Status", command=self.update_status,
                                       bg=self.button_bg, fg=self.button_text, font=("Arial", 10, "bold"))
        self.status_button.pack(pady=5)

        # Dark mode toggle button
        self.dark_mode_button = tk.Button(self.status_frame, text="Dark Mode", command=self.toggle_dark_mode,
                                          bg=self.button_bg, fg=self.button_text, font=("Arial", 10, "bold"))
        self.dark_mode_button.pack(pady=5)

        # Contact list frame
        self.contact_frame = tk.Frame(self.root, bg=self.bg_color)
        self.contact_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Contact list
        self.contact_list = tk.Listbox(self.contact_frame, bg=self.contact_bg, fg=self.contact_text, font=("Arial", 12))
        self.contact_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar for contact list
        self.scrollbar = tk.Scrollbar(self.contact_frame, orient="vertical")
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.contact_list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.contact_list.yview)

        # Add contacts
        self.contacts = ["Friend 1", "Friend 2", "Friend 3", "Friend 4"]
        for contact in self.contacts:
            self.contact_list.insert(tk.END, contact)

        # Bind click event to contact list
        self.contact_list.bind("<<ListboxSelect>>", self.on_contact_select)

        # Chat area
        self.chat_area = tk.Text(self.root, wrap=tk.WORD, state='disabled', bg=self.chat_bg, fg=self.text_color)
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Message input
        self.message_entry = tk.Entry(self.root, bg=self.entry_bg, fg=self.entry_text, font=("Arial", 12))
        self.message_entry.pack(padx=10, pady=5, fill=tk.X)

        # Send button
        self.send_button = tk.Button(self.root, text="Send", command=self.send_message, bg=self.button_bg,
                                     fg=self.button_text, font=("Arial", 12, "bold"))
        self.send_button.pack(pady=5)

        # File upload button
        self.file_button = tk.Button(self.root, text="Send File", command=self.send_file, bg=self.button_bg,
                                     fg=self.button_text, font=("Arial", 10, "bold"))
        self.file_button.pack(pady=5)

        # Image upload button
        self.image_button = tk.Button(self.root, text="Send Image", command=self.send_image, bg=self.button_bg,
                                      fg=self.button_text, font=("Arial", 10, "bold"))
        self.image_button.pack(pady=5)

        # Audio message button
        self.audio_button = tk.Button(self.root, text="Send Audio", command=self.send_audio, bg=self.button_bg,
                                      fg=self.button_text, font=("Arial", 10, "bold"))
        self.audio_button.pack(pady=5)

        # Video call button
        self.video_button = tk.Button(self.root, text="Video Call", command=self.start_video_call, bg=self.button_bg,
                                      fg=self.button_text, font=("Arial", 10, "bold"))
        self.video_button.pack(pady=5)

        # Group chat button
        self.group_button = tk.Button(self.root, text="Create Group", command=self.create_group, bg=self.button_bg,
                                      fg=self.button_text, font=("Arial", 10, "bold"))
        self.group_button.pack(pady=5)

        # Profile picture button
        self.profile_button = tk.Button(self.root, text="Change Profile", command=self.change_profile,
                                        bg=self.button_bg, fg=self.button_text, font=("Arial", 10, "bold"))
        self.profile_button.pack(pady=5)

        # Message reactions button
        self.reactions_button = tk.Button(self.root, text="Add Reactions", command=self.add_reactions,
                                          bg=self.button_bg, fg=self.button_text, font=("Arial", 10, "bold"))
        self.reactions_button.pack(pady=5)

        # Initialize chat
        self.initialize_chat()

        # Start a simple server for demonstration purposes
        self.start_server()

    def start_server(self):
        # This is a simplified server for demonstration purposes
        # In a real application, you would need a proper server
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('localhost', 8080))
        self.server_socket.listen(5)

        # Start a thread to handle incoming connections
        threading.Thread(target=self.handle_connections, daemon=True).start()

    def handle_connections(self):
        while True:
            try:
                client_socket, client_address = self.server_socket.accept()
                # In a real application, you would handle the connection
                # For now, we'll just close the connection
                client_socket.close()
            except:
                break

    def initialize_chat(self):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, "Welcome to WhatsApp Clone!\n")
        self.chat_area.config(state='disabled')

    def on_contact_select(self, event):
        # Get selected contact
        selected = self.contact_list.curselection()
        if selected:
            contact = self.contact_list.get(selected)
            # Clear chat area
            self.chat_area.config(state='normal')
            self.chat_area.delete(1.0, tk.END)
            self.chat_area.config(state='disabled')
            # Update title
            self.root.title(f"WhatsApp Clone - {contact}")
            # Update status
            self.status_label.config(text=f"Status: {contact}")

    def send_message(self):
        message = self.message_entry.get()
        if message:
            # Get current contact
            selected = self.contact_list.curselection()
            contact = "Friend" if not selected else self.contact_list.get(selected)

            # Add timestamp
            timestamp = time.strftime("%H:%M")

            # Add message to chat
            self.chat_area.config(state='normal')
            self.chat_area.insert(tk.END, f"{timestamp} You: {message}\n", ("sent",))
            self.chat_area.tag_configure("sent", background=self.sent_bg, foreground=self.sent_text, font=("Arial", 12))
            self.chat_area.tag_configure("timestamp", foreground=self.timestamp_color, font=("Arial", 10))
            self.chat_area.tag_configure("text", font=("Arial", 12))
            self.chat_area.tag_configure("contact", font=("Arial", 12, "bold"))
            self.chat_area.tag_configure("message", font=("Arial", 12))
            self.chat_area.tag_configure("received", background=self.received_bg, foreground=self.received_text,
                                         font=("Arial", 12))

            self.chat_area.config(state='disabled')
            self.message_entry.delete(0, tk.END)

            # Simulate reply after random time
            delay = random.randint(1000, 3000)  # 1-3 seconds
            self.root.after(delay, self.simulate_reply)

    def simulate_reply(self):
        # Get current contact
        selected = self.contact_list.curselection()
        contact = "Friend" if not selected else self.contact_list.get(selected)

        # Generate random reply
        replies = ["Hello!", "How are you?", "That's great!", "I'm good, thanks!", "What's up?"]
        reply = random.choice(replies)

        # Add timestamp
        timestamp = time.strftime("%H:%M")

        # Add message to chat
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"{timestamp} {contact}: {reply}\n", ("received",))
        self.chat_area.tag_configure("received", background=self.received_bg, foreground=self.received_text,
                                     font=("Arial", 12))
        self.chat_area.config(state='disabled')

    def send_file(self):
        # Open file dialog
        file_path = filedialog.askopenfilename()
        if file_path:
            # Get current contact
            selected = self.contact_list.curselection()
            contact = "Friend" if not selected else self.contact_list.get(selected)

            # Add timestamp
            timestamp = time.strftime("%H:%M")

            # Add file message to chat
            self.chat_area.config(state='normal')
            self.chat_area.insert(tk.END, f"{timestamp} You: Sent file {os.path.basename(file_path)}\n", ("sent",))
            self.chat_area.tag_configure("sent", background=self.sent_bg, foreground=self.sent_text, font=("Arial", 12))
            self.chat_area.tag_configure("timestamp", foreground=self.timestamp_color, font=("Arial", 10))
            self.chat_area.tag_configure("text", font=("Arial", 12))
            self.chat_area.tag_configure("contact", font=("Arial", 12, "bold"))
            self.chat_area.tag_configure("message", font=("Arial", 12))
            self.chat_area.tag_configure("received", background=self.received_bg, foreground=self.received_text,
                                         font=("Arial", 12))

            self.chat_area.config(state='disabled')

            # Simulate reply after random time
            delay = random.randint(1000, 3000)  # 1-3 seconds
            self.root.after(delay, self.simulate_file_reply, contact, os.path.basename(file_path))

    def simulate_file_reply(self, contact, filename):
        # Add timestamp
        timestamp = time.strftime("%H:%M")

        # Add file message to chat
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"{timestamp} {contact}: File received\n", ("received",))
        self.chat_area.tag_configure("received", background=self.received_bg, foreground=self.received_text,
                                     font=("Arial", 12))
        self.chat_area.config(state='disabled')

    def send_image(self):
        # Open file dialog
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")])
        if file_path:
            # Get current contact
            selected = self.contact_list.curselection()
            contact = "Friend" if not selected else self.contact_list.get(selected)

            # Add timestamp
            timestamp = time.strftime("%H:%M")

            # Add image message to chat
            self.chat_area.config(state='normal')
            self.chat_area.insert(tk.END, f"{timestamp} You: Sent image {os.path.basename(file_path)}\n", ("sent",))
            self.chat_area.tag_configure("sent", background=self.sent_bg, foreground=self.sent_text, font=("Arial", 12))
            self.chat_area.tag_configure("timestamp", foreground=self.timestamp_color, font=("Arial", 10))
            self.chat_area.tag_configure("text", font=("Arial", 12))
            self.chat_area.tag_configure("contact", font=("Arial", 12, "bold"))
            self.chat_area.tag_configure("message", font=("Arial", 12))
            self.chat_area.tag_configure("received", background=self.received_bg, foreground=self.received_text,
                                         font=("Arial", 12))

            self.chat_area.config(state='disabled')

            # Simulate reply after random time
            delay = random.randint(1000, 3000)  # 1-3 seconds
            self.root.after(delay, self.simulate_image_reply, contact, os.path.basename(file_path))

    def simulate_image_reply(self, contact, filename):
        # Add timestamp
        timestamp = time.strftime("%H:%M")

        # Add image message to chat
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"{timestamp} {contact}: Image received\n", ("received",))
        self.chat_area.tag_configure("received", background=self.received_bg, foreground=self.received_text,
                                     font=("Arial", 12))
        self.chat_area.config(state='disabled')

    def send_audio(self):
        # Simulate audio message
        # In a real application, this would record audio
        selected = self.contact_list.curselection()
        contact = "Friend" if not selected else self.contact_list.get(selected)

        # Add timestamp
        timestamp = time.strftime("%H:%M")

        # Add audio message to chat
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"{timestamp} You: Sent audio message\n", ("sent",))
        self.chat_area.tag_configure("sent", background=self.sent_bg, foreground=self.sent_text, font=("Arial", 12))
        self.chat_area.tag_configure("timestamp", foreground=self.timestamp_color, font=("Arial", 10))
        self.chat_area.tag_configure("text", font=("Arial", 12))
        self.chat_area.tag_configure("contact", font=("Arial", 12, "bold"))
        self.chat_area.tag_configure("message", font=("Arial", 12))
        self.chat_area.tag_configure("received", background=self.received_bg, foreground=self.received_text,
                                     font=("Arial", 12))

        self.chat_area.config(state='disabled')

        # Simulate reply after random time
        delay = random.randint(1000, 3000)  # 1-3 seconds
        self.root.after(delay, self.simulate_audio_reply, contact)

    def simulate_audio_reply(self, contact):
        # Add timestamp
        timestamp = time.strftime("%H:%M")

        # Add audio message to chat
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"{timestamp} {contact}: Audio message received\n", ("received",))
        self.chat_area.tag_configure("received", background=self.received_bg, foreground=self.received_text,
                                     font=("Arial", 12))
        self.chat_area.config(state='disabled')

    def start_video_call(self):
        # Simulate video call
        # In a real application, this would initiate a video call
        selected = self.contact_list.curselection()
        contact = "Friend" if not selected else self.contact_list.get(selected)

        # Add timestamp
        timestamp = time.strftime("%H:%M")

        # Add video call message to chat
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"{timestamp} You: Started video call with {contact}\n", ("sent",))
        self.chat_area.tag_configure("sent", background=self.sent_bg, foreground=self.sent_text, font=("Arial", 12))
        self.chat_area.tag_configure("timestamp", foreground=self.timestamp_color, font=("Arial", 10))
        self.chat_area.tag_configure("text", font=("Arial", 12))
        self.chat_area.tag_configure("contact", font=("Arial", 12, "bold"))
        self.chat_area.tag_configure("message", font=("Arial", 12))
        self.chat_area.tag_configure("received", background=self.received_bg, foreground=self.received_text,
                                     font=("Arial", 12))

        self.chat_area.config(state='disabled')

        # Simulate reply after random time
        delay = random.randint(1000, 3000)  # 1-3 seconds
        self.root.after(delay, self.simulate_video_reply, contact)

    def simulate_video_reply(self, contact):
        # Add timestamp
        timestamp = time.strftime("%H:%M")

        # Add video call message to chat
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"{timestamp} {contact}: Video call accepted\n", ("received",))
        self.chat_area.tag_configure("received", background=self.received_bg, foreground=self.received_text,
                                     font=("Arial", 12))
        self.chat_area.config(state='disabled')

    def create_group(self):
        # Simulate creating a group
        group_name = simpledialog.askstring("Create Group", "Enter group name:")
        if group_name:
            # Add timestamp
            timestamp = time.strftime("%H:%M")

            # Add group creation message to chat
            self.chat_area.config(state='normal')
            self.chat_area.insert(tk.END, f"{timestamp} You: Created group {group_name}\n", ("sent",))
            self.chat_area.tag_configure("sent", background=self.sent_bg, foreground=self.sent_text, font=("Arial", 12))
            self.chat_area.tag_configure("timestamp", foreground=self.timestamp_color, font=("Arial", 10))
            self.chat_area.tag_configure("text", font=("Arial", 12))
            self.chat_area.tag_configure("contact", font=("Arial", 12, "bold"))
            self.chat_area.tag_configure("message", font=("Arial", 12))
            self.chat_area.tag_configure("received", background=self.received_bg, foreground=self.received_text,
                                         font=("Arial", 12))

            self.chat_area.config(state='disabled')

            # Simulate reply after random time
            delay = random.randint(1000, 3000)  # 1-3 seconds
            self.root.after(delay, self.simulate_group_reply, group_name)

    def simulate_group_reply(self, group_name):
        # Add timestamp
        timestamp = time.strftime("%H:%M")

        # Add group message to chat
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"{timestamp} Group {group_name}: Welcome to the group!\n", ("received",))
        self.chat_area.tag_configure("received", background=self.received_bg, foreground=self.received_text,
                                     font=("Arial", 12))
        self.chat_area.config(state='disabled')

    def change_profile(self):
        # Open color dialog to change profile color
        color = colorchooser.askcolor(title="Choose profile color")
        if color:
            # Update profile color
            self.status_label.config(fg=color)
            self.status_button.config(bg=color)
            self.dark_mode_button.config(bg=color)
            self.send_button.config(bg=color)
            self.file_button.config(bg=color)
            self.image_button.config(bg=color)
            self.audio_button.config(bg=color)
            self.video_button.config(bg=color)
            self.group_button.config(bg=color)
            self.reactions_button.config(bg=color)
            self.profile_button.config(bg=color)

    def add_reactions(self):
        # Add reactions to the last message
        self.chat_area.config(state='normal')
        # Get the last message
        self.chat_area.tag_configure("last", background=self.sent_bg, foreground=self.sent_text, font=("Arial", 12))
        self.chat_area.tag_configure("reaction", font=("Arial", 12))
        self.chat_area.tag_configure("emoji", font=("Arial", 12))

        # Add reactions
        self.chat_area.insert(tk.END, "👍", ("reaction",))
        self.chat_area.tag_configure("reaction", background=self.sent_bg, foreground=self.sent_text, font=("Arial", 12))
        self.chat_area.tag_configure("emoji", font=("Arial", 12))

        self.chat_area.config(state='disabled')

    def update_status(self):
        # Open dialog to update status
        status = simpledialog.askstring("Update Status", "Enter your status:")
        if status:
            self.status_label.config(text=f"Status: {status}")

    def toggle_dark_mode(self):
        if self.dark_mode:
            # Switch to light mode
            self.bg_color = "#f0f0f0"
            self.chat_bg = "#ffffff"
            self.sent_bg = "#d3e9ff"
            self.received_bg = "#f0f0f0"
            self.text_color = "#333333"
            self.sent_text = "#000000"
            self.received_text = "#000000"
            self.entry_bg = "#ffffff"
            self.entry_text = "#000000"
            self.button_bg = "#25d366"
            self.button_text = "#ffffff"
            self.contact_bg = "#f0f0f0"
            self.contact_text = "#000000"
            self.timestamp_color = "#888888"
            self.status_color = "#000000"
            self.status_bg = "#ffffff"
            self.dark_mode = False
        else:
            # Switch to dark mode
            self.bg_color = "#121212"
            self.chat_bg = "#1e1e1e"
            self.sent_bg = "#1a4d7c"
            self.received_bg = "#2a2a2a"
            self.text_color = "#ffffff"
            self.sent_text = "#ffffff"
            self.received_text = "#ffffff"
            self.entry_bg = "#2a2a2a"
            self.entry_text = "#ffffff"
            self.button_bg = "#008000"
            self.button_text = "#ffffff"
            self.contact_bg = "#2a2a2a"
            self.contact_text = "#ffffff"
            self.timestamp_color = "#cccccc"
            self.status_color = "#ffffff"
            self.status_bg = "#1e1e1e"
            self.dark_mode = True

        # Update all widgets
        self.root.configure(bg=self.bg_color)
        self.status_frame.configure(bg=self.bg_color)
        self.status_label.configure(bg=self.status_bg, fg=self.status_color)
        self.status_button.configure(bg=self.button_bg, fg=self.button_text)
        self.dark_mode_button.configure(bg=self.button_bg, fg=self.button_text)
        self.contact_list.configure(bg=self.contact_bg, fg=self.contact_text)
        self.chat_area.configure(bg=self.chat_bg, fg=self.text_color)
        self.message_entry.configure(bg=self.entry_bg, fg=self.entry_text)
        self.send_button.configure(bg=self.button_bg, fg=self.button_text)
        self.file_button.configure(bg=self.button_bg, fg=self.button_text)
        self.image_button.configure(bg=self.button_bg, fg=self.button_text)
        self.audio_button.configure(bg=self.button_bg, fg=self.button_text)
        self.video_button.configure(bg=self.button_bg, fg=self.button_text)
        self.group_button.configure(bg=self.button_bg, fg=self.button_text)
        self.reactions_button.configure(bg=self.button_bg, fg=self.button_text)
        self.profile_button.configure(bg=self.button_bg, fg=self.button_text)

        # Update the logo if it exists
        if hasattr(self, 'logo_image'):
            self.logo_label.configure(bg=self.bg_color)

    def update_status(self):
        # Open dialog to update status
        status = simpledialog.askstring("Update Status", "Enter your status:")
        if status:
            self.status_label.config(text=f"Status: {status}")


if __name__ == "__main__":
    root = tk.Tk()
    app = WhatsAppClone(root)
    root.mainloop()