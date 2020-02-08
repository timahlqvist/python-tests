class Record():
    def __init__(self, artist, title, year):
        self.artist = artist
        self.title = title
        self.year = year

    def printRecord(self):
        print("Artist:", self.artist, ", Title:", self.title, ", Year", self.year)

# Register a record
artist = input("Please type in artist: ")
title = input("Please type in title: ")
year = input("Please type in year: ")

#Creating an object with the information that the user inputed
record1 = Record(artist, title, year)

#Prints the record that the user registered
record1.printRecord()