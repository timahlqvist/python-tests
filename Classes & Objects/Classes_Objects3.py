class Person():
    def __init__(self, name, age, serviceUsing):
        self.name = name
        self.age = age
        self.serviceUsing = serviceUsing

    def personInformation(self):
        print("Name:", self.name, ", Age:", self.age, ", Using streaming service:", self.serviceUsing)

class Service():
    def __init__(self, name):
        self.name = name

# Creating three streaming services to the Service class
spotify = Service("Spotify")
googleMusic = Service("Google Music")
itunes = Service("ITunes")

# Creating three persons to the Person class
tim = Person("Tim Ahlqvist", 15, spotify.name)
gustav = Person("Gustav Pettersson", 37, itunes.name)
nils = Person("Nils Nilsson", 10, googleMusic.name)

# Print the information about each person
tim.personInformation()
gustav.personInformation()
nils.personInformation()