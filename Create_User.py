'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
#####
Ammaar Siddiqui
Create User
Version 1 .0
This is my create user program
The user can choose their username, password, gender, type(admin, user, guest), and job.
'''

#Ammaar Siddiqui
#Advanced Computer Programming
#9/24/18

from tkinter import *
from tkinter import ttk
#imports tkinter libraries

class App:
    def __init__(self, master, *args):
        main_frame=Frame(master)
        main_frame.pack(side=TOP)#makes main frame

        self.userlabel=Label(main_frame, text="Username")
        self.userlabel.pack(anchor='w')
        self.username=Entry(main_frame, textvariable=un)
        self.username.pack(anchor='w')#puts the username and user label on top of frame

        self.passlabel=Label(main_frame, text="Password")
        self.passlabel.pack(anchor='w')
        self.password=Entry(main_frame,show="*", textvariable=pw)
        self.password.pack(anchor='w')#same for password entry

        self.gender=Label(main_frame, text="Gender:")
        self.gender.pack(anchor='w')
        mf.set(0)
        self.male=Radiobutton(main_frame, text="Male", variable=mf, value="male")
        self.male.pack(anchor='w')
        self.female=Radiobutton(main_frame, text="Female", variable=mf, value="female")
        self.female.pack(anchor='w')#makes radiobutton for male/female

        self.typelabel=Label(main_frame, text="User Type:")
        self.typelabel.pack(anchor='w')
        self.admin=Checkbutton(main_frame, text="Admin", variable=user_type, onvalue="admin", offvalue="")
        self.admin.pack(anchor='w')
        self.user=Checkbutton(main_frame, text="User", variable=user_type, onvalue="user", offvalue="")
        self.user.pack(anchor='w')
        self.guest=Checkbutton(main_frame, text="Guest", variable=user_type, onvalue="guest", offvalue="")
        self.guest.pack(anchor='w')#makes three checkbuttons with same variable so you can only select one

        self.joblabel=Label(main_frame, text="Job:")
        self.joblabel.pack(anchor='w')
        self.jobs=ttk.Combobox(main_frame, values=["IT", "HR", "Sales", "Maintenance", "Other"], textvariable=job, state='readonly')
        self.jobs.pack(anchor='w')#makes a combobox with the different jobs along with label
        self.jobs.bind('<FocusIn>', self.defocus)#gets rid of blue higlight on combobox

        frame4=Frame(main_frame)
        frame4.pack(anchor='w')
        self.spacer=Label(frame4, text="")
        self.spacer.pack()#spacer between all entries and buttons

        frame2=Frame(main_frame)
        frame2.pack(anchor='w')
        self.submit=Button(frame2, text="Submit", command=self.save_all)
        self.submit.pack(side=LEFT)
        self.clear=Button(frame2, text="Clear", command=self.clearall)
        self.clear.pack(side=RIGHT)#makes new frame for submit/clear

        frame3=Frame(main_frame)
        frame3.pack(anchor='w')
        self.success=Label(frame3, text="")
        self.success.pack(anchor='w')
        self.reason=Label(frame3, text="")
        self.reason.pack(anchor='w')#new frame for failure/success label and reason for failure label

    def save_all(self):
        allusernames=[]
        file=open("users.txt","r")
        allusers=file.readlines()
        file.close()#pust all usernames in list
        for user in allusers:
            all_objects=user.split("***")
            allusernames.append(all_objects[0])
        if un.get()=="":#checks if username is entered
            self.success.config(text="Error")
            self.reason.config(text="Please enter username")
        elif pw.get()=="":#checks if password is entered
            self.success.config(text="Error")
            self.reason.config(text="Please enter password")
        elif mf.get()==0:#checks if gender is chosen
            self.success.config(text="Error")
            self.reason.config(text="Please choose gender")
        elif  user_type.get()=="":#checks if checkbutton is selected
            self.success.config(text="Error")
            self.reason.config(text="Please choose user type")
        elif job.get()=="":#checks if combobox has something selected
            self.success.config(text="Error")
            self.reason.config(text="Please choose a job")
        elif un.get() in allusernames:#checks if username is taken
            self.success.config(text="Error")
            self.reason.config(text="Username is already taken")
        else:
            file=open("users.txt","a")
            file.write(un.get()+"***"+pw.get()+"***"+mf.get()+"***"+user_type.get()+"***"+job.get()+"\n")
            file.close()
            self.success.config(text="User Created")
            self.reason.config(text="")
            self.username.delete(0, "end")
            self.password.delete(0, 'end')
            mf.set(0)
            self.admin.deselect()
            self.guest.deselect()
            self.user.deselect()
            job.set('')#if it meets all criteria it saves everyhting to a file
            

    def clearall(self):
        self.username.delete(0, "end")
        self.password.delete(0, 'end')
        mf.set(0)
        self.admin.deselect()
        self.guest.deselect()
        self.user.deselect()
        job.set('')
        self.success.config(text="")
        self.reason.config(text="")#clears everything

    def defocus(self, event):
        event.widget.master.focus_set()#gets rid of blue highlighting on combobox
        

root = Tk()
un=StringVar()
pw=StringVar()
mf=StringVar()
user_type=StringVar()
job=StringVar()
app = App(root, un, pw, mf, user_type, job)#define and pass all variables
root.title("Create User")#tab title
root.geometry("250x400")#sixe of tab
root.resizable(width=False, height=False)#so they can't full screen
root.mainloop()#puts into loop
root.destroy()
