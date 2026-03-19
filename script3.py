import whatsapp_clone as tk
from whatsapp_clone import ttk, messagebox, scrolledtext
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import json
import os


class ChaseUpApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ChaseUpp - Freelancer Payment Manager")
        self.root.geometry("1200x800")
        self.root.configure(bg="#1a1a2e")

        # Data storage
        self.data_file = "chaseup_data.json"
        self.load_data()

        # Color scheme
        self.colors = {
            'bg_dark': '#1a1a2e',
            'bg_medium': '#16213e',
            'accent': '#0f3460',
            'gold': '#e94560',
            'text': '#ffffff',
            'button': '#e94560',
            'button_hover': '#ff6b81',
            'success': '#00d9ff',
            'frame_bg': '#16213e'
        }

        self.create_widgets()

    def load_data(self):
        """Load saved data from JSON file"""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = {
                'freelancers': [],
                'payments': [],
                'email_config': {}
            }

    def save_data(self):
        """Save data to JSON file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=4)

    def create_widgets(self):
        """Create all UI widgets"""
        # Header with gradient effect
        header_frame = tk.Frame(self.root, bg=self.colors['gold'], height=100)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        header_frame.pack_propagate(False)

        header_label = tk.Label(
            header_frame,
            text="💰 ChaseUpp - Get Paid Faster! 💸",
            font=("Helvetica", 32, "bold"),
            bg=self.colors['gold'],
            fg=self.colors['text']
        )
        header_label.pack(expand=True)

        # Main container
        main_container = tk.Frame(self.root, bg=self.colors['bg_dark'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Left panel - Form
        left_panel = tk.Frame(main_container, bg=self.colors['frame_bg'], relief=tk.RAISED, bd=3)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        self.create_form(left_panel)

        # Right panel - List and actions
        right_panel = tk.Frame(main_container, bg=self.colors['frame_bg'], relief=tk.RAISED, bd=3)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.create_list_panel(right_panel)

    def create_form(self, parent):
        """Create the input form"""
        form_title = tk.Label(
            parent,
            text="📝 New Payment Request",
            font=("Helvetica", 20, "bold"),
            bg=self.colors['frame_bg'],
            fg=self.colors['success']
        )
        form_title.pack(pady=20)

        # Form fields
        fields = [
            ("Freelancer Name:", "name"),
            ("Client Name:", "client"),
            ("Client Email:", "email"),
            ("Amount:", "amount"),
            ("Project Description:", "project")
        ]

        self.entries = {}

        for label_text, key in fields:
            frame = tk.Frame(parent, bg=self.colors['frame_bg'])
            frame.pack(pady=10, padx=30, fill=tk.X)

            label = tk.Label(
                frame,
                text=label_text,
                font=("Helvetica", 12, "bold"),
                bg=self.colors['frame_bg'],
                fg=self.colors['text'],
                anchor='w'
            )
            label.pack(anchor='w')

            entry = tk.Entry(
                frame,
                font=("Helvetica", 12),
                bg=self.colors['bg_medium'],
                fg=self.colors['text'],
                insertbackground=self.colors['text'],
                relief=tk.FLAT,
                bd=5
            )
            entry.pack(fill=tk.X, pady=5)
            self.entries[key] = entry

        # Currency dropdown
        currency_frame = tk.Frame(parent, bg=self.colors['frame_bg'])
        currency_frame.pack(pady=10, padx=30, fill=tk.X)

        currency_label = tk.Label(
            currency_frame,
            text="Currency:",
            font=("Helvetica", 12, "bold"),
            bg=self.colors['frame_bg'],
            fg=self.colors['text'],
            anchor='w'
        )
        currency_label.pack(anchor='w')

        self.currency_var = tk.StringVar(value="USD")
        currencies = ["USD 💵", "EUR 💶", "GBP 💷", "JPY 💴", "CAD 🍁", "AUD 🦘", "INR ₹", "NGN ₦"]

        currency_menu = ttk.Combobox(
            currency_frame,
            textvariable=self.currency_var,
            values=currencies,
            font=("Helvetica", 12),
            state="readonly"
        )
        currency_menu.pack(fill=tk.X, pady=5)

        # Payment method
        payment_frame = tk.Frame(parent, bg=self.colors['frame_bg'])
        payment_frame.pack(pady=10, padx=30, fill=tk.X)

        payment_label = tk.Label(
            payment_frame,
            text="Payment Method:",
            font=("Helvetica", 12, "bold"),
            bg=self.colors['frame_bg'],
            fg=self.colors['text'],
            anchor='w'
        )
        payment_label.pack(anchor='w')

        self.payment_var = tk.StringVar(value="Bank Transfer")
        payment_methods = ["Bank Transfer 🏦", "PayPal 💳", "Stripe 💰", "Wise 🌍", "Crypto ₿", "Cash 💵"]

        payment_menu = ttk.Combobox(
            payment_frame,
            textvariable=self.payment_var,
            values=payment_methods,
            font=("Helvetica", 12),
            state="readonly"
        )
        payment_menu.pack(fill=tk.X, pady=5)

        # Buttons
        button_frame = tk.Frame(parent, bg=self.colors['frame_bg'])
        button_frame.pack(pady=30)

        send_button = tk.Button(
            button_frame,
            text="📧 Send Payment Request",
            font=("Helvetica", 14, "bold"),
            bg=self.colors['button'],
            fg=self.colors['text'],
            activebackground=self.colors['button_hover'],
            activeforeground=self.colors['text'],
            relief=tk.FLAT,
            bd=0,
            padx=30,
            pady=15,
            cursor="hand2",
            command=self.send_payment_request
        )
        send_button.pack(side=tk.LEFT, padx=10)

        clear_button = tk.Button(
            button_frame,
            text="🔄 Clear Form",
            font=("Helvetica", 14, "bold"),
            bg=self.colors['accent'],
            fg=self.colors['text'],
            activebackground=self.colors['bg_medium'],
            activeforeground=self.colors['text'],
            relief=tk.FLAT,
            bd=0,
            padx=30,
            pady=15,
            cursor="hand2",
            command=self.clear_form
        )
        clear_button.pack(side=tk.LEFT, padx=10)

    def create_list_panel(self, parent):
        """Create the payment requests list panel"""
        list_title = tk.Label(
            parent,
            text="📋 Payment Requests",
            font=("Helvetica", 20, "bold"),
            bg=self.colors['frame_bg'],
            fg=self.colors['success']
        )
        list_title.pack(pady=20)

        # Scrolled text for displaying requests
        self.request_list = scrolledtext.ScrolledText(
            parent,
            font=("Courier", 10),
            bg=self.colors['bg_medium'],
            fg=self.colors['text'],
            relief=tk.FLAT,
            bd=5,
            wrap=tk.WORD
        )
        self.request_list.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        # Action buttons
        action_frame = tk.Frame(parent, bg=self.colors['frame_bg'])
        action_frame.pack(pady=20)

        refresh_button = tk.Button(
            action_frame,
            text="🔄 Refresh List",
            font=("Helvetica", 12, "bold"),
            bg=self.colors['success'],
            fg=self.colors['bg_dark'],
            activebackground=self.colors['button_hover'],
            relief=tk.FLAT,
            bd=0,
            padx=20,
            pady=10,
            cursor="hand2",
            command=self.refresh_list
        )
        refresh_button.pack(side=tk.LEFT, padx=5)

        mark_paid_button = tk.Button(
            action_frame,
            text="✅ Mark as Paid",
            font=("Helvetica", 12, "bold"),
            bg="#2ecc71",
            fg=self.colors['text'],
            activebackground="#27ae60",
            relief=tk.FLAT,
            bd=0,
            padx=20,
            pady=10,
            cursor="hand2",
            command=self.mark_as_paid
        )
        mark_paid_button.pack(side=tk.LEFT, padx=5)

        config_button = tk.Button(
            action_frame,
            text="⚙️ Email Config",
            font=("Helvetica", 12, "bold"),
            bg=self.colors['accent'],
            fg=self.colors['text'],
            activebackground=self.colors['bg_medium'],
            relief=tk.FLAT,
            bd=0,
            padx=20,
            pady=10,
            cursor="hand2",
            command=self.open_email_config
        )
        config_button.pack(side=tk.LEFT, padx=5)

        self.refresh_list()

    def send_payment_request(self):
        """Send payment request email"""
        # Validate inputs
        name = self.entries['name'].get().strip()
        client = self.entries['client'].get().strip()
        email = self.entries['email'].get().strip()
        amount = self.entries['amount'].get().strip()
        project = self.entries['project'].get().strip()
        currency = self.currency_var.get().split()
        payment_method = self.payment_var.get().split()

        if not all([name, client, email, amount, project]):
            messagebox.showerror("Error", "Please fill in all fields!")
            return

        # Create payment request record
        request = {
            'id': len(self.data['payments']) + 1,
            'freelancer': name,
            'client': client,
            'email': email,
            'amount': amount,
            'currency': currency,
            'payment_method': payment_method,
            'project': project,
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'status': 'Pending'
        }

        # Send email
        if self.send_email(request):
            self.data['payments'].append(request)
            self.save_data()
            messagebox.showinfo("Success", f"Payment request sent to {client}! 🎉")
            self.clear_form()
            self.refresh_list()
        else:
            messagebox.showwarning("Warning", "Request saved but email not sent. Please configure email settings.")
            self.data['payments'].append(request)
            self.save_data()
            self.refresh_list()

    def send_email(self, request):
        """Send email using SMTP"""
        if not self.data.get('email_config'):
            return False

        try:
            config = self.data['email_config']

            # Create message
            msg = MIMEMultipart()
            msg['From'] = config['email']
            msg['To'] = request['email']
            msg['Subject'] = f"Payment Request - {request['project']}"

            # Email body
            body = f"""
Dear {request['client']},

I hope this email finds you well!

This is a friendly reminder regarding the payment for the project: {request['project']}

Payment Details:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💰 Amount: {request['currency']} {request['amount']}
👤 Freelancer: {request['freelancer']}
📅 Date: {request['date']}
💳 Preferred Payment Method: {request['payment_method']}

I would greatly appreciate it if you could process this payment at your earliest convenience.

If you have any questions or concerns, please don't hesitate to reach out.

Thank you for your continued partnership!

Best regards,
{request['freelancer']}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sent via ChaseUpp - Freelancer Payment Manager
            """

            msg.attach(MIMEText(body, 'plain'))

            # Send email
            server = smtplib.SMTP(config['smtp_server'], int(config['smtp_port']))
            server.starttls()
            server.login(config['email'], config['password'])
            server.send_message(msg)
            server.quit()

            return True
        except Exception as e:
            print(f"Email error: {e}")
            return False

    def clear_form(self):
        """Clear all form fields"""
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.currency_var.set("USD")
        self.payment_var.set("Bank Transfer")

    def refresh_list(self):
        """Refresh the payment requests list"""
        self.request_list.delete(1.0, tk.END)

        if not self.data['payments']:
            self.request_list.insert(tk.END, "No payment requests yet. Create your first one! 🚀\n")
            return

        for payment in self.data['payments']:
            status_emoji = "✅" if payment['status'] == 'Paid' else "⏳"
            #text = f"""
 # status_emoji} Request #{payment['id']} - {payment['status']}
#━ # ━━━━ # ━━━━━━━━
