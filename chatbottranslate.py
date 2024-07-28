from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.geometry('1100x320')
# root.iconbitmap(default='warning')  #This line might cause issues, remove if necessary
root['bg']= 'skyblue'
root.title('Language translator by Gitau Ian')

Input_text = Entry(root, width=60)
Input_text.place(x=30, y=130)
Input_text.get()

Label(root, text = "Output", font = 'arial 13 bold', bg = 'white smoke').place(x=780, y=90)
Output_text = Text(root, font='arial 10', height = 5, wrap = WORD, padx= 5, pady = 5, width = 50)
Output_text.place(x=600, y= 130)

Language = list(LANGUAGES.values())

dest_lang = ttk.Combobox(root, values = Language, width = 22)
dest_lang.place(x=130, y=160)
dest_lang.set('choose language')

def Translate():
    translator = Translator()
    translated = translator.translate(text=Input_text.get(), dest = dest_lang.get())
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)

#Translate button

trans_btn= Button(root, text = 'Translate', font = 'arial 12 bold', pady = 5, command= Translate, bg = 'orange', activebackground = 'green')

trans_btn.place(x= 445, y=180)


root.mainloop()  #Add the missing argument