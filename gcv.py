# img_viewer.py
from azalpha import *
import PySimpleGUI as sg
import os.path
import traceback

# First the window layout in 2 columns

file_list_column = [
	[
		sg.Text("Source Document:"),
		sg.In(size=(25, 1), enable_events=True, key="-SRC_FILE-"),
		sg.FileBrowse(),
	],
	[
		sg.Text("Target Document:"),
		sg.In(size=(25, 1), enable_events=True, key="-DST_FILE-"),
		sg.FileBrowse(),
	],
	[
	sg.Button('To Arabic'), 
	sg.Button('To Latin'), 
	sg.Button('Help'), 
	sg.Button('Close')
	],
]

# For now will only show the name of the file that was chosen
output_viewer_column = [
	[sg.Text("Choose files and hit proper conversion button")],
	[sg.Text(size=(40, 2), key="-TOUT-")],
]

# ----- Full layout -----
layout = [
	[
		sg.Column(file_list_column),
		sg.VSeperator(),
		sg.Column(output_viewer_column),
	]
]

window = sg.Window("AzAlpha Converter", layout)

# Run the Event Loop
srcfile = '' 
dstfile = ''
sozluk = "./sozluk.xlsx"

while True:
	event, values = window.read()
	if event == "Close" or event == "Exit" or event == sg.WIN_CLOSED:
		break
	# Folder name was filled in, make a list of files in the folder
	if event == "-SRC_FILE-" or event == "-DST_FILE-" : # Just read the variables
		srcfile = values["-SRC_FILE-"]
		dstfile = values["-DST_FILE-"]
	
	elif event == "To Latin":  # file conversion from arabic to latin is requested
		try:
			window["-TOUT-"].update(srcfile + '\n' + dstfile)
			ar2la(srcfile , dstfile,sozluk, gui_log_message)
		except:
			pass

	elif event == "To Arabic":  # file conversion from latin  to arabic   is requested
		try:
			window["-TOUT-"].update(srcfile + '\n' + dstfile)
			arla(srcfile , dstfile,  sozluk , 'la2ar')
		except:
			print('Error:')
			traceback.print_exc()
			pass

window.close()

def gui_log_message(msg):
	window["-TOUT-"].update(msg)
