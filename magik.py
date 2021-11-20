from tkinter import *
import random

root=Tk()

root.title("Lucky Friend+")
root.geometry("500x500")
root.configure(background = 'lavender')

entern = Entry(root)
entern.place(relx=0.5,rely=0.2,anchor=CENTER)

friend_list=Label(root)
rnl = Label(root)
lucky_friend = Label(root)

list1 = []
def addthatboi():
    friendn = entern.get()
    list1.append(friendn)
    friend_list['text'] = "Your friendlist : " + str(list1)
    
def randnumber():
    length = len(list1)
    random_no = random.randint(0, length-1)
    rnl['text'] = str(random_no)
    generated_random_number = list1[random_no]
    lucky_friend['text'] = "Your lucky friend is : " + str(generated_random_number) + ", totally not scuffed."

btn = Button(root, text="Add to the friendlist", command=addthatboi)
btn.place(relx=0.5,rely=0.3,anchor=CENTER)

rnl.place(relx=0.5,rely=0.6,anchor=CENTER)
lucky_friend.place(relx=0.5,rely=0.7,anchor = CENTER)
friend_list.place(relx=0.5,rely=0.4,anchor=CENTER)

btn1=Button(root,text='Who is your Lucky Friend?',command=randnumber)
btn1.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()