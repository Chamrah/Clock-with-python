#library that do the creation of graphical interfaces
import tkinter as tk
# Libray that have relation with the time
from time import strftime

def update_time():
    time_str = strftime("%H:%M:%S %p")
    lb1.config(text=time_str)
    lb1.after(1000, update_time)

# Display the program
root = tk.Tk()
root.title("Digital clock")


lb1 = tk.Label(root, font=('Arial', 50, 'bold'), background='black', foreground='green')
lb1.pack(anchor='center')

update_time()
root.mainloop()
