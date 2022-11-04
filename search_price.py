from pprint import pprint
import csv
import json
import pandas as pd
import requests
import ast
import re
import sys

#-----------------------------------------------Q2: get price----------------------------------------------------

def searchp(lower_range,upper_range):
	
	#Define the query and desired range of output as a variables
	payload = {'orderBy':'"price"','startAt': lower_range, 'endAt': upper_range}

	#Get result from firebase
	r2 = requests.get('https://dsci551-hw1-c8674-default-rtdb.firebaseio.com/cars/.json', params=payload)

	#Convert the query result into a json object
	result2=r2.json()

	
	#Get the Car IDs as a sorted list from the keys of the result2 dictionary
	result2=result2.keys()
	answer2=[]

	for CarID in result2:
		answer2.append(int(CarID))
	answer2.sort()



	#Print result if not blank otherwise display message
	if not answer2==[]:
		print(f"IDs for the car price range are: {answer2}")
	else:
		print('No cars found with the given range')


if __name__ == "__main__":

	try:
		lower_range= sys.argv[1]
		upper_range= sys.argv[2]
		searchp(lower_range,upper_range)

	except: print('Please define an upper and lower limit for the price range')

	