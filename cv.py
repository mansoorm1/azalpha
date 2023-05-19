from azalpha import *
from  docx import Document
import os
import pandas as pd
   

def main():

	sozluk = "./sozluk.xlsx"
	
	input_document  = './data/sample005.docx'
	output_document = './data/sample005_la.docx'

	arla (input_document,output_document, sozluk, 'ar2la' )

	
	return 
	
	
#main function

if __name__ == '__main__':
	main()
