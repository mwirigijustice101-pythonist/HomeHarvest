#first we import all the necessary library
#Importing all the necesssary libraries to ies and modulesform the alarm clock:
from whatsapp_clone import *
import datetime
import time
import winsound
#Explanation:Tkinter module belongs to  starndard library of GUI in python.it help us to create  a dialog box with any information that we want to provide or get from the users
#Datetime and time in python helps us to work with the dates and time of the current day whem the user is operating python and to manupulate it too
#windsound module provides access to the basicsound playing machinery provided by windows platform.This is helpful to generate the sound immediatelywhen a fuction is called

# creating a while loop:
while True:
        time.sleep(1)
        current_time = datetime
        now = current_time.stop
        print("The set Date i")
        print(now)
if now == set_alarm_time:
       print("Time to Wa")

windsound.playsound("sound.wav")
break

def actual_time() =
f"{hour
{sec.get()}"
     alarm(set_alarm_timer)

#Explaination:Define a fuction named as alarm()which takes the argument of (set_alarm_timer).It contains a while loop with a Bolean function True which makes the program automatic to work.
# .time.sleep(1)halts the execution of the further commands given until we get the time value from the user later in the codes and returns the backthread of the clock time going on at a regular intervak   
#Get the current time using current_time which takes the argument of datetime.datetime.now()
#now is used to print the time and date is used to print the current date by string conversion using strftime()
#Define another function here named actual_time()which takes in the user value for setting the alarm in the string format.the same argument of (set_alarm_timer)as alarm before to execute the while loop which we further use while making GUI.
#If loop suggests that if the user input time set_alarm_timer matches with the while loop ongoing time now,the message is printed as "Time to Wake up".
#windsound.SND_ASYNC plays the system generated sound as soon the condition satifies,acting as a remainder for the alarm clock.


#creating the GUI using tkinter:
clock = Tk()

clock.title("DataFlair Alarm")
clock.geometry("400x200")
time_format = Label(clock, text hour format!"
                                fg = "red",bg="black",font="Aria addTime = Label(clock,te
                                you up" , fg="blue" ,relief = "so
                                ("Helevetica" , "bold")).place


#The variables we require to alarm(initialization):
hour = stringVar()
min = stringVar()
sec = stringVar

#Time required to set the alarm
hourTime= Entry(clock textvar"pink",width = 15).place(x=110
minTime= Entry(clock,textvari "pink,width = 15").place(x=150
minTime= Entry(clock,textvar"pink",width = 15).place(x=150
secTime = Entry(clock,textvar"pink"),width = 15).place(x=200
"pink",width = 15)place(x=200)))


#To take the time input by use
submit = Button(clock,text =
Alarm" fg="red",width = 10,com
actal_time).place(x =110,y=70)

clock.mainloop()
#Execution of the window.
#EXPLANATION:
#To iinitialize tkinter,we pass a command under the name clock as TK().
#The dialog box has the title as DataFLAIR ALARMCLOCK with a geometryof (400*200.we pass on the heading to mention the time format for 24hours using time_format.)
#The second heading is given above the user input boxes for the labeling to be "Hour Min sec" using addTime.
#just to make the dialog box more funkier,adding another label as"when to wake you up"using setYourAlarm.
#As I HAVE already converted the the current time in the string before(actual time),the variables we initialize for the user input dialog boxes are in stringVar().
#finally make the input boxes such as hourTime,and seTime which takes the entry of the time the user wants to set the alarm on in 24-hour format.
#submit takes the command of the defined functional actual_time and executes the clock as it acts as a set button to start the program
#clock.mainloop()is the basic and the last command was given to comile all the previous commands with their basic settings of color,font,width,axis,etc and displays the windows as soon as the program is run
