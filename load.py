from pprint import pprint
import csv
import json
import pandas as pd
import requests
import ast
import re
import sys


#-----------------------------------------------Q1: Load data into Firebase----------------------------------------------------


def loadf(csvFilePath):
	# Load the csv file into a pandas dataframa
	df = pd.read_csv(csvFilePath)

	#set car ID as the index of the df
	df=df.set_index('car_ID')

	#Transpose the df so that the index is the key of the df when we convert it to json (not the features)
	df=df.transpose()

	#convert the transposed df into a dictionary
	df=df.to_dict('dict')

	#Convert the dictionary into a json object
	jsondata=json.dumps(df)

	#Create a node in firebase called cars
	requests.put('https://dsci551-hw1-c8674-default-rtdb.firebaseio.com/.json', data='{"cars":""}')

	#Load the jsondata into firebase under a node called cars
	requests.patch('https://dsci551-hw1-c8674-default-rtdb.firebaseio.com/cars/.json', data=jsondata)


if __name__ == "__main__":
    csvFilePath = sys.argv[1]
    loadf(csvFilePath)