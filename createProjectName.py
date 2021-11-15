import tkinter
from tkinter import *
from tkinter import ttk
import datetime
import subprocess
import pickle

MY_USER = 'NRS'
now = datetime.datetime.now()
time = now.strftime("%Y-%m-%d_%H-%M") #Текущая дата и время с использованием strftime:
#user_backup = ''
#project_backup = 0
#sonata_backup = 0
app = tkinter.Tk()
app.geometry('400x150')
app.title("createProjectName")  
user_lbl = tkinter.Label(width="7",  text='user')
combo_project = ttk.Combobox(width="15")
combo_sonata = ttk.Combobox(width="7")
user_ent = Entry(width="7")
but = Button(text="Gen" , command= lambda:create_project_name( user_ent.get() , combo_project.get() , combo_sonata.get()) )
res = Entry(width="40")

projects = [
    "SEV",
    "KOV_ASU_TP_ESN",
    "KNG_PHG_VRK",
    "NOVOUB_ASUE",
    "NOVOURD_ASUE",
    "ZPLR_ASU_TP_ESN",
    "ZPLR_PRU",
    "ZPLR_SAU_BPG",
    "SOSN",
]

sonata = [
    "r10021",
    "r10223",
    "r7861",
    "r10255",
    "r10277",
    "r10301", 
]


def create_project_name(user, Project_attr, Sonata_attr):
    res.delete(0, END)
    res.insert(0,  (user + '_' + Project_attr + '_' + time + '_' + Sonata_attr))
    result = user + '_' + Project_attr + '_' + time + '_' + Sonata_attr
    prepare_data()
    cmd='echo '+result.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

def prepare_data():
    with open('data1.pickle', 'wb') as f:
        pickle.dump(user_ent.get(), f)
    with open('data2.pickle', 'wb') as f:
        pickle.dump(combo_project.get(), f)
    with open('data3.pickle', 'wb') as f:
        pickle.dump(combo_sonata.get()  , f)
 
def open_data():
    try:
        with open('data1.pickle', 'rb') as f:
            user_backup = pickle.load(f)
    except FileNotFoundError:
        user_backup = MY_USER
    try:
        with open('data2.pickle', 'rb') as f:
            project_backup = projects.index(pickle.load(f))
    except FileNotFoundError:
        project_backup = 0
    try:
        with open('data3.pickle', 'rb') as f:
            sonata_backup = sonata.index(pickle.load(f))
    except FileNotFoundError:
        sonata_backup = 0        
    return user_backup, project_backup, sonata_backup

def convert_data(user_backup,project_backup,sonata_backup):
    user_ent.insert( 1, user_backup) 
    combo_project.current(project_backup)
    combo_sonata.current(sonata_backup)


combo_project.configure(values = projects)
combo_sonata.configure(values = sonata)
user_backup,project_backup,sonata_backup = open_data()
convert_data(user_backup,project_backup,sonata_backup)


user_lbl.grid(row=1, column=0, ipadx=2, ipady=6, padx=2, pady=5)
user_ent.grid(row=1, column=1, ipadx=2, ipady=6, padx=2, pady=5)
combo_project.grid(row=2, column=0, ipadx=2, ipady=6, padx=2, pady=5)
combo_sonata.grid(row=2, column=1, ipadx=2, ipady=6, padx=2, pady=5)
but.grid(row=3, column=0, ipadx=2, ipady=6, padx=2, pady=5)
res.grid(row=3, column=1, ipadx=2, ipady=6, padx=2, pady=5)
app.mainloop()
