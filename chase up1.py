import whatsapp_clone as tk
from whatsapp_clone import messagebox
import smtplib
from email.mime.text import MIMEText

class ChaseUpApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ChaseUp - Paycheck Request")
        self.root.geometry("400x600")
        self.root.configure(bg="#f0f0f0")

        # Create a phone frame look
        frame = tk.Frame(root, bg="#ffffff", bd=2, relief="raised")
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Employer Name Label and Entry
        self.employer_label = tk.Label(frame, text="Enter your employer's name:", bg="#ffffff")
        self.employer_label.pack(pady=10)
        self.employer_entry = tk.Entry(frame, width=30, bg="#e6e6e6")
        self.employer_entry.pack(pady=5)

        # Amount Due Label and Entry
        self.amount_label = tk.Label(frame, text="Enter amount due:", bg="#ffffff")
        self.amount_label.pack(pady=10)
        self.amount_entry = tk.Entry(frame, width=30, bg="#e6e6e6")
        self.amount_entry.pack(pady=5)

        # Button to generate message
        self.generate_button = tk.Button(frame, text="Generate Request", command=self.generate_message, bg="#4CAF50", fg="white")
        self.generate_button.pack(pady=20)

        # Button to send message
        self.send_button = tk.Button(frame, text="Send Message", command=self.send_email, bg="#2196F3", fg="white")
        self.send_button.pack(pady=5)

        # Message Text Area
        self.message_text = tk.Text(frame, width=50, height=10, wrap=tk.WORD, bg="#ffffff")
        self.message_text.pack(pady=10)

    def generate_message(self):
        employer_name = self.employer_entry.get().strip()
        amount_due = self.amount_entry.get().strip()

        if employer_name and amount_due:
            message = (
                f"Dear {employer_name},\n\n"
                f"I hope this message finds you well. I'm writing to kindly ask for the paycheck of {amount_due} "
                f"that is due. Your assistance in this matter is greatly appreciated.\n\nThank you!"
            )
            self.message_text.delete(1.0, tk.END)  # Clear previous text
            self.message_text.insert(tk.END, message)  # Insert the new message
        else:
            messagebox.showwarning("Input Error", "Please fill in both fields.")

    def send_email(self):
        recipient_email = "recipient@example.com"  # Replace with the actual recipient email address
        subject = "Paycheck Request"
        body = self.message_text.get(1.0, tk.END).strip()

        if body:
            # Set up the SMTP server
            sender_email = "your_email@example.com"  # Replace with your email
            sender_password = "your_password"  # Replace with your email password

            # Create the email message
            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = sender_email
            msg['To'] = recipient_email

            try:
                with smtplib.SMTP('smtp.gmail.com', 587) as server:
                    server.starttls()
                    server.login(sender_email, sender_password)
                    server.send_message(msg)
                    messagebox.showinfo("Success", "Email sent successfully!")
            except Exception as e:
                messagebox.showerror("Send Error", f"Failed to send email.\nError: {str(e)}")
        else:
            messagebox.showwarning("Input Error", "Please generate a message before sending.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChaseUpApp(root)
    root.mainloop()
