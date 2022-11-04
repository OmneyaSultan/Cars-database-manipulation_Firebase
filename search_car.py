from pprint import pprint
import csv
import json
import pandas as pd
import requests
import ast
import re
import sys

#-----------------------------------------------------Q4: Search keyword Index by Car Name----------------------------------

def searchcar(keyword):
	#split the input keyword into tokens and store in search list
	search_list=re.split('\W+',keyword)

	if '' in search_list:
		search_list.remove('')

	result_dict={}

	#For each token(search_term) get the corresponding car IDs from firebase
	for i in range(len(search_list)):
		search_term='"'+search_list[i]+'"'

		#Define the query and desired range of output as a variables
		payload = {'orderBy':'"$key"','equalTo': search_term}

		#Get result from firebase and store in json object
		r = requests.get('https://dsci551-hw1-c8674-default-rtdb.firebaseio.com/keyword_index/.json', params=payload)
		r=r.json()


		#Format the search term so it can be used as key in json object to get corresponding values and store in a list
		search_term=search_term.replace('"','')

		result=list(r[search_term])

		result.sort()

		#create a dictionary of the search_term and result
		result_dict[search_term]=result


	#Get the list of lists of results of searches for all search terms
	finalresult=(list(result_dict.values()))

	
	#Get list of car IDs that are common across all search words
	#------------------------------------------------------------
	r6=finalresult 

	#the number of times the intersection operation will be done is 1 less than the number of search terms
	count=(len(search_list))-1

	#initialize a blank list to store the final sorted answer
	answer4=[]

	#iteratively get the intersection of n, n-1, n-2 search terms...etc
	while count>0:
		intersec=list(set.intersection(*map(set, r6)))
		intersec.sort()
		for element in intersec:
			if not element in answer4:
				answer4.append(element)

		r6.remove(r6[count])
		count=count-1

	
	#Retrieve original result list again 
	#------------------------------------------------------------
	search_list=re.split('\W+',keyword)

	if '' in search_list:
		search_list.remove('')

	result_dict={}

	for i in range(len(search_list)):
		search_term='"'+search_list[i]+'"'

		#Define the query and desired range of output as a variables
		payload = {'orderBy':'"$key"','equalTo': search_term}

		#Get result from firebase
		r = requests.get('https://dsci551-hw1-c8674-default-rtdb.firebaseio.com/keyword_index/.json', params=payload)
		r=r.json()

		search_term=search_term.replace('"','')

		result=list(r[search_term])

		result.sort()

		result_dict[search_term]=result

		finalresult=(list(result_dict.values()))

	
	#Populate final answer sorted by car names common across all search terms followed by first term....etc
	#--------------------------------------------------------------------------------------------------------

	for sublist in finalresult:
		for elem in sublist:
			if not elem in answer4:
				answer4.append(elem)
	if not answer4==[]:
		print(f"IDs for the car are: {answer4}")

	else:
		print("no card found")











	



if __name__ == "__main__":
    keyword = sys.argv[1]
    searchcar(keyword)


	