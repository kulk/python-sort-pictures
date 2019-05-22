import re
import os
import shutil

class Collection:

	def __init__(self, file_name, year, month):
		self.file_name = file_name
		self.year = year
		self.month = month

class Operation:

	pics_dir = os.getcwd() + "\pics" # Create the pics folder location
	pics_list = os.listdir(pics_dir)
	
	def __init__(self):
		self.file_list = []

	def findYear(self, file_name):
		year = re.findall(r'IMG_\d\d\d\d', file_name)
		year = year[0].replace('IMG_', '')
		return year

	def findMonth(self, file_name):
		month = re.findall(r'IMG_\d\d\d\d\d\d', file_name)
		month = re.sub('IMG_\d\d\d\d', '', month[0])
		return month

	def findFileType(self, file_name):
		file_type = re.findall(r'\.\w+\Z', file_name)
		return file_type

	def yearExists():

	def monthExists():
		pass

	def move_file():
		pass

	def engine(self, pics_list):
		pass
		#Check if pics_dir exists

		#Loop trough pics_list

		#Check the file type

		#Go to next item if file is not .jpg or .mp4

		#Find year and month

		#Check if year folder exists, if not create one (method)

		#Check if month folder exists, if not create one (method)

		#Move file to new folder (method)

'''
	def isJpg(self, file_name):
		#Don't need this
		jpg = re.search('.jpg', file_name)
		if(jpg):
			is_jpg =  True
		else:
			is_jpg = False
		return is_jpg

	def addToCollectionList(self, file_name):
		# Why do I need this?
		year = self.findYear(file_name)
		month = self.findMonth(file_name)
		new_collection = Collection(file_name, year, month)
		self.file_list.append(new_collection)
'''

x = Operation()
x.engine(x.pics_list)


'''
pics_dir = os.getcwd() + "\pics"

test_folder = pics_dir + "\\test"
test_file = pics_dir + "\IMG_20170713_134922359.txt"
print(test_file)
print(test_folder)

shutil.copy(test_file, test_folder)
'''
