import re
import os
from shutil import copyfile

class Operation:

	pics_dir = os.getcwd() + "\pics" # Create the pics folder location
	pics_list = os.listdir(pics_dir)

	def findYear(self, file_name):
		year = re.findall(r'[IV][MI][GD]_\d\d\d\d', file_name)
		if year:
			year = re.sub(r'[IV][MI][GD]_', '', year[0])
			return year

	def findMonth(self, file_name):
		month = re.findall(r'[IV][MI][GD]_\d\d\d\d\d\d', file_name)
		if month:
			month = re.sub(r'[IV][MI][GD]_\d\d\d\d', '', month[0])
			return month

	def findFileType(self, file_name):
		file_type = re.findall(r'\.\w+\Z', file_name)
		if file_type:
			return file_type[0]

	def yearExists(self, year):
		year_exsists = os.path.isdir(self.pics_dir + "\\" + year)
		if year_exsists is False:
			os.mkdir(self.pics_dir + "\\" + year)

	def monthExists(self, year, month):
		month_exsists = os.path.isdir(self.pics_dir + "\\" + year + "\\" + month)
		dest_dir = self.pics_dir + "\\" + year + "\\" + month
		if month_exsists is False:
			os.mkdir(dest_dir)
		return dest_dir

	def move_file(self, fileName, dest_dir):
		copyfile(self.pics_dir + "\\" + fileName, dest_dir + "\\" + fileName )
		print("File %s has been copied" % fileName)

	def run(self):		
		for fileName in self.pics_list: #Loop trough pics_list		
			file_type = self.findFileType(fileName) #Check if file type is jpg or .mp4

			if file_type == ".jpg" or file_type == ".mp4":
				year = self.findYear(fileName) #Find year and month
				month = self.findMonth(fileName)
				self.yearExists(year) 
				dest_dir = self.monthExists(year, month) #Create month folder if does not exist
				self.move_file(fileName, dest_dir) #Move file to new folder

if __name__ == "__main__":
    Operation().run()


