from pprint import pprint
import csv
import json
import pandas as pd
import requests
import ast
import re
import sys


#----------------Q3: Create a key-value pair of name keywords-car names and load into Firebase----------------------------------------------------


def loadf(csvFilePath):
	# Load the csv file into a pandas dataframa
	df2 = pd.read_csv(csvFilePath)

	#set car ID as the index of the df
	df2=df2.set_index('car_ID')



	#Create a keywords list of keywords appearing in each car name
	#--------------------------------------------------------------
	keywords=[]

	#Split each CarName into keywords using re.split('W+') to identify punctuation seperators and put in interim list called interim_keyword_list

	for name in df2['CarName']:
		interim_keyword_list=re.split('\W+',name)
		#Append interim_keyword_list to total list of sublists (interim_keyword_lists) called keywords
		keywords.append(interim_keyword_list)


	#Get the unique list of keywords
	#--------------------------------------------------------------

	#Convert the keywords list of lists into one big list
	keywords=[elem for sublist in keywords for elem in sublist]

	#Get only the unique keywords in the big list
	keywords=list(set(keywords))

	#Remove the blank value from the list to prepare for Firebase upload
	keywords.remove('')


	#Get the Car Names associated with each unique Keyword and put in dictionary called Keyword_index (WITHOUT Car NAME)
	#-------------------------------------------------------------------------------------------------------------------
	keyword_index={}

	for keyword in keywords:
		interimlist=[]

		for name in df2['CarName']:
			name_breakdown=re.split('\W+',name)


			if keyword in name_breakdown:
				Car_ID=df2.index[df2['CarName']==name].tolist()

				for ID in Car_ID:
					interimlist.append(ID)

			else: continue

		interimlist=list(set(interimlist))

		keyword_index[keyword]=interimlist

	





	#Convert the keyword_index dictionary into a json object
	keyword_index_json=json.dumps(keyword_index)

	#Create a node in firebase called keyword_index
	requests.patch('https://dsci551-hw1-c8674-default-rtdb.firebaseio.com/.json', data='{"keyword_index":""}')

	#Load the keyword_index jsondata into firebase under the node called keyword_indexrequests.patch('https://dsci551-hw1-c8674-default-rtdb.firebaseio.com/keyword_index.json', data=keyword_index_json)
	requests.patch('https://dsci551-hw1-c8674-default-rtdb.firebaseio.com/keyword_index.json', data=keyword_index_json)



if __name__ == "__main__":
    csvFilePath = sys.argv[1]
    loadf(csvFilePath)