import tkinter as tk
import time

class pet():
    def __init__(self):
        # create a window
        self.window = tk.Tk()

        # placeholder image
        img = tk.PhotoImage(file='Assets/william_cat.png')

        # make window frameless
        self.window.overrideredirect(True)

        # make window draw over all others
        self.window.attributes('-topmost', True)

        # create a label as a container for our image
        self.label = tk.Label(self.window, bd=0, bg='gray')
        
        # turn black into transparency
        self.window.wm_attributes('-transparentcolor','gray')
        
        # create a window with size and cordinate
        self.window.geometry('150x150-15-15')

        # add the image to our label
        self.label.configure(image=img)

        # give window to geometry manager (so it will appear)
        self.label.pack()

        # run self.update() after 0ms when mainloop starts
        self.window.after(0, self.update)
        self.window.mainloop()
        
    def update(self):
        self.window.after(10, self.update)

pet()