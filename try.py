import tkinter as tk
from tkinter import filedialog
from tkinter import StringVar
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from email12 import *
import csv
# Top level window
frame = tk.Tk()
frame.title("Mass email")
frame.geometry('600x800')
# Function for getting Input
# from textbox and printing it
# at label widget
Email_value=tk.StringVar()
Password_value=tk.StringVar()
Subject_value=tk.StringVar()
Body_value=""#tk.StringVar()
# For footer
photo=tk.StringVar()#logo_path
full_name=tk.StringVar()#full name
website=tk.StringVar()
fb=tk.StringVar()
linked=tk.StringVar()
twitter=tk.StringVar()
email=tk.StringVar()
phone=tk.StringVar()
logo1=tk.StringVar()
logo1=""
photo=""
filename=""
def printInput():
	global Email_value,inputtxt
	inp = inputtxt.get(1.0, "end-1c")
	Body_value=inp
	print("Email ",Email_value.get())
	print("Password ",Password_value.get())
	print("Subject ",Subject_value.get())
	print("Body :",inp)
	print("Full N : ",full_name.get())
	print("Webste : ",website.get())
	print("Facebo : ",fb.get())
	print("Linked : ",linked.get())
	print("Twitte : ",twitter.get())
	print("Email : ",email.get())
	print("Contact : ",phone.get())
	print("foto ",photo)
	print("logo ",logo1)
	footer1=footer(photo,full_name.get(),website.get(),fb.get(),linked.get(),twitter.get(),email.get(),phone.get(),logo1)
	
	body1=body(inp)
	# print(header1+body1+footer1)
	print(filename)
	with open(filename) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		for row in csv_reader:
			if line_count == 0:
				print(row)#print(f'Column names are {", ".join(row)}')
				line_count += 1
			else:
				header1=header("<div>To,<br>The Principal,<br>"+row[1]+",<br>"+row[2]+"<br><br><section style='padding-left:10px;'>Subject:<span style='padding-left:5px;'>"+Subject_value.get()+"</span></section></div>")
				send_email(sender_email=Email_value.get().strip(),password=Password_value.get().strip(),body=header1+body1+footer1,subject=Subject_value.get(),logo_path=logo1,receiver_email=row[0])
				print(f'\t{row[0]} ')#works in the {row[1]} department, and was born in {row[2]}.
				line_count += 1
		print(f'Sent to {line_count} email addresses.')
		print(header1+body1+footer1)
			# inp = inputtxt.get(1.0, "end-1c")
	# lbl.config(text = "Provided Input: "+inp)


def button(label1,command1,frame_name):
	# global btn
	label=label1
	command1=command1
	frame_name=frame_name
	button=tk.Button(frame_name,text=label,command=command1).pack()
	return button
def callback1(input):
    if input.isdigit():
		#btn.config(state='active')
        print(input)
        return True  
    else:
		#btn.config(state='disabled')
        return False
def callback3(input):
    if input.isalnum() and len(input)>5:
		#btn.config(state='active')
        print(input)
        return True
  
    else:		
		#btn.config(state='disabled')
        return False
def callback2(input):
	print(input)
	try:
		if len(input)>8 and input.index('@')==input.rindex('@') and input.index('.com')>=0:
			#btn.config(state='active')
			print(input)
			return True

		else:
			#btn.config(state='disabled')
			return False
	except:
		#btn.config(state='disabled')
		return False

reg = frame.register(callback1)
reg1 = frame.register(callback2)
reg2 = frame.register(callback3)

def text1(label1,frame1,variables1,width=20):
	frame_name=frame1
	label=tk.Label(text=label1).pack()
	text1= tk.Entry(frame_name,width=width,textvariable=variables1)
	text1.pack()

def entry1(label1,frame1,variables1,validation,width=20):
	frame_name=frame1
	label=tk.Label(text=label1).pack()
	text1= tk.Entry(frame_name,width=width,textvariable=variables1)
	text1.pack()
	if validation=="int":
		text1.config(validate ="focusout", 
         validatecommand =(reg, "% P"))
	elif validation=="email":
		text1.config(validate ="focusout", 
         validatecommand =(reg1, "% P"))
	else:
		text1.config(validate ="focusout", 
         validatecommand =(reg2, "% P"))#btn.confi
# Function for opening the
# file explorer window
def browseFiles(x):
	global logo1,photo,filename
	filename1 = filedialog.askopenfilename(initialdir = "/",
										title = "Select a File",
										filetypes = (("all files",
														"*.*"),("JPEG",
														"*.jpeg*"),
														("JPG",
														"*.jpg*"),
														("GIF",
														"*.gif*"),
														("png",
														"*.png*")
													))
	
	if x==0:
		logo1=filename1
	elif x==1:
		photo=filename1
	elif x==2:
		filename=filename1
	# if 
	# Change label contents
	# filename

def header(salutation="Sir"):
	header=f'''
	<html>
	<head>
		<style>@import url('https://fonts.googleapis.com/css?family=Oxygen');</style>
	</head>
	<body>
	<div style="margin-top:4px;">{salutation}</div>
	'''
	return header
def body(inp):
	body1=f"<section>{inp}</section><br><section style='margin-top:4px;text-align:center;'>Thank you!</section>"
	return body1
def footer(photo,full_name,website,fb,linked,twitter,email,phone,logo1=""):
	footer1=f'''
	<div style="margin-top:4px;">
		Sincerely yours,<br>
		{full_name},<br>
		Deputy-Coordinator,<br>
		Organizing Committee
		Coding Olympics Nepal
	</div>
	<section>
	  <table style="width:100%;background:whitesmoke;height: 213px; padding-top:33px; padding-right:0; padding-bottom:38px; padding-left:10px; font-family: 'Oxygen', sans-serif; font-size: 12px">
		<tbody>
		<tr>
			<td style="width:110px; padding:0;">
			<img src="'''+logo1+'''"  style="width:92px;height:92px;border-radius:50%;  padding-right: 20px; opacity: 0.8">
			<br>
			<br>
			<a href="'''+fb+'''"><img src="https://mleewise.com/assets/img/facebook32px.png" width=16px alt="Facebook Link" style="padding-left:14px;"></a>
			<a href="'''+linked+'''"><img src="https://mleewise.com/assets/img/linkedin32px.png" width=16px alt="LinkedIn Link"></a>
			<a href="'''+twitter+'''"><img src="https://mleewise.com/assets/img/twitter32px.png" width=16px alt="Twitter Link"></a>
			
			</td>
			<td style="border-left: 2px solid #f1451e; width:22px; height:136px; padding: 0px; opacity:0.8"></td>
			<td style="padding:0px">
			
			<div style="font-size:26px;font-weight:700;">'''+full_name.strip()+'''</div>
			<br style="line-height:10px">
			<a href="tel:'''+phone+'''" style="font-size:18px;text-decoration:none; color:black;"><img src="https://www.mleewise.com/assets/img/telephone32px.png"  height=10px alt="Orange Phone Icon">'''+phone+'''</a>
			<br>
			<a href="mailto:'''+email+'''" style="font-size:18px;text-decoration:none; color:black;"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNFH-wlpKR5lZPPkAKiOqhaiRYfR0L_gHTtzkIzZRl&s" width=16px alt="Twitter Link">'''+email+'''</a>
			<br>
			'''
	if website!="":
		footer1+='''<a href="'''+website+'''" style="font-size:18px;text-decoration:none; color:black;"><img src="https://www.mleewise.com/assets/img/linkthickflip32px.png"  height=12px alt="Orange Link Icon"> '''+website+'''</a>
			<br>'''
	footer1+='''<br style="line-height:30px">
			<!--a href="'''+website+'''"><img src="'''+logo1+'''" alt="The logo for 'Primary Theory'" style="width:158px;height:140px;"></a-->
			
			</td>
		 </tr>
		</tbody>
	</table>
	</section>
	'''
	# print(footer1)
	return footer1+"""
	</body>
	</html>"""



my_font1=('times', 12, 'bold')
tk.Label(frame,text="Main Email ",font=my_font1).pack()

entry1("email",frame,Email_value,"email")
entry1("password",frame,Password_value,"email")
entry1("subject",frame,Subject_value,"email")
# entry1("body",frame,Body_value,"int")
l = tk.Label(frame, text = "Body").pack()
inputtxt = tk.Text(frame,
                   height = 5,
                   width = 20)
  
inputtxt.pack()
#footer
tk.Label(frame,text="Details for footer design",font=my_font1).pack()
entry1("Full Name",frame,full_name,"string")
entry1("Webste link",frame,website,"string")
entry1("Facebook Link",frame,fb,"string")
entry1("Linkedin Link",frame,linked,"string")
entry1("Twitter Link",frame,twitter,"string")
entry1("Email",frame,email,"email")
entry1("Contact number",frame,phone,"string")

tk.Button(frame,
						text = "Company Logo",
						command =lambda: browseFiles(0)).pack()
tk.Button(frame,
						text = "Contact person photo",
						command = lambda:browseFiles(1)).pack()




##footer end
l1 = tk.Label(frame,text='Upload File & read',width=30,font=my_font1).pack()
b1 = tk.Button(frame, text='Upload File', 
   width=20,command = lambda:upload_file()).pack()
btn=tk.Button(text="Submit",command=printInput).pack()#button("Submit",printInput,frame)
# TextBox Creation
# inputtxt = tk.Text(frame,
# 				height = 5,
# 				width = 20)

# inputtxt.pack()

# # Button Creation
# printButton = tk.Button(frame,
# 						text = "Print",
# 						command = printInput)
# printButton.pack()
# Label Creation
def upload_file():
	global filename
	file1 = filedialog.askopenfilename()
	footer("https://mleewise.com/assets/img/JN-PT.png","Sangam Thapa","google.com","fb.com/sangam218","linkedin.com/in/sangam218","twitter.com/sangam218","sangam11e@gmail.com","+9779860865421","https://scontent.fbwa1-1.fna.fbcdn.net/v/t39.30808-6/314359627_115296531389943_8586446705815225360_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=UrSa032TsPwAX-NB96b&_nc_ht=scontent.fbwa1-1.fna&oh=00_AfD74gFQ-oFAZ3BtTWRbxP-3CijHs0K70lHnMIK2Za_3cw&oe=638E1B40")
	fob=open(file1,'r')
	filename=file1
    # print(fob.read())
frame.mainloop()

