class Record():
    def __init__(self, artist, title, year):
        self.artist = artist
        self.title = title
        self.year = year

    def printRecord(self):
        print("Artist:", self.artist, ", Title:", self.title, ", Year:", self.year)

# Creating records to the Record class
fiender_ar_trakigt = Record("Veronica Maggio", "Fiender är tråkigt", 2019)
tim = Record("Avicii", "Tim", 2019)
kent = Record("kent", "kent", 1995)
verkligen = Record("kent", "Verkligen", 1996)
illusioner = Record("Håkan Hellström", "Illusioner", 2018)

# Printing out the records to the terminal
fiender_ar_trakigt.printRecord()
tim.printRecord()
kent.printRecord()
verkligen.printRecord()
illusioner.printRecord()