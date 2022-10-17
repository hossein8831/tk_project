from tkinter import *
import wikipedia as wk
import speech_recognition as sr
import random
from PIL import ImageTk,Image
import urllib.request
wk.set_lang('fa')
win = Tk()
win.geometry('700x550')
win.iconbitmap('wiki.ico')
win.title('wiki search with Tk')
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
            r.pause_threshold = 3
            audio = r.listen(source)
            try:
                query = r.recognize_google(audio, language ='fa-IR', show_all=False)
                label_1.configure(text=query)
                result_wk = wk.summary(query,sentences=3)
                msg_1.configure(text=result_wk)
                wk.set_lang('fa')
                wer =wk.page(query).images
                urllib.request.urlretrieve(wer[random.randrange(1,11)],'sd.jpg')
                img = Image.open('sd.jpg')
                img = img.resize((300,250),Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                pj.configure(image=img)
                pj.image =img
            except Exception as e:
                label_1.configure(text='متوجه نشدم')
                msg_1.configure(text=':(')
label_1 = Label(text='None',fg='blue',bg='yellow',font='bold')
label_1.pack(ipadx='25')
button_1 = Button(text='سرچ کن',command=takeCommand)
button_1.pack(ipadx='30',ipady='8')
pj = Label(image= None)
pj.pack()
msg_1 = Message(text='.',font='bold',fg='green')
msg_1.pack(pady='10')
win.mainloop()
