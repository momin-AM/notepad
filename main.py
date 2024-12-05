from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as msg

file_path = "" 
open_opened = False
def save():
    global file_path,open_opened
    user_input=(text.get(1.0, 'end-1c'))
    if not open_opened:
        file_path = filedialog.asksaveasfilename( title="Create New File", defaultextension=".txt", filetypes=(("Text files", "*.txt"), ("All files", "*.*")) )
    elif file_path=='':
        msg.showerror('error','error in finding file!!!')
    else:
        pass
    with open(file_path,'w') as f:
        f.write(user_input)
    msg.showinfo('saved',f'your text saved successfully at {file_path}')
    
def open0():
    global file_path,open_opened
    file_path = filedialog.askopenfilename( title="Select a File", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if file_path: 
        with open(file_path, 'r') as f: 
            text_content = f.read() 
            text.delete(1.0, 'end') 
            text.insert(1.0, text_content) 
            open_opened = True

def new():
    global file_path
    text.delete(1.0, 'end')
    file_path=''


def about():
    msg.showinfo('Info','A under development note pad\n created by ->> Momin')

file_icon=r"C:\\Users\\sk454\\Downloads\\notepadicon.ico"

root=Tk()
root.iconbitmap(file_icon)
root.geometry('666x444')
root.title('Notepad')

main_menu=Menu(root)
meno0=Menu(main_menu,tearoff=0)
meno0.add_command(label='new',command=new)
meno0.add_command(label='save',command=save)
meno0.add_command(label='open',command=open0)
meno0.add_command(label='about',command=about)
main_menu.add_cascade(label='Options',menu=meno0)
meno1=Menu(main_menu,tearoff=0)
meno1.add_command(label='new submenu')
main_menu.add_cascade(label='new menu',menu=meno1)
root.config(menu=main_menu)


scrollbvar=Scrollbar(root,borderwidth=8)
scrollbvar.pack(side=RIGHT,fill=Y)

text=Text(root,yscrollcommand=scrollbvar.set)
text.pack(fill=BOTH)
scrollbvar.config(command=text.yview)


root.mainloop()
