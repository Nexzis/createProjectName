import tkinter
from tkinter import *
from tkinter import ttk
import datetime
import subprocess
import pickle


now = datetime.datetime.now()
time = now.strftime("%Y-%m-%d_%H-%M") #Текущая дата и время с использованием strftime:
app = tkinter.Tk()
app.geometry('400x150')
app.resizable(False, False)
app.title("createProjectName")  
user_lbl = tkinter.Label(width="7",  text='user')
combo_project = ttk.Combobox(width="15")
combo_sonata = ttk.Combobox(width="7")
user_ent = Entry(width="7")
but = Button(text="Gen" , command= lambda:create_project_name( user_ent.get() , combo_project.get() , combo_sonata.get()) )
res = Entry(width="40")


data_old = {
    'user': ['NRS'],
    'projects': [   "SEV",
                    "KOV_ASU_TP_ESN",
                    "KNG_PHG_VRK",
                    "NOVOUB_ASUE",
                    "NOVOURD_ASUE",
                    "ZPLR_ASU_TP_ESN",
                    "ZPLR_PRU",
                    "ZPLR_SAU_BPG",
                    "SOSN",],
    'versions': [   "10021",
                    "10223",
                    "7861",
                    "10255",
                    "10277",
                    "10301",
                    "10335"],
    'current_settings' : ['test',0,0]
}


def open_data():
    try:
        with open('config.pickle', 'rb') as f:
            data = pickle.load(f)
    except FileNotFoundError:
        data = data_old                       
    return data

def convert_data(user_backup,project_backup,sonata_backup):
    user_ent.insert( 1, user_backup) 
    combo_project.current(project_backup)   
    combo_sonata.current(sonata_backup)    


def create_project_name(user, Project_attr, Sonata_attr):
    res.delete(0, END)
    res.insert(0,  (user + '_' + Project_attr + '_' + time + '_r' + Sonata_attr))
    result = user + '_' + Project_attr + '_' + time + '_r' + Sonata_attr
    print(result)
    prepare_data()
    cmd='echo '+result.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)


def prepare_data():
    data['current_settings'][0] = user_ent.get()
    data['current_settings'][1] = combo_project.current()
    data['current_settings'][2] = combo_sonata.current()
    with open('config.pickle', 'wb') as f:
        pickle.dump(data, f) 


data = open_data() 
combo_project.configure(values = data['projects'])
combo_sonata.configure(values = data['versions'])
convert_data(data['current_settings'][0],data['current_settings'][1],data['current_settings'][2])

user_lbl.grid(row=1, column=0, ipadx=2, ipady=6, padx=2, pady=5)
user_ent.grid(row=1, column=1, ipadx=2, ipady=6, padx=2, pady=5)
combo_project.grid(row=2, column=0, ipadx=2, ipady=6, padx=2, pady=5)
combo_sonata.grid(row=2, column=1, ipadx=2, ipady=6, padx=2, pady=5)
but.grid(row=3, column=0, ipadx=2, ipady=6, padx=2, pady=5)
res.grid(row=3, column=1, ipadx=2, ipady=6, padx=2, pady=5)
app.mainloop()
