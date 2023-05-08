import tkinter as tk
from tkinter import *
import re
class CypherProgame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Ceasar Cypher Simulator")
        self.geometry("600x400")



#This does somthing
application = CypherProgame()



#Functions

def Cypher(Words, Modifier, Preset):
    Nothing = True
    for i in Modifier:
        if i != " ":
            Nothing = False
    if Nothing:
        return("ERROR: NO OFFSET INPUTTED")

    try:
        Modifier = int(Modifier)
    except:
        return("ERROR: OFFSET NOT NUMBER")
    Letters = "abcdefghijklmnopqrstuvwxyz"
    Cyphered = ""
    for x in Words:
        if x.isalpha():
            if x.isupper():
                Letters = Letters.upper()
            else:
                Letters = Letters.lower()
            Position = 0
            for i in Letters:
                if i == x:
                    break
                else:
                    Position = Position + 1

            if Preset == "Encode":
                Position = Position + Modifier
            elif Preset == "Decode":
                Position = Position - Modifier
            Position = Position % 26


            Cyphered = Cyphered + Letters[Position]

        else:
            Cyphered = Cyphered + x

    print(Cyphered)
    return(Cyphered)


    return("Null.")


def UnencryptAI(Words):
    #so what i have to do is make somthing to get a value of english words to not english words
    with open('words.txt', 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    Text = Input.get("1.0", "end")
    Text = re.split(" |\n|\s", Text)
    #Text = [line.strip() for line in Text]
    print(Text)

    Exit = False
    while not Exit:
        for i in Text:
            if i == "":
                Text.remove("")
        print(Text)
        Repeat = False
        for i in Text:
            if i == "":
                Repeat = True
        if not Repeat:
            Exit = True

    print(Text)
    if Text[0] == "":
        return("ERROR: NO TEXT TO UNENCRYPT")

    return(Text)


def Write(text):
    Output.delete("1.0", "end")
    Output.insert(tk.END, text)

def ButtonPressed(Button):
    Change = Offset.get()
    Text = Input.get("1.0", "end")
    if Button == "Unencrypt":
        Write(UnencryptAI(Text))
    else:
        Write(Cypher(Text, Change, Button))




#Button Press Detection
def EncodeFunction():
    ButtonPressed("Encode")
def DecodeFunction():
    ButtonPressed("Decode")
def UnencrytFunction():
    ButtonPressed("Unencrypt")


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
Encode = Button(application, text="Encode", font="Arial 10", command=EncodeFunction)
Decode = Button(application, text="Decode", font="Arial 10", command=DecodeFunction)
Unencryt = Button(application, text="Unencrypt", font="Arial 10", command=UnencrytFunction)

Title.pack(side=TOP)

Spacer1.pack(side=BOTTOM)
Output.pack(side=BOTTOM)
Label3.pack(side=BOTTOM)
Input.pack(side=BOTTOM)
Label1.pack(side=BOTTOM)

Spacer2.pack(side=LEFT)
Label2.pack(side=LEFT)
Offset.pack(side=LEFT)

Spacer3.pack(side=RIGHT)
Unencryt.pack(side=RIGHT)
Spacer4.pack(side=RIGHT)
Decode.pack(side=RIGHT)
Spacer5.pack(side=RIGHT)
Encode.pack(side=RIGHT)


application.mainloop()

#