from threading import Thread
from time import sleep
from tkinter import *
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
from datetime import datetime
from pygame import mixer 

portion  = Tk()
portion.title("ALARM CLOCK")
portion.geometry('400x400')
portion.configure( bg = '#{:02x}{:02x}{:02x}'.format(204, 16, 250))
border = Frame(portion, width=400, height=20, bg='#{:02x}{:02x}{:02x}'.format(224,224,224), highlightthickness=2, highlightbackground='#{:02x}{:02x}{:02x}'.format(255, 255, 255))
border.place(x=0, y=0)
border2 = Frame(portion, width=400, height=20, bg='#{:02x}{:02x}{:02x}'.format(224,224,224), highlightthickness=2, highlightbackground='#{:02x}{:02x}{:02x}'.format(255, 255, 255))
border2.place(x=0, y =380)
time_list = []
duration_list = []

snooze_duration = 60
icn_clock = Image.open('clock1.png')
icn_clock = icn_clock.resize((100,100))
icn_clock = ImageTk.PhotoImage((icn_clock))

icn_load = Label(portion, height = 100, image = icn_clock, bg ='#{:02x}{:02x}{:02x}'.format(204, 16, 250) )
icn_load.place(x= 10, y = 30)
def increase_counter_part():
    global counter
    counter += 1
    counter_entry.delete(0, END)
    counter_entry.insert(0, str("AM"))
 
def decrease_counter_part():
    global counter
    counter -= 1
    counter_entry.delete(0, END)
    counter_entry.insert(0, str("PM"))

  

def increase_counter_hour():
    global counter_hour
    counter_hour += 1
    
    if(counter_hour > 12):
      counter_hour = 1
      counter_entry_hour.delete(0, END)
      counter_entry_hour.insert(0, str(counter_hour))
    else: 
     counter_entry_hour.delete(0, END)
     counter_entry_hour.insert(0, str(counter_hour))
    if(counter_hour<10):
       counter_entry_hour.delete(0, END)
       counter_entry_hour.insert(0, "0" + str(counter_hour))

def decrease_counter_hour():
    global counter_hour
    counter_hour -= 1
    
    if(counter_hour <= 0):
      counter_hour = 12
      counter_entry_hour.delete(0, END)
      counter_entry_hour.insert(0, str(counter_hour))
    else:
     counter_entry_hour.delete(0, END)
     counter_entry_hour.insert(0, str(counter_hour))    
    if(counter_hour<10):
       counter_entry_hour.delete(0, END)
       counter_entry_hour.insert(0, "0" + str(counter_hour))

def increase_counter_min():
    global counter_min
    counter_min += 1
    
    if(counter_min >= 60):
       counter_min = 0
       counter_entry_min.delete(0, END)
       counter_entry_min.insert(0, str(counter_min))
    else:   
     counter_entry_min.delete(0, END)
     counter_entry_min.insert(0, str(counter_min))
    if(counter_min<10):
       counter_entry_min.delete(0, END)
       counter_entry_min.insert(0, "0" + str(counter_min))
def decrease_counter_min():
    global counter_min
    counter_min -= 1
   
    if(counter_min<=0):
       counter_min = 59
       counter_entry_min.delete(0, END)
       counter_entry_min.insert(0, str(counter_min))
    else:   
     counter_entry_min.delete(0, END)
     counter_entry_min.insert(0, str(counter_min))   
    if(counter_min<10):
       counter_entry_min.delete(0, END)
       counter_entry_min.insert(0, "0" + str(counter_min))

def increase_counter_sec():
    global counter_sec
    counter_sec += 1
   
    if(counter_sec >= 60):
       counter_sec = 0
       counter_entry_sec.delete(0, END)
       counter_entry_sec.insert(0, str(counter_sec))
    else:  
     counter_entry_sec.delete(0, END)
     counter_entry_sec.insert(0, str(counter_sec))
    if(counter_sec<10):
       counter_entry_sec.delete(0, END)
       counter_entry_sec.insert(0, "0" + str(counter_sec)) 

def decrease_counter_sec():
    global counter_sec
    counter_sec -= 1
    
    if(counter_sec<=0):
       counter_sec = 59
       counter_entry_sec.delete(0, END)
       counter_entry_sec.insert(0, str(counter_sec)) 
    else:   
        counter_entry_sec.delete(0, END)
        counter_entry_sec.insert(0, str(counter_sec))        
    if(counter_sec<10):
       counter_entry_sec.delete(0, END)
       counter_entry_sec.insert(0, "0" + str(counter_sec))

heading = Label(portion, text = "Alarm Time Set", height = 3, font = ("Times 30 bold"), bg ='#{:02x}{:02x}{:02x}'.format(204, 16, 250))
heading.place(x = 108, y = 20)

hour = Label(portion, text = "HOURS", height = 5, font = ("Times 10 bold"), bg ='#{:02x}{:02x}{:02x}'.format(204, 16, 250))
hour.place(x = 108, y = 120)




counter_hour = 0

counter_entry_hour = Entry(portion, width = 3, font=("Arial", 22), justify='center', bg = '#{:02x}{:02x}{:02x}'.format(180, 240, 245 ), bd = 2, relief="groove")
counter_entry_hour.insert(0, str(counter_hour))
counter_entry_hour.place(x = 104, y = 180)
increase_button_hour = Button(portion, width =4, height = 3, text="▲", command=increase_counter_hour, font=("Arial",5))
increase_button_hour.place(x = 106, y = 225)
decrease_button_hour = Button(portion, width = 4, height = 3, text="▼", command=decrease_counter_hour, font=("Arial", 5))
decrease_button_hour.place(x = 133, y = 225)


counter_min = 0

min = Label(portion, text = "MINUTES", height = 5, font = ("Times 10 bold"), bg ='#{:02x}{:02x}{:02x}'.format(204, 16, 250))
min.place(x = 170, y = 120)



counter_entry_min = Entry(portion, width = 3, font=("Arial", 22), justify='center', bg = '#{:02x}{:02x}{:02x}'.format(180, 240, 245 ), bd = 2, relief="groove")
counter_entry_min.insert(0, str(counter_min))
counter_entry_min.place(x = 177, y = 180)
increase_button_min = Button(portion, width =4, height = 3, text="▲", command=increase_counter_min, font=("Arial",5))
increase_button_min.place(x = 180, y = 225)
decrease_button_min = Button(portion, width = 4, height = 3, text="▼", command=decrease_counter_min, font=("Arial", 5))
decrease_button_min.place(x = 207, y = 225)


counter_sec = 0

seconds = Label(portion, text = "SECONDS", height = 5, font = ("Times 10 bold"), bg ='#{:02x}{:02x}{:02x}'.format(204, 16, 250))
seconds.place(x = 244, y = 120)




counter_entry_sec = Entry(portion, width = 3, font=("Arial", 22), justify='center', bg = '#{:02x}{:02x}{:02x}'.format(180, 240, 245 ), bd = 2, relief="groove")
counter_entry_sec.insert(0, str(counter_sec))
counter_entry_sec.place(x = 251, y = 180)
increase_button_sec = Button(portion, width =4, height = 3, text="▲", command=increase_counter_sec, font=("Arial",5))
increase_button_sec.place(x = 254, y = 225)
decrease_button_sec = Button(portion, width = 4, height = 3, text="▼", command=decrease_counter_sec, font=("Arial", 5))
decrease_button_sec.place(x = 281, y = 225)


part = Label(portion, text = "PERIOD", height = 5, font = ("Times 10 bold"), bg ='#{:02x}{:02x}{:02x}'.format(204, 16, 250))
part.place(x = 325, y = 120)



selected = IntVar()
counter = 0


counter_entry = Entry(portion, width = 3, font=("Arial", 22), justify='center', bg = '#{:02x}{:02x}{:02x}'.format(180, 240, 245 ), bd = 2, relief="groove")
counter_entry.insert(0, str(counter))
counter_entry.place(x = 327, y = 180)
increase_button = Button(portion, width = 4, height = 3, text="▲", command=increase_counter_part, font=("Arial",5))
increase_button.place(x = 329, y = 225)
decrease_button = Button(portion, width = 4, height = 3, text="▼", command=decrease_counter_part, font=("Arial", 5))
decrease_button.place(x = 356, y = 225)

def set_alarm():
   a = Thread(target= alarm_time)
   a.start()

def dismiss_alarm():
   mixer.music.stop()   
   # snooze_thread = Thread(target=snooze)
   # snooze_thread.start()

set_btn = Radiobutton(portion, font = ('Times 16 bold'), value = TRUE , text = "set", bg ='#{:02x}{:02x}{:02x}'.format(204, 16, 250), command = set_alarm, variable=selected)
set_btn.place(x = 100, y = 270)

music_playList = Label(portion, text = "Music PlayList", height = 1, font = ("Ivy 7 bold"), bg = '#{:02x}{:02x}{:02x}'.format(255,255,255 ), bd = 2, relief="groove")
music_playList.configure(width = 12, height = 3)
music_playList.place(x = 15 , y = 180)

music_playList_dropdown = Combobox(portion, width=9, height= 6, font= ('Times 10'))
music_playList_dropdown['values']=  ('alarm1.mp3', 'alarm2.mp3', 'alarm3.mp3')
music_playList_dropdown.place(x = 15 , y = 220)


def alarm_ring():
    
     mixer.music.load(music_playList_dropdown.get())
     mixer.music.play()
     selected.set(False)

def alarm_time():
   while True:
      control = selected.get()
      
      h_time = counter_entry_hour.get()
      m_time = counter_entry_min.get()
      s_time = counter_entry_sec.get()
      part_time = counter_entry.get().upper()
      # part_time = str(counter).upper()
       
      print("h: " + str(h_time))
      print("m: " + str(m_time))
      print("s: " + str(s_time))
      # print("h: " + str(p_time))

      # time_list.append([h_time, m_time, s_time, part_time])

       
      current_time = datetime.now()


      current_hour = current_time.strftime("%I")
      current_min = current_time.strftime("%M")
      current_sec = current_time.strftime("%S")
      current_part = current_time.strftime("%p")
      print(type(current_hour))

      print(current_hour )
      print(current_min)
      print(current_sec)
      print(current_part)

     
      if(control == TRUE  and  part_time == current_part and h_time == current_hour
        and m_time == current_min and s_time == current_sec):
         alarm_ring()
         
         dismiss_btn = Radiobutton(portion, font = ('Times 16 bold'), value = 3 , text = "dismiss", bg ='#{:02x}{:02x}{:02x}'.format(204, 16, 250), command = dismiss_alarm, variable = selected.get())
         dismiss_btn.place(x = 160, y = 270)
         

         snooze_btn = Radiobutton(portion, font = ('Times 16 bold'), value = TRUE, text = "snooze", bg ='#{:02x}{:02x}{:02x}'.format(204, 16, 250), command = snooze, variable=selected.get())
         snooze_btn.place(x = 250, y = 270)
         control = FALSE
         break
     

      sleep(1)


def reset():    
   control = FALSE

def back_screen():
    selected = FALSE

def snooze():
   #  sleep(snooze_duration)
    mixer.music.pause()
    sleep(60)
    mixer.music.load(music_playList_dropdown.get())
    mixer.music.play()
    reset()

         
   #  alarm_time()


mixer.init()
portion.mainloop()


