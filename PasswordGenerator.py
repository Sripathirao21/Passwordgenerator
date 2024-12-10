from tkinter import *
from random import randint

root = Tk()
root.title('Optimal-Password Generator')
root.iconbitmap('Lockico.ico')
root.geometry("500x300")
the_password=chr(randint(33,126))

def new_rand():
    #clear screen
    pr_entry.delete(0,END)

    #get length

    pr_length = int(given_entry.get())
    print(pr_entry)

    #variable to hold our password

    the_password = ''

    #loop in password length

    for x in range(pr_length):
        the_password += chr(randint(33,126))
    
    #output text

    pr_entry.insert(0,the_password)



def clipper():
    root.clipboard_clear()
    root.clipboard_append(pr_entry.get())


#label frame

lf= LabelFrame(root, text="Give the count of characters !")
lf.pack(pady=20)

#entry box
given_entry =  Entry(lf, font=("Helvetica",24))
given_entry.pack(pady=20,padx=20)

#box for our returned value

pr_entry = Entry(root, text='',font=('Helvetica',24),bd=0,bg="systembuttonface")

pr_entry.pack(pady=20)

#create a frame for our button

made_frame = Frame(root)
made_frame.pack(pady=20)

#button creation

press_buttons = Button(made_frame,text='Generate Strong Password',command=new_rand)
press_buttons.grid(row=0,column=0,padx=10)

clip_button = Button(made_frame,text='Copy text to clipboard',command=clipper)
clip_button.grid(row=0,column=1, padx=10)




root.mainloop()