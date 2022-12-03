from tkinter import Label, Tk 
import time

root = Tk() 
root.title("Digital Clock") 
root.resizable(1,1)

def dig_clock():
   time_str = time.strftime("%I:%M:%S")
   time_label.config(text=time_str)
   
   date_str = time.strftime("%B  %d, %Y")
   date_label.config(text=date_str)
   
   day_str = time.strftime("%A")
   day_label.config(text=day_str)

   time_label.after(1000,dig_clock)

time_label = Label(root, font=("Calibri",45), bg="black", fg="yellow") 
time_label.pack()

date_label = Label(root, font=("Arial",15,"italic"), bg="white", fg="green") 
date_label.pack()

day_label = Label(root, font=("Arial",15,"italic"), bg="white", fg="green") 
day_label.pack()

dig_clock()
root.mainloop()