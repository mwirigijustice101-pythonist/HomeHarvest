import whatsapp_clone as tk
from whatsapp_clone import messagebox

class ChaseUpApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ChaseUp - Paycheck Request")

        # Employer Name Label and Entry
        self.employer_label = tk.Label(root, text="Enter your employer's name:")
        self.employer_label.pack(pady=10)
        self.employer_entry = tk.Entry(root, width=30)
        self.employer_entry.pack(pady=5)

        # Amount Due Label and Entry
        self.amount_label = tk.Label(root, text="Enter amount due:")
        self.amount_label.pack(pady=10)
        self.amount_entry = tk.Entry(root, width=30)
        self.amount_entry.pack(pady=5)

        # Button to generate message
        self.generate_button = tk.Button(root, text="Generate Request", command=self.generate_message)
        self.generate_button.pack(pady=20)

        # Message Text Area
        self.message_text = tk.Text(root, width=50, height=10, wrap=tk.WORD)
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

if __name__ == "__main__":
    root = tk.Tk()
    app = ChaseUpApp(root)
    root.mainloop()

