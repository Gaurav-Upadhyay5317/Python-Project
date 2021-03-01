"""
Name: Gaurav Sanjiv Upadhyay

Program: To know your starsign using your birthdate.


How to run this program:
python3 Assignment1_SMDM.py

"""

# Using OS library to use the system information. 
from os import system, name

# Created Screen clear function to clear the output screen
def Clear_screen(): 
  
    # For Windows OS
    if name == 'nt': 
        _ = system('cls') 
    # For Mac/Linux OS 
    else: 
        _ = system('clear')

class Starsign_Display(object):
	"""
	Created a class name Starsign_Display which is sued to display the information 
	related to different starsigns.

	"""

	def __init__(self, name, element, ruler, compatibility, luckynum, show_date):
		# Constructor function used to initialize the variables.
		self.name = name
		self.element = element
		self.ruler = ruler
		self.compatibility = compatibility
		self.luckynum = luckynum
		self.show_date = show_date
#		self.Reset_Seats()
		super(Starsign_Display, self).__init__()

	def Starsign_info(self):
		# Starsign_info method to show information related to a particular starsign.
		print ("Name : %s" %  self.name)
		print ("Element : %s" %  self.element)
		print("Ruler : %s" % self.ruler)
		print("Greatest Overall Compatibility : %s" % self.compatibility)
		print ("Lucky Numbers: %d" %  self.luckynum)
		print ("Date range: %s\n" %  self.show_date)
		Answer = input("Would you like to see your starsign (Y/N)?\n")
		Answer = Answer[0].lower()
		
		if(Answer == 'y'):
			my_function()



		# List Comprehension to display all the starsigns
		Starsign = ["Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn"]
def my_function():
	day = int(input("Input birthday: "))
	month = input("Input month of birth (e.g. march, july etc): ")
	if month == 'december':
				astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
				print("Your Astrological sign is :",astro_sign)
	elif month == 'january':
				astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
				print("Your Astrological sign is :",astro_sign)
	elif month == 'february':
				astro_sign = 'Aquarius' if (day < 19) else 'pisces'
				print("Your Astrological sign is :",astro_sign)
	elif month == 'march':
				astro_sign = 'Pisces' if (day < 21) else 'aries'
				print("Your Astrological sign is :",astro_sign)
	elif month == 'april':
				astro_sign = 'Aries' if (day < 20) else 'taurus'
				print("Your Astrological sign is :",astro_sign)
	elif month == 'may':
				astro_sign = 'Taurus' if (day < 21) else 'gemini'
				print("Your Astrological sign is :",astro_sign)
	elif month == 'june':
				astro_sign = 'Gemini' if (day < 21) else 'cancer'
				print("Your Astrological sign is :",astro_sign)
	elif month == 'july':
				astro_sign = 'Cancer' if (day < 23) else 'leo'
				print("Your Astrological sign is :",astro_sign)
	elif month == 'august':
				astro_sign = 'Leo' if (day < 23) else 'virgo'
				print("Your Astrological sign is :",astro_sign)
	elif month == 'september':
				astro_sign = 'Virgo' if (day < 23) else 'libra'
				print("Your Astrological sign is :",astro_sign)
	elif month == 'october':
				astro_sign = 'Libra' if (day < 23) else 'scorpio'
				print("Your Astrological sign is :",astro_sign)
	elif month == 'november':
				astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
				print("Your Astrological sign is :",astro_sign)

	Answer = input("\nWould you like to know more about your starsign (Y/N)?\n")
			# This will handle user input cases e.g Yes, Y, yes, YES, No, N, no, n
	Answer = Answer[0].lower()
	if(Answer == 'y'):
				showstarsigns(all_starsigns)
	elif(Answer == 'n'):
				print("Thankyou...")
	elif (Answer != 'n'):
				print ("You entered an invalid option....Please Try Again.")
	'''elif(Answer == 'n'):
			print("Thankyou...")		
		elif (Answer != 'n'):
			print ("You entered an invalid option....Please Try Again.")'''

def showstarsigns(all_starsigns):
	# This method shows list of all the starsigns and ask user, if he wants to know more deatils about a particular starsign.
	i = 1
	print(" ")
	for key in all_starsigns:
		print ("%d. %s" % (i, all_starsigns[key].name))
		i += 1
	Answer = input ("\nEnter your Starsign number to know more else press q to exit.\n")

	# Try catch to handle out of range input
	try:
		if Answer == 'q':
			return
		Answer = int(Answer)
		if 0 < Answer <= len(all_starsigns.keys()):
			all_starsigns[list(all_starsigns.keys())[Answer-1]].Starsign_info()
		else:
			raise ValueError()
	except ValueError:
		Clear_screen()
		print ("Invalid option. Please try again.")
		showstarsigns(all_starsigns)

def main(all_starsigns):
	# Main method to display different options available.
	Answer = ''
	while (Answer == ''):
		Clear_screen()
		print ("\n\n_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-Know Your Starsign_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
		print ("\n--------Select from the following options--------\n")
		print ("        1. Know your Starsign")
		print ("        2. List all the starsigns.")
		print ("\n----Press Q to quit and Thank you, have a good day!!---- ")

		Answer = input()
		Answer = Answer[0].lower()
		
		if (Answer == '1'):
			my_function()

		elif (Answer == '2'):
			# Create dictonary using dictonary comprehension.
			showstarsigns(all_starsigns)
			

if __name__ == '__main__':
	# Init function that is used for adding and deleting all_starsigns.
	all_starsigns = {
		'1': Starsign_Display("Aquarius", "Air" , "Uranus, Saturn", "Leo, Sagittaruis", 4, " January 20 - February 18"),
		'2': Starsign_Display("Pisces", "Water", "Neptune, Jupiter", "Virgo, Taurus", 3, "February 19 - March 20"),
		'3': Starsign_Display("Aries", "Fire", "Mars", "Libra, Leo", 1, "March 21 - April 19"),
		'4': Starsign_Display("Taurus", "Earth", "Venus", "Scorpio, Cancer", 2, "April 20 - May 20"),
		'5': Starsign_Display("Gemini",  "Air", "Mercury", "Sagittarius, Aquaruis", 5, "May 21 - June 20"),
		'6': Starsign_Display("Cancer", "Water", "Moon", "Capricorn, Taurus", 3, "June 21 - July 22"),
		'7': Starsign_Display("Leo", "Fire", "Sun", "Aquarius, Gemini", 10, "July 23 - August 22"),
		'8': Starsign_Display("Virgo", "Earth", "Mercury", "Pisces, Cancer", 14, "August 23 – September 22"),
		'9': Starsign_Display("Libra", "Air", "Venus", "Aries, Sagittarius", 6, "September 23- OCtober 22"),
		'10': Starsign_Display("Scorpio", "Water", "Pluto", "Taurus, Cancer", 8, "October 23 - November 21"),
		'11': Starsign_Display("Sagittarius",  "Fire", "Jupiter", "Gemini, Aries", 7, "November 22- December 21"),
		'12': Starsign_Display("Capricon",  "Earth", "Saturn", "Taurus, Cancer", 13, "December 22- January 19"),
	}
	main(all_starsigns)

	
