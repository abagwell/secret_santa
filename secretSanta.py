#This script is for python3
import random

class Player:
	"""This class will be used to instantiate actual participants"""
	
	def __init__(self, name, familyNum):
		self.name = name
		self.family = familyNum

def main():

    debugger = False
    
    participantList = []
    familyCounter = 1
    trap = True

    userInput = input("Enter the number of families playing Secret Santa: ")
    totalFamilies= int(userInput)

    if totalFamilies < 2:
    	print("You can't play secret santa with just 1 person!")
    	return

    while familyCounter <= totalFamilies:

    	userInput = input("List the members of a family - " + str(familyCounter) + ": ")
    	family = userInput.split(",")
    	
    	for member in family:
    		player = Player(member, familyCounter)
    		participantList.append(player)

    	familyCounter += 1

    #begin assigning people by drawing random indices from the array, if the person matches with family member, draw again

    if len(participantList) % 2 != 0:
    	print("Family distribution is imbalanced. Invite more families to redistribute!")
    	return

    print (len(participantList))  

    used = []
    partners = []

    
    while len(used) < len(participantList):
    	
    	draw1 = random.randint(0, len(participantList) -1)
    	draw2 = random.randint(0, len(participantList) -1)

    	if draw1 in used:
    		continue

    	if draw2 in used:
    		continue

    	if participantList[draw1].family == participantList[draw2].family:
    		continue

    	used.append(draw1)
    	used.append(draw2)
    	partners.append((participantList[draw1].name, participantList[draw2].name))

    print (partners)
    return 

#point of entry for script

if __name__ == "__main__":
	main()
