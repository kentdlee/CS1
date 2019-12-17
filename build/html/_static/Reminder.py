import sys
import tkinter
import tkinter.messagebox
import os

def addReminder(text,x,y,notes,reminders):
    notewin = tkinter.Toplevel()
    notewin.resizable(width=False,height=False)
    notewin.geometry("+"+str(x)+"+"+str(y))
    
    reminder = tkinter.Text(notewin,bg="yellow", width=30,height=15)

    reminder.insert(tkinter.END,text)
    
    reminder.pack()

    
    notes.append(notewin)
    reminders.append(reminder)
    
    
    def deleteWindowHandler():
        print("Window Deleted")
        notewin.withdraw()
        notes.remove(notewin)
        reminders.remove(reminder)
    
    notewin.protocol("WM_DELETE_WINDOW", deleteWindowHandler)
    
    
def main():
    
    def post():
        print("Post")
        addReminder(note.get("1.0",tkinter.END), \
                  root.winfo_rootx()+5,root.winfo_rooty()+5,notes,reminders)
        note.delete("1.0",tkinter.END)               
   
    root = tkinter.Tk()
    
    root.title("Reminder!")
    root.resizable(width=False,height=False)

    notes = []
    reminders = []

    bar = tkinter.Menu(root)
    
    fileMenu = tkinter.Menu(bar,tearoff=0)
    fileMenu.add_command(label="Exit",command=root.quit)
    bar.add_cascade(label="File",menu=fileMenu)
    root.config(menu=bar)
    
    mainFrame = tkinter.Frame(root,borderwidth=1,padx=5,pady=5)
    mainFrame.pack()
    
    note = tkinter.Text(mainFrame,bg="yellow", width=30,height=15)
    note.pack()
    
    tkinter.Button(mainFrame,text="New Reminder!", command=post).pack()
  
    try:
        print("reading reminders.txt file")
        file = open("reminders.txt","r")
        x = int(file.readline())
        y = int(file.readline())
        root.geometry("+"+str(x)+"+"+str(y))
        
        
        line = file.readline()
        while line.strip() != "":
            x = int(line)
            y = int(file.readline())
            text = ""
            line = file.readline()
            while line.strip() != "____....____._._._":
                text = text + line
                line = file.readline()
                
            text = text.strip()
            
            addReminder(text,x,y,notes,reminders)
            
            line = file.readline()
    except:
        print("reminders.txt not found")
        
        
    
    def appClosing():
        print("Application Closing")
        file = open("reminders.txt","w")
        
        file.write(str(root.winfo_x())+"\n")
        file.write(str(root.winfo_y())+"\n")
        
        for i in range(len(notes)):
            print(notes[i].winfo_rootx())
            print(notes[i].winfo_rooty())
            print(reminders[i].get("1.0",tkinter.END))
            
            file.write(str(notes[i].winfo_rootx())+"\n")
            file.write(str(notes[i].winfo_rooty())+"\n")
            file.write(reminders[i].get("1.0",tkinter.END)+"\n")
            file.write("____....____._._._\n")
            
        file.close()
        root.destroy()
        root.quit()
        sys.exit()
        
    
    root.protocol("WM_DELETE_WINDOW", appClosing)  
    
         
    tkinter.mainloop()
    
if __name__ == "__main__":
    main()
