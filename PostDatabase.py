from pymongo import MongoClient
from datetime import datetime

class PostDatabase():
	monthLookup = dict([('Jan', 1), ('Feb', 2), ('Mar', 3), ('Apr', 4), ('May', 5), ('Jun', 6), ('Jul', 7), ('Aug', 8), ('Sep', 9), ('Oct', 10), ('Nov', 11), ('Dec', 12)])

	def __init__(self):
		self.client = MongoClient()
		self.db = self.client.entries

		

	def makePost(self, userIn, username, maxPeople):
		location = userIn['Location']
		description = userIn['Description']
		title = userIn['Title']
		time = userIn['Time']
		location = location.split()
		latitude = location[1][0:len(location[1]) - 1]
		latitude = float(latitude)
		longitude = location[3][0:len(location[3]) - 1]
		longitude = float(longitude)
		dateInfo = time.split()
		date = datetime(int(dateInfo[2]), self.monthLookup[dateInfo[0]], int(dateInfo[1][0:len(dateInfo[1]) - 1]), int(dateInfo[3][0:1]), int(dateInfo[3][3:4]))
		result = self.db.entries.insert_one(
    	{
        	"longitude": longitude,
        	"latitude": latitude,
        	"description": description, 
        	"time": date,
        	"title": title,
        	"user": username,
        	"maxPeople": maxPeople,
    	}
		)








		