import tkinter as tk
from tkinter import *


#This does somthing
application = tk.Tk()

#Make the name and size
application.title("Ceasar Cypher Simulator")
application.geometry("600x400")


#Make GUI

Title = Label(application, text="Welcome to Epic Ceasar Cypher Simulator 😎", font="Arial 16")
Label1 = Label(application, text="Input Text to Encrypt / Decrypt:", font="Arial 10")
Input = Text(application, height=8, width=70)
Label2 = Label(application, text="Offset (Number):", font="Arial 10")
Offset = Entry(application, width=4)
Label3 = Label(application, text="Output:", font="Arial 10")
Output = Text(application, height=8, width=70)
Spacer1 = Label(application)
Spacer2 = Label(application, width=16)
Spacer3 = Label(application, width=16)
Spacer4 = Label(application, width=2)
Spacer5 = Label(application, width=2)
Encode = Button(application, text="Encode", font="Arial 10")
Decode = Button(application, text="Decode", font="Arial 10")
Unencryt = Button(application, text="Unencrypt", font="Arial 10")

Title.pack(side=TOP)

Spacer1.pack(side=BOTTOM)
Output.pack(side=BOTTOM)
Label3.pack(side=BOTTOM)
Input.pack(side=BOTTOM)
Label1.pack(side=BOTTOM)

Spacer2.pack(side=LEFT)
Spacer3.pack(side=RIGHT)
Label2.pack(side=LEFT, anchor=W)
Offset.pack(side=LEFT, anchor=W)

Unencryt.pack(side=RIGHT)
Spacer4.pack(side=RIGHT)
Decode.pack(side=RIGHT)
Spacer5.pack(side=RIGHT)
Encode.pack(side=RIGHT)


application.mainloop()
