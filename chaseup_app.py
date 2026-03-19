import whatsapp_clone as tk
from whatsapp_clone import messagebox
import webbrowser
import urllib.request

class ChaseUpApp:
    def __init__(self,root):
        self.root = root
        self.root.title("ChaseUp-Paycheck Rquest")
        self.root.geometry("500x650")
        self.root.resizable(True,False)

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
MIMEMultipart
from PIL import Image,ImageDraw,

def create_rounded_frame_image(width,height,radius,color):
    inage = Image.new("RGB",(width,height),(0,0,0))
    draw = ImageDraw.Draw(inage)
    draw.rounded_rectangle([(0,0,),(width,height)], radius=radius,fill=color)
    return ImageTk.photoImage(inage)

#use of background
img = create_rounded_frame_image(100,100,50,"#f0f4f8")
label = tk.Label(main_frame_image=img, bg="#f0f4f8")
label.image = img #keep reference
label.pack(pady=(0,30))


class ChaseUpApp:
    def __init__(self,root):
        self.root = root
        self.root.title("ChaseUp-Paycheck Rquest")
        self.root.geometry("500x700")
        self.root.resizable(True,False)

        #Create main container with padding
        main_frame = tk.Frame(root,bg="#f0f4f8")
        main_fame.pack(expand=True,fill="both",padx=30,pady=30)

        # Header with Icon & Button
        from whatsapp_clone import Canvas,PhotoImage
        header_canvas = Canvas(main_frame,width=440,height=100,
                               bg="#f0f4f8",highlightthickness=0)
        header_canvas.pack(expand=True,fill="x",pady=(0,20))


        #Sleaker,flatter design with subtle shadow effect
        round_rectangle(header_canvas,0,0,440,100,radius=20,
                        fill="#0f172a",outline="")
        #Modern minimal title (left-aligned like most apps)
        header_canvas.create_text(24,50,text=ChaseUpApp,
                                  font=("Segoe UI",24,"bold"),
                                  fill="#ffffff",anchor="W")

        #Add notification badge or action button (top right)
        round_rectangle(header_canvas,380,30,420,70,radius=20,
                        fill="#3b82f6",outline="")
        header_canvas.craete_text(400,50,text="+",
                                  font=("Segoe UI",28),
                                  fill=("#ffffff")

#Employer Name
tk.Label(
    inner_form,
    text="Employer's Name",
    font=("Arial",11,"bold"),
    bg="#fffff",
    fg="##2c3e50",
    anchor="w"
).pack(fill="x",pady=(0,5))

self employer_entry = tk.Entry(
inner_form,
 font=("")





