# Imports there
try :
	import pandas as pd
	from tkinter import *
	from datetime import datetime
	from random import choice
except:
	print("Import Error please install Required Package")


#Display Screen On Call
class DisplayMessage:
	def __init__(self,title,message):
		self.root=Tk()
			
		#Getting colours
		self.colorPrimary=choice(["red","green","purple","blue","orange","black","pink"])
		self.colorSecondry=choice(["#FFE4C4","#008B8B","#F5DEB3","#6495ED","#98FB98","#FF4500","#0000CD"])
		
		#Body of screen
		self.ScreenEdits()
		self.TopFrame(title,message)
		self.root.mainloop()
	
	#Screen Initial Sertings
	def ScreenEdits(self):
		self.root.title("Alvin's Reminder System")
		self.root.config(background="#f0fffc")
		self.root.geometry("1000x900")
		
	#Main message Creator in app
	def TopFrame(self,title,message):
		#main Canvas
		c1=Canvas(self.root,width="1000",height="720",background="#f0fffc")
		c1.pack()
		
		#message Title
		c1.create_text(500,100,width=800,fill=self.colorPrimary,font="Times 12 italic bold",text=title)
	
		#mesaage Body
		c1.create_text(500,300,width=800,fill=self.colorSecondry,font="Times 8 italic bold",text=message)
	
		b1=Button(self.root,text="Dismis",command=self.root.destroy)
		b1.pack(pady=40)
			

class GetRecord:
	def __init__(self):
		self.Get()
		self.Check()
					
	def Get(self):
		self.data=pd.read_excel("Record.xlsx")

	def Check(self):
		for i in range(1):#len(self.data)):
			
			#Organizing Date
			DateStamp=str(self.data["Date"][i]).split(" ")[0].split("-")
			raw_year=DateStamp[0]
			raw_month=DateStamp[1]
			raw_date=DateStamp[2]
			date=raw_date+raw_month+raw_year
			
			#Organizing Time
			TimeStamp=str(self.data["Time"][1]).split(":")
			raw_hrs=TimeStamp[0]
			raw_min=TimeStamp[1]
			time=raw_hrs+raw_min
			
			#full Stamp
			Stamp=date+time
				
 
GetRecord()
	    

		   											