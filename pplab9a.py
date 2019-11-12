from tkinter import *
from tkinter import messagebox
class Application(Frame):
	def __init__(self,master):
		Frame.__init__(self,master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		Label(self,text="Movie Selection").grid(row=0,column=0,columnspan=2,sticky=W)
		self.language = StringVar()
		Label(self,text="Choose a Language").grid(row=1,column=0,columnspan=2,sticky=W)
		Radiobutton(self,value="English",variable=self.language,text="English").grid(row=2,column=0,sticky=W)
		Radiobutton(self,value="Kannada",variable=self.language,text="Kannada").grid(row=2,column=1,sticky=W)
		Radiobutton(self,value="Hindi",variable=self.language,text="Hindi").grid(row=2,column=2,sticky=W)
		self.movieselect1 = BooleanVar()
		self.movieselect2 = BooleanVar()
		self.movieselect3 = BooleanVar()
		Label(self,text="Choose Movies:").grid(row=3,column=0,columnspan=2,sticky=W)
		Checkbutton(self,variable= self.movieselect1,text="Titanic").grid(row=4,column=0,sticky=W)
		Checkbutton(self,variable= self.movieselect2,text="Kirik Party").grid(row=4,column=1,sticky=W)
		Checkbutton(self,variable= self.movieselect3,text="Chicchore").grid(row=4,column=2,sticky=W)
		Label(self,text="Select the Number of Tickets:").grid(row=5,column=0,columnspan=2,sticky=W)
		self.tickets = StringVar()
		choices=['1','2','3','4','5']
		self.tickets.set('1')
		self.popupMenu = OptionMenu(self, self.tickets, *choices)
		self.popupMenu.grid(row = 6, column =1,sticky=W)
		self.btn = Button(self,text="Submit",command=self.check)
		self.btn.grid(row=10,column=2,sticky=W)


	def check(self):
		if self.language.get() == "":
			messagebox.showerror("Error","Please choose a Language")
		elif not self.movieselect1.get() and not self.movieselect2.get() and not self.movieselect3.get():
			messagebox.showerror("Error","Please choose a Movie")
		else:
			messagebox.showinfo("Success","Successfull")
	

root = Tk()
root.title("Movie ticket booking")
root.geometry("300x300")
app =Application(root)
root.mainloop()
