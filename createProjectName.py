from tkinter import *
import datetime
import subprocess

selected_box1 = ''
selected_box2 = ''

def on_select_box1(event):
    global selected_box1
    selection = event.widget.curselection()
    if selection:
        selected_box1 = event.widget.get(selection[0])

def on_select_box2(event):
    global selected_box2
    selection = event.widget.curselection()
    if selection:
        selected_box2 = event.widget.get(selection[0])
    
def load_list(filename,user,box1,box2):
    with open(filename, 'r') as f:
        data = f.read().splitlines()
        
        user = data[0]
        index = data.index('----------')
        items1 = data[2:index]
        items2 = data[index+1:]

        entry_user.delete(0, END)
        box1.delete(0, END)
        box2.delete(0, END)
        
        entry_user.insert(0, user)
         
        for item in items1:
            box1.insert(END, item)
            
        for item in items2:
            box2.insert(END, item)
            
def add_item(box, entry, sort):
    if entry.get() != "":
        box.insert(END, entry.get())
        entry.delete(0, END)
        if sort:
            items = [box.get(idx) for idx in range(box.size())]
            items.sort()
            box.delete(0, END)
            for item in items:
                box.insert(END, item)
                
def del_list(box):
    select = list(box.curselection())
    select.reverse()
    for i in select:
        box.delete(i)
        
def save_list(user,box1, box2, filename):
    f = open(filename, 'w')   # Открываем файл в режиме записи
    f.truncate(0)    # Удаляем предыдущее содержимое файла
    #user = entry_user.get() 
    items1 = [f"{item}" for item in box1.get(0, END)]
    items2 = [f"{item}" for item in box2.get(0, END)]
    f.write("\n".join([user] + ['*******'] + items1 + ['----------'] + items2))
    f.close()

def create_project_name(user, selected_box1, selected_box2):
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d_%H-%M") #Текущая дата и время с использованием strftime:
    res.delete(0, END)
    if not selected_box1 or not selected_box2 or not user:
        res.insert(0, "Не выбран пользователь, проект или версия")
        return
    res.insert(0,  (user + "_" + selected_box1 + "_" + time + "_r" + selected_box2))
    result = user + "_" + selected_box1 + "_" + time + "_r" + selected_box2
    print(result)
    cmd="echo "+result.strip()+"|clip"
    return subprocess.check_call(cmd, shell=True)

root = Tk()
root.geometry("500x240")
root.resizable(False, False)
root.wm_attributes("-alpha", 0.93)
root.title("createProjectName")


# общий фрейм
Button(root, text="Save config", command=lambda: save_list(entry_user.get(), box1, box2, 'list.txt'), width="9")\
    .pack(side=TOP,anchor=W)
frame1 = Frame(root)
frame1.pack(side=TOP, padx=5,anchor=N)
frame_user = Frame(frame1)
frame_user.pack(side=LEFT, padx=5,anchor=N)
frame_prj = Frame(frame1)
frame_prj.pack(side=LEFT, padx=5,anchor=N)
frame_ver = Frame(frame1)
frame_ver.pack(side=LEFT, padx=5,anchor=N)
frame_res = Frame(root)
frame_res.pack(side=TOP, padx=5,anchor=N,fill=X,)

# набор для пользователя

lbl_user = Label(frame_user,width="7", text="User")
lbl_user.pack(anchor=N)
entry_user = Entry(frame_user , width="7")
entry_user.pack(anchor=N)

# набор для проекта
lbl_prj = Label(frame_prj,width="20", text="Projects")
lbl_prj.pack(side=TOP, padx=5)
box1 = Listbox(frame_prj, selectmode=EXTENDED)
box1.pack(side=LEFT)
box1.bind('<<ListboxSelect>>', on_select_box1)
scroll1 = Scrollbar(frame_prj, command=box1.yview)
scroll1.pack(side=LEFT, fill=Y)
box1.config(yscrollcommand=scroll1.set)

entry1 = Entry(frame_prj,width="12")
entry1.pack()
Button(frame_prj, text="Add", command=lambda: add_item(box1, entry1, 'false'),width="9")\
    .pack()
Button(frame_prj, text="Delete", command=lambda: del_list(box1),width="9")\
    .pack()

# набор для версии
lbl_ver = Label(frame_ver,width="15", text="Version")
lbl_ver.pack(side=TOP, padx=5)
box2 = Listbox(frame_ver, selectmode=EXTENDED ,width="12")
box2.pack(side=LEFT)
box2.bind('<<ListboxSelect>>', on_select_box2)
scroll2 = Scrollbar(frame_ver, command=box2.yview)
scroll2.pack(side=LEFT, fill=Y)
box2.config(yscrollcommand=scroll2.set)

entry2 = Entry(frame_ver,width="12")
entry2.pack()
Button(frame_ver, text="Add", command=lambda: add_item(box2, entry2, 'true'),width="9")\
    .pack()
Button(frame_ver, text="Delete", command=lambda: del_list(box2),width="9")\
    .pack()

# Набор результата
but = Button(frame_res, width="5", height = "1", text="Gen" , command= lambda:create_project_name( entry_user.get() , selected_box1 , selected_box2) )
res = Entry(frame_res,width="80")
but.pack(side=LEFT)
res.pack(side=RIGHT, padx=5 ,fill=X)

load_list('list.txt', entry_user, box1, box2)

root.mainloop()