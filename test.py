'''
from breezypythongui import EasyFrame


#initializes the title screen
class display(EasyFrame):

    
    def __init__(self):
        EasyFrame.__init__(self)
        
        self.main_display = self.addLabel(text = 'Welcome to Fune', row = 0, column = 0, columnspan = 1, sticky = 'NSEW')
        self.start_button = self.addButton(text = 'Start', row = 1, column = 0, command = self.start)

    



#starts the game
def main():
    display().mainloop()
    
    

    
if __name__ == '__main__':
    main()
'''

from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk

'''
def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + .5) / 10000.0)
    except ValueError:
        pass

root = Tk()
root.title('Feet to Meters')

mainframe = ttk.Frame (root, padding = '3 3 12 12')
mainframe.grid(column = 0, row = 0, sticky = (N, W, S, E))
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width = 7, textvariable = feet)
feet_entry.grid(column = 2, row = 1, sticky = (W, E))

meters = StringVar()
ttk.Label(mainframe, textvariable = meters).grid(column = 2, row = 2, sticky = (W, E))

ttk.Button(mainframe, text = 'Calculate', command = calculate).grid(column = 3, row = 3, sticky = W)

ttk.Label(mainframe, text = 'feet').grid(column = 3, row = 1, sticky = W)
ttk.Label(mainframe, text = 'is equal to').grid(column = 1, row = 2, sticky = E)
ttk.Label(mainframe, text = 'meters').grid(column = 3, row = 2, sticky = W)

for child in mainframe.winfo_children():
    child.grid_configure(padx = 5, pady = 5)
feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()
'''

'''
test = Tk()
test.title("Image test")

rm12 = PhotoImage(file = "rm_12.png")

image_label= ttk.Label(test, image=rm12)
image_label.pack()

test.mainloop()
'''

import random


'''
room_changer = Tk()
room_changer.title("Room Changer")

mainframe = ttk.Frame (room_changer, padding = '12 12 12 12')
mainframe.grid(column = 0, row = 0, sticky = (N, W, S, E))
room_changer.columnconfigure(0, weight = 1)
room_changer.rowconfigure(0, weight = 1)

controller = Tk()
controller.title("Controller")

frame2 = ttk.Frame (controller, padding = '12 12 12 12')
frame2.grid(column = 0, row = 0, sticky = (N, W, S, E))
controller.columnconfigure(0, weight = 1)
controller.rowconfigure(0, weight = 1)


moves = {"up":True, 'down':False, 'left':False, 'right':False}


def new_room_up():
    new_room = random.randint(1,2)
    if moves['up']:
        if new_room == 1:
            new_image = ttk.Label(mainframe, image = room2).grid(row = 1, column = 1)
            moves['down'] = True
        elif new_room == 2:
            new_image = ttk.Label(mainframe, image = room3).grid(row = 1, column = 1)
            moves['down'] = True
    else:
        pass

def new_room_down():
    new_room = random.randint(1,2)
    global moves
    if moves['down']:
        if new_room == 1:
            new_image = ttk.Label(mainframe, image = room4).grid(row = 1, column = 1)
        elif new_room == 2:
            new_image = ttk.Label(mainframe, image = room5).grid(row = 1, column = 1)
    else:
        pass
        
    

room1 = PhotoImage(file = "rm_1.png")
room2 = PhotoImage(file = "rm_2.png")
room3 = PhotoImage(file = "rm_3.png")
room4 = PhotoImage(file = "rm_4.png")
room5 = PhotoImage(file = "rm_5.png")


image_label = ttk.Label(mainframe, image = room1).grid(row = 1, column = 1, )

ttk.Button(frame2, text = "Up", command = new_room_up).grid(row = 2, column = 1)
ttk.Button(frame2, text = "Down", command = new_room_down).grid(row = 2, column = 2)



room_changer.mainloop()
'''



