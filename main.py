import os  # accessing the os functions
import Capture_Image
import Train_Image
import Recognize
from tkinter import * 
import tkinter as tk
import threading
from PIL import Image, ImageTk

def autom_call():
	tkStatus.set("Sending Mail...")
	status_label.update()
	os.system("py automail.py")
	tkStatus.set("Mail Sent")
	status_label.update()

def autom():
	t5=threading.Thread(target=autom_call,daemon=True)
	t5.start()


def cfaces_call():
    tkStatus.set("Capturing Faces...")
    status_label.update()
    try:
        Capture_Image.takeImages(str(tkID.get()),str(tkName.get()),str(tkEmail.get()))
        tkStatus.set("Faces Captured")
        status_label.update()
        tkID.set("")
        id_label.update()
        tkName.set("")
        name_label.update()
        tkEmail.set("")
        email_label.update()
    except Exception as e:
        if (tkID.get().isnumeric()==False):
            tkStatus.set("Enter valid user id")
            status_label.update()
        else:
            tkStatus.set("Enter valid user email")
            status_label.update()


def CaptureFaces():
	t2=threading.Thread(target=cfaces_call,daemon=True)
	t2.start()


def timages_call():
	tkStatus.set("Training Images...")
	status_label.update()
	Train_Image.TrainImages()
	tkStatus.set("Images Trained.")
	status_label.update()

def Trainimages():
	t3=threading.Thread(target=timages_call,daemon=True)
	t3.start()
	
def rfaces_call():
	tkStatus.set("Recognizing Faces...")
	status_label.update()
	Recognize.recognize_attendence()
	tkStatus.set("Faces Recognized.")
	status_label.update()

def RecognizeFaces():
	t4=threading.Thread(target=rfaces_call,daemon=True)
	t4.start()

root = Tk()  
root.title("Thapar Attendance System")
root.configure(background='#000000')
root.geometry('700x660')
tkID = tk.StringVar()
tkName = tk.StringVar()
tkEmail = tk.StringVar()  
tkStatus = tk.StringVar()      
image1 = Image.open("thapar.jpg")
image1= image1.resize((200, 200))
test = ImageTk.PhotoImage(image1)

label1 = tk.Label(image=test, bg="#000000")
label1.image = test
label1.grid(
	column=0
)


message = tk.Label(root, text="Get Present" ,bg="#000000"  ,fg="white" ,height=3,font=('times', 30 )) 

message.place(x=300, y=20)

root.resizable(False, False)
root.lift()
#root.attributes('-topmost', 1)


id_label = tk.Label(root,
        text='Enter Your Thapar ID:', bg='#000000',
        fg='#ffffff',
        anchor=tk.W)
id_label.grid(
    padx=0,
    pady=(8, 0),
    ipadx=0,
    ipady=1,
    row=1,
    column=1,
    columnspan=1,
    sticky=tk.W + tk.E + tk.N + tk.S,
    )

id_entry = tk.Entry(root, textvariable=tkID,
                           bg='#176B87', exportselection=0,
                           relief=tk.FLAT)
id_entry.grid(
    padx=0,
    pady=6,
    ipadx=8,
    ipady=8,
    row=1,
    column=2,
    columnspan=3,
    sticky=tk.W + tk.E + tk.N + tk.S,
    )

name_label = tk.Label(root,
        text='Enter Your Name(as per Webkiosk):', bg='#000000',
        fg='#ffffff',
        anchor=tk.W)
name_label.grid(
    padx=0,
    pady=(8, 0),
    ipadx=0,
    ipady=1,
    row=2,
    column=1,
    columnspan=1,
    sticky=tk.W + tk.E + tk.N + tk.S,
    )

name_entry = tk.Entry(root, textvariable=tkName,
                           bg='#176B87', exportselection=0,
                           relief=tk.FLAT)
name_entry.grid(
    padx=0,
    pady=6,
    ipadx=8,
    ipady=8,
    row=2,
    column=2,
    columnspan=3,
    sticky=tk.W + tk.E + tk.N + tk.S,
    )

email_label = tk.Label(root,
        text='Enter Email:', bg='#000000',
        fg = '#ffffff',
        anchor=tk.W)
email_label.grid(
    padx=0,
    pady=(8, 0),
    ipadx=0,
    ipady=1,
    row=3,
    column=1,
    columnspan=1,
    sticky=tk.W + tk.E + tk.N + tk.S,
    )

email_entry = tk.Entry(root, textvariable=tkEmail,
                           bg='#176B87', 
                            fg = '#ffffff',
                            exportselection=0,
                           relief=tk.FLAT)
email_entry.grid(
    padx=0,
    pady=6,
    ipadx=8,
    ipady=8,
    row=3,
    column=2,
    columnspan=3,
    sticky=tk.W + tk.E + tk.N + tk.S,
    )


btn2 = tk.Button(
    root,
    text='CAPTURE MY FACE',
    command=CaptureFaces,
    width=20,
    bg='#525FE1',
    fg='#ffffff',
    bd=2,
    relief=tk.FLAT,
    activebackground = "Green",
    activeforeground = "White",
    )
btn2.grid(
    padx=60,
    pady=8,
    ipadx=24,
    ipady=6,
    row=4,
    column=1,
    columnspan=4,
    sticky=tk.W + tk.E + tk.N + tk.S,
    )


btn3 = tk.Button(
    root,
    text='GET ME REGISTERED',
    command=Trainimages,
    width=20,
    bg='#525FE1',
    fg='#ffffff',
    bd=2,
    relief=tk.FLAT,
    activebackground = "Green",
    activeforeground = "White",
    )
btn3.grid(
    padx=60,
    pady=8,
    ipadx=24,
    ipady=6,
    row=5,
    column=1,
    columnspan=4,
    sticky=tk.W + tk.E + tk.N + tk.S,
    )


btn4 = tk.Button(
    root,
    text='RECOGNIZE ME',
    command=RecognizeFaces,
    width=20,
    bg='#525FE1',
    fg='#ffffff',
    bd=2,
    relief=tk.FLAT,
    activebackground = "Green",
    activeforeground = "White",
    )
btn4.grid(
    padx=60,
    pady=8,
    ipadx=24,
    ipady=6,
    row=6,
    column=1,
    columnspan=4,
    sticky=tk.W + tk.E + tk.N + tk.S,
    )


btn5 = tk.Button(
    root,
    text='MAIL ME ',
    command=autom,
    width=20,
    bg='#525FE1',
    fg='#ffffff',
    bd=2,
    relief=tk.FLAT,
    activebackground = "Green",
    activeforeground = "White",
    )
btn5.grid(
    padx=60,
    pady=8,
    ipadx=24,
    ipady=6,
    row=7,
    column=1,
    columnspan=4,
    sticky=tk.W + tk.E + tk.N + tk.S,
    )


btn6 = tk.Button(
    root,
    text='EXIT',
    command=root.destroy,
    width=20,
    bg='#525FE1',
    fg='#ffffff',
    bd=2,
    relief=tk.FLAT,
    activebackground = "Green",
    activeforeground = "White",
    )
btn6.grid(
    padx=60,
    pady=8,
    ipadx=24,
    ipady=6,
    row=8,
    column=1,
    columnspan=4,
    sticky=tk.W + tk.E + tk.N + tk.S,
    )

status_label = tk.Label(
    root,
    textvariable=tkStatus,
    bg='#001C30',
    anchor=tk.W,
    justify=tk.LEFT,
    relief=tk.FLAT,
    wraplength=350,
    )
status_label.grid(
    padx=12,
    pady=(0, 12),
    ipadx=0,
    ipady=1,
    row=9,
    column=1,
    columnspan=4,
    sticky=tk.W + tk.E + tk.N + tk.S,
    )
 
# Set the position of button on the top of window.      
 
root.mainloop()
#mainMenu()
