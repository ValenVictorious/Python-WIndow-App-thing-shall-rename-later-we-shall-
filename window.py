import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hello = tk.Button(self)
        self.hello["text"] = "what does this do?"
        self.hello["command"] = self.do
        self.hello.pack(side="top")

        self.make_button = tk.Button(self, fg="green")
        self.make_button["text"] = "mmake button?"
        self.make_button["command"] = self.new_button
        self.make_button.pack(side="bottom")

        self.kill_it = tk.Button(self, text="Kill It With CLicker!", fg="red", command=self.master.destroy )
        self.kill_it.pack(side="bottom")


    def do(self):
        print("I guess you will never know!")

    def new_button(self):
        self.thing = tk.Button(self, text="what does this do?")
        self.thing["command"] = self.works
        self.thing.pack(side="center")

    def works(self):
        print("wait! this actually works?")

# create the application
cerra = App()

#
# here are method calls to the window manager class
#
cerra.master.title("CERRA")
cerra.master.maxsize(700, 700)
cerra.master.minsize(300, 300)
# start the program
cerra.mainloop()