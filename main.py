import tkinter as tk
from tkinter import *
import re
import openai
import time

openai.api_key = open("key.txt", "r").read()


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


    return(Cyphered)


def UnencryptAlgorythm():
    with open('words.txt', 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
    #reads all words and puts them in list lines


    New = []
    for x in range(26):
        New.append([])
    Alphabet = "abcdefghijklmnopqrstuvwxyz"
    for x in lines:
        New[Alphabet.find(x[0])].append(x)
    lines = New
    #Turns all words into lists alphabetically

    Text = Input.get("1.0", "end")
    Text = re.split(" |\n|\s", Text)
    # Gets text in textbox

    New = []
    for i in Text:
        if not i.isalpha():
            word = ""
            for x in i:
                if x.isalpha():
                    word = word + x
            New.append(word.lower())
        else:
            New.append(i.lower())
    Text = New


    Exit = False
    while not Exit:
        for i in Text:
            if i == "":
                Text.remove("")
        Repeat = False
        for i in Text:
            if i == "":
                Repeat = True
        if not Repeat:
            Exit = True
    #Turns words inputted into a list


    if not Text:
        return("ERROR: NO TEXT TO UNENCRYPT")


    Results = []
    for j in range(0, 26):
        Result = 0
        for i in Text:
            Decyphered = Cypher(i, str(j), "Decode")

            Data = [False]
            Position = Alphabet.find(Decyphered[0])
            Words = lines[Position]
            for x in Words:
                if Decyphered == x:
                    Data = [True, Decyphered, j]
            if Data[0]:
                Result = Result + 1
        Results.append(Result)
    print(Results)

    Highest = 0
    Change = 0
    for j in range(0, 26):
        if Results[j] > Highest:
            Highest = Results[j]
            Change = j



    Words = Input.get("1.0", "end")
    # Gets text in textbox

    return("The text has been deciphered with a key of " + str(Change) + " and an accuracy of " + str(round(Highest / len(Text) * 100)) + "%.\n"+ Cypher(Words, str(Change), "Decode"))


def UnencryptAI(Words):
    #ChatGPT partually wrote the following 7 lines of code.
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "The following text has been cyphered in a ceasar cypher, can you decypher it for me?: " + Words},
        ]
    )
    assistant_reply = response['choices'][0]['message']['content']
    return(assistant_reply)


def Write(text):
    Output.delete("1.0", "end")
    Output.insert(tk.END, text)

def ButtonPressed(Button):
    Change = Offset.get()
    Text = Input.get("1.0", "end")
    if Button == "AI":
        Write(UnencryptAI(Text))
    elif Button == "Algorythm":
        Write(UnencryptAlgorythm())
    else:
        Write(Cypher(Text, Change, Button))




#Button Press Detection
def EncodeFunction():
    ButtonPressed("Encode")
def DecodeFunction():
    ButtonPressed("Decode")
def AlgorythmFunction():
    ButtonPressed("Algorythm")
def AIFunction():
    ButtonPressed("AI")


#Make GUI

Title = Label(application, text="Welcome to Epic Ceasar Cypher Simulator 😎", font="Arial 16")
Label1 = Label(application, text="Input Text to Encrypt / Decrypt:", font="Arial 10")
Input = Text(application, height=8, width=70)
Label2 = Label(application, text="Offset (Number):", font="Arial 10")
Offset = Entry(application, width=4)
Label3 = Label(application, text="Output:", font="Arial 10")
Output = Text(application, height=8, width=70)
Spacer1 = Label(application)
Spacer2 = Label(application, width=3)
Spacer3 = Label(application, width=3)
Spacer4 = Label(application, width=2)
Spacer5 = Label(application, width=2)
Spacer6 = Label(application, width=2)
Encode = Button(application, text="Encode", font="Arial 10", command=EncodeFunction)
Decode = Button(application, text="Decode", font="Arial 10", command=DecodeFunction)
Unencryt = Button(application, text="Algorythm Unencrypt", font="Arial 10", command=AlgorythmFunction)
Broken = Button(application, text="AI Unencrypt", font="Arial 10", command=AIFunction)

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
Broken.pack(side=RIGHT)
Spacer4.pack(side=RIGHT)
Unencryt.pack(side=RIGHT)
Spacer5.pack(side=RIGHT)
Decode.pack(side=RIGHT)
Spacer6.pack(side=RIGHT)
Encode.pack(side=RIGHT)



application.mainloop()

#Ocvo rvn ijo v admz ydnodibpdnczm, ocvo rvn v agvhzocmjrzm, gjg.