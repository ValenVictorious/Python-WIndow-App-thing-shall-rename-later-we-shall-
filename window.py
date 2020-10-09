import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

# create the application
cerra = App()

#
# here are method calls to the window manager class
#
cerra.master.title("CERRA")
cerra.master.maxsize(700, 700)
cerra.master.minsize(300, 300)
cerra.relief("groove")
# start the program
cerra.mainloop()