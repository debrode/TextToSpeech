from tkinter import *
import pyttsx3


root=Tk()
root.title("Text-To-Speech")
root.geometry("800x500")
root.iconbitmap(r'favicon.ico')

def talk():
    voice=pyttsx3.init()
    voice.say(input.get())
    voice.runAndWait()
    input.delete(0,END)


input=Entry(root,font=("Helvetica",28))
input.pack(pady=20)

myBtn=Button(root,text="Speak",command=talk)
myBtn.pack(pady=20)


root.mainloop()
