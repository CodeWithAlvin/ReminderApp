# Imports there
try :
	import pandas as pd	
	from tkinter import Tk,Canvas,Button
	from datetime import datetime
	from random import choice
except:
	print("Import Error please install Required Package")


#Display Screen On Call
class DisplayMessage:
	def __init__(self,title,time,message):
		self.root=Tk()
			
		#Getting colours
		self.colorPrimary=choice(["red","green","purple","blue","orange","black","pink"])
		self.colorSecondry=choice(["#FFE4C4","#008B8B","#F5DEB3","#6495ED","#98FB98","#FF4500","#0000CD"])
		
		#Body of screen
		self.ScreenEdits()
		self.TopFrame(title,time,message)
		self.root.mainloop()
	
	#Screen Initial Sertings
	def ScreenEdits(self):
		self.root.title("Alvin's Reminder System")
		self.root.config(background="#f0fffc")
		self.root.geometry("1000x900")
		
	#Main message Creator in app
	def TopFrame(self,title,time,message):
		#main Canvas
		c1=Canvas(self.root,width="1000",height="720",background="#f0fffc")
		c1.pack()
		
		#message Title
		c1.create_text(500,100,width=800,fill=self.colorPrimary,font="Times 12 italic bold",text=title)
		
		#message Time
		c1.create_text(500,200,width=800,fill=self.colorPrimary,font="Times 5 italic bold",text=time)
	
		#mesaage Body
		c1.create_text(500,400,width=800,fill=self.colorSecondry,font="Times 8 italic bold",text=message)
	
		b1=Button(self.root,text="Dismis",command=self.root.destroy)
		b1.pack(pady=40)
			
class RunMessage:
	def __init__(self,i,data):
		#Getting Data To send		
		Title=data["TITLE"][i]
		Time=data["TIME"][i]
		Message=data["DESCRIPTION"][i]
		#Running Screen
		DisplayMessage(Title,Time,Message)




class GetRecord:
	def __init__(self):
		self.Get()
		self.Check()
					
	def Get(self):
		self.data=pd.read_excel("Record.xlsx")

	def Hackdata(self,DateStamp,TimeStamp):
		#Organizing Date
			raw_year=DateStamp[0]
			raw_month=DateStamp[1]
			raw_date=DateStamp[2]
			date=raw_year+raw_month+raw_date
			
			#Organizing Time			
			raw_hrs=TimeStamp[0]
			raw_min=TimeStamp[1]
			time=raw_hrs+raw_min
			
			#full Stamp
			return(date+time)
			
	def Check(self):
		for i in range(len(self.data)):
			DateStamp=str(self.data["DATE"][i]).split(" ")[0].split("-")
			TimeStamp=str(self.data["TIME"][i]).split(":")
			
			CurrentDate=str(datetime.now()).split(" ")[0].split("-")
			CurrentTime=str(datetime.now()).split(" ")[1].split(":")
			
			recordTime=self.Hackdata(DateStamp,TimeStamp)
			myTime=self.Hackdata(CurrentDate,CurrentTime)
					
			if recordTime==myTime:
				RunMessage(i,self.data)
	
				NewDf=self.data.drop(i)
				NewDf.to_excel("Record.xlsx",index=False)
      
                       
#Running App  
while True:
	GetRecord()
	    

		   											