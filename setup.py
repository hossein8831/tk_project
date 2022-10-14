from tkinter import *
import wikipedia as wk
import speech_recognition as sr
wk.set_lang('fa')
win = Tk()
win.geometry('700x550')
win.iconbitmap('wiki.ico')
win.title('wiki search with Tk')
def takeCommand():
    global query
    r = sr.Recognizer()
    with sr.Microphone() as source:
            r.pause_threshold = 1
            audio = r.listen(source)
            msg_1.configure(text='yezare')
            try:
                query = r.recognize_google(audio, language ='fa-IR', show_all=False)
                label_1.configure(text=query)
                result_wk = wk.summary(query,sentences=2)
                msg_1.configure(text=result_wk)
        
            except Exception as e:
                label_1.configure(text='متوجه نشدم')
label_1 = Label(text='None',fg='blue',bg='yellow',font='bold')
label_1.pack(ipadx='25')
button_1 = Button(text='سرچ کن',command=takeCommand)
button_1.pack(ipadx='30',ipady='8')
msg_1 = Message(text='  ',fg='green',font='bold')

label_2 = Label(text=query)
label_2.pack()
msg_1.pack()
win.mainloop()
