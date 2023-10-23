#Python to do list app
import tkinter
from tkinter.simpledialog import askstring
from ctypes import windll

root=tkinter.Tk()
windll.shcore.SetProcessDpiAwareness(1) #Makes the window less blurry

#Position and size of window (sizex x sizey + posx + posy)
root.geometry("1500x1000+450+400")

#Window Configuration
root.title('To Do List')
root.configure(background="#505050")
root.iconbitmap("images_icons\icon.ico")
root.resizable(False,False)

# Returns all tasks in the text file in a list
def listTasks():
    with open("ToDo.txt",'r') as reading:
        tasks = reading.readlines()
        return tasks # maybe recursion or something

def removeTask():
    taskList.config(state="normal")
    remove = askstring("Remove","Enter the task number you would like to remove:")
    __tasks = listTasks()
    for i in __tasks:
        if remove in i[0:2]:
            __tasks.remove(i)
    with open('ToDo.txt','w') as editing:
        for i in __tasks:
            editing.write(i)
        
taskList = tkinter.Text(height=28.6, width = 70, font=('Calibri',20))

# Populates the textbox with all the tasks in the list from the txt file using listTasks()
for i in range(len(listTasks())):
    taskList.insert(tkinter.END,f'{listTasks()[i]}',"white")# trying to display tasks line by line 

#Places the textbox on the window, makes the textbox read only
taskList.place(relx=0.01,rely=0.02)
taskList.config(state="disabled")

#Creates a button for removing tasks!
button = tkinter.Button(root, height = 6, width = 25, bg="#111233", fg="white", text="Remove", font=('Calibri',25,'bold'), command=removeTask)
button.place(relx=0.69,rely=0.02)

#Main loop
root.mainloop()