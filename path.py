# Python program to create
# a file explorer in Tkinter

# import all components
# from the tkinter library
from tkinter import *
import csv
# import filedialog module
from tkinter import filedialog

# Function for opening the
# file explorer window
def browseFiles():
	test1 = filedialog.askopenfilename(initialdir = "/",
										title = "Select a File",
										filetypes = (("CSV files",
														"*.csv*"),
													("all files",
														"*.*")))
	
	# Change label contents
	label_file_explorer.configure(text="File Opened: "+test1)
	with open(test1) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		for row in csv_reader:
			if line_count == 0:
				print(row)#print(f'Column names are {", ".join(row)}')
				line_count += 1
			else:
				print(f'\t{row[0]} ')#works in the {row[1]} department, and was born in {row[2]}.
				line_count += 1
		print(f'Processed {line_count} lines.')
		# window.destroy()
	
																								
# Create the root window
window = Tk()

# Set window title
window.title('File Explorer')

# Set window size
window.geometry("500x500")

#Set window background color
window.config(background = "white")
test1=StringVar()
test1="File Explorer using Tkinter"
# Create a File Explorer label
label_file_explorer = Label(window,
							text = test1,
							width = 100, height = 4,
							fg = "blue")

	
button_explore = Button(window,
						text = "Browse Files",
						command = browseFiles)

button_exit = Button(window,
					text = "Exit",
					command = exit)

# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column = 1, row = 1)

button_explore.grid(column = 1, row = 2)

button_exit.grid(column = 1,row = 3)

# Let the window wait for any events
window.mainloop()
