# Import Required Libraries
from tkinter import *
import datetime
import time
from playsound import playsound
from threading import Thread

# Create Tkinter Window
root = Tk()
root.title("Alarm Clock")
root.geometry("400x200")


# Function to Run Alarm in a Separate Thread
def Threading():
    t1 = Thread(target=alarm)
    t1.daemon = True  # Allows thread to exit when main program closes
    t1.start()


# Alarm Function
def alarm():
    set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

    while True:
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Current Time: {current_time} | Alarm Set For: {set_alarm_time}")

        if current_time == set_alarm_time:
            print("⏰ Time to Wake Up! ⏰")
            try:
                playsound("sound.mp3")  # Make sure you have a sound file
            except Exception as e:
                print(f"Error playing sound: {e}")
            break  # Exit loop after alarm goes off


# GUI Components
Label(root, text="Alarm Clock", font=("Helvetica", 20, "bold"), fg="red").pack(pady=10)
Label(root, text="Set Time", font=("Helvetica", 15, "bold")).pack()

frame = Frame(root)
frame.pack()

# Hour Dropdown
hour = StringVar(root)
hours = [f"{i:02}" for i in range(24)]  # 00 - 23
hour.set(hours[0])
OptionMenu(frame, hour, *hours).pack(side=LEFT)

# Minute Dropdown
minute = StringVar(root)
minutes = [f"{i:02}" for i in range(60)]  # 00 - 59
minute.set(minutes[0])
OptionMenu(frame, minute, *minutes).pack(side=LEFT)

# Second Dropdown
second = StringVar(root)
seconds = [f"{i:02}" for i in range(60)]  # 00 - 59
second.set(seconds[0])
OptionMenu(frame, second, *seconds).pack(side=LEFT)

# Set Alarm Button
Button(root, text="Set Alarm", font=("Helvetica", 15), command=Threading).pack(pady=20)

# Run Tkinter Main Loop
root.mainloop()
