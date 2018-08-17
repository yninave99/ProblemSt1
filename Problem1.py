import time

def logData(data):
	'''Load User logs into three different files in three different formats respectively'''
	try:
		print ("Data Loading!!! Please Wait...")
		time.sleep(5)

		with open('file1.txt', 'a') as fp:
			for items in data:
				fp.writelines("   |   ".join([items[4],items[2],items[0],items[1],"\n"]))
			fp.close()

		with open('file2.txt', 'a') as fp:
			for items in data:
				fp.writelines("   |   ".join([str(int(int(items[2])//int(items[3]))),items[4],"\n"]))
			fp.close()

		with open('file3.txt', 'a') as fp:
			for items in data:
				fp.writelines("   |   ".join([items[0],items[1],items[2],items[3],items[4],"\n"]))
			fp.close()
		print ("\n\n\nData Logged Successfully!!!")

	except Exception as e:
		print ("Log Data Failed!!!")
		print(e.args)

	return()


# Execute code only from command line.
if __name__ == "__main__":
	'''Program Starts Here'''
	print ("***************** WELCOME **************")

	#Hold Person Records
	personRecord = []

	#Provide Command Line input
	inputStr = input("***************** M E N U **************\nEnter Data : FirstName(String),LastName(String),Experience(Months),Age(Years),Organization(String)\nEnter Keyword: SORT\nEnter Keyword: Exit\n")

	while(1):
		#Sort User Input
		if inputStr.upper() == "SORT":
			if (len(personRecord) == 0):
				print ("\n\n\nNo Data Entered!!!")
			else:
				personRecord = sorted(personRecord, key=lambda x: x[0])
				logData(personRecord)
		#Exit Program
		elif inputStr.upper() == "EXIT":
			print ("Thanks for Using Me :)")
			exit()
		#Collect User Input
		elif len(inputStr.split(',')) == 5:
			personRecordList = inputStr.split(',')
			print (personRecordList)
			if personRecordList[2].strip().isdigit() and personRecordList[3].strip().isdigit():
				personRecord.append((tuple(inputStr.split(','))))
			else:
				print ("\n\n\n*********************Please Provide the Proper Input!!!***********************\n")
		#Improper Input
		else:
			print ("\n\n\n*********************Please Provide the Proper Input!!!***********************\n")
		inputStr = input("***************** M E N U **************\nEnter Data : FirstName(String),LastName(String),Experience(Months),Age(Years),Organization(String)\nEnter Keyword: SORT\nEnter Keyword: Exit\n")