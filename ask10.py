# encoding=UTF-8

import sys
import string
from random import randint

filename = raw_input("Enter the file's name: ")
filename += ".txt"

# Άνοιγμα αρχείου και έλεγχος
try:
	file = open(filename, 'r')
except IOError:
	print "Could not find file!"
	raw_input("Press enter to exit...")
	sys.exit()

wordList = []

# Αντικατάσταση των σημείων στίξης με το κενό
wordList = file.read().translate(None, string.punctuation)

# Διαχωρισμός των προτάσεων σε ξεχωριστές λέξεις
wordList = wordList.split()

# Έλεγχος λέξεων σε περίπτωση που περιέχουν κεφαλαία γράμματα
for word in wordList:
	if(any(x.isupper() for x in word)):
		wordList.remove(word)

triplets = []

# Σχηματισμός τριάδων
for x in range(len(wordList) - 2):
	triplets.append([wordList[x], wordList[x + 1], wordList[x + 2]])
	# print str(x) + " Triplet: " +  triplets[x][0] + " " + triplets[x][1] + "  " + triplets[x][2]

# Επιλογή αρχικής τριάδας
keyTriplet = triplets[randint(0, len(triplets) - 1)]

matching = []

# Τριάδες που ταιριάζουν βάσει κανόνα
for check in range(len(triplets)):
	if(keyTriplet[1] == triplets[check][0] and
		keyTriplet[2] == triplets[check][1]):
		matching.append(triplets[check])


freqMap = []

# Μέτρηση εμφανίσεων κάθε τριάδας
for key in range(len(matching)):
	duplicate = False
	
	# Σε περίπτωση που έχουμε ξαναελέγξει την ίδια τριάδα 
	for x in range(len(freqMap)):
			for y in range(1, len(freqMap[x])):
				if(key == freqMap[x][y]):
					duplicate = True
					duplicateIndex = x
	
	# Έλεγχος για ίδιες τριάδες
	for check in range(len(matching)):
		if(matching[key] == matching[check] and not duplicate):
			try:
				freqMap[key][0] += 1
				freqMap[key].extend([check])
			except IndexError:
				freqMap.append([1])
				freqMap[key].extend([check])

output = ""

# Εισαγωγή πρώτης τριάδας στο τελικό κείμενο
for word in keyTriplet:
	output += word + " "

# Εισαγωγή υπολοίπων τριάδων στο τελικό κείμενο
# έτσι ώστε να περιέχει περίπου 200 λέξεις (3 * 67 = 201)
for x in range(67):
	freqIndex = x % len(freqMap)

	if(freqMap[freqIndex] == 1):
		for word in matching[freqMap[freqIndex][1]]:
			output += word + " "

	# Σε περίπτωση που μια τριάδα έχει πολλές εμφανίσεις
	# διάλεξε μια τυχαία
	else:
		randomDuplicate = randint(1, len(freqMap[freqIndex]) - 1)

		for word in matching[freqMap[freqIndex][randomDuplicate]]:
			output += word + " "

print "Output: "
print output

# Κλείσιμο αρχείου
file.close()

# Τέλος προγράμματος
raw_input("Press enter to exit...")