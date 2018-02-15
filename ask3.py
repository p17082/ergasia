# coding=utf-8

# Συνάρτηση αν το γράμμα είναι κεφαλαίο
def rot13Upper( char ):
	return chr((ord(char) - 78) % (90 - 65 + 1) + 65)

# Συνάρτηση αν το γράμμα είναι πεζό
def rot13Lower( char ):
	return chr((ord(x) - 110) % (122 - 97 + 1) + 97)

# String του χρήστη
myString = raw_input("Enter a string: ")

# Αρχικοποίηση του κωδικοποιημένου string
rot13String = ""


for x in myString:
	# Έλεγξε αν το γράμμα είναι κεφαλαίο ή πεζό (ASCII) και κάλεσε
	# την αντίστοιχη συνάρτηση
	if(ord(x) >= 65 and ord(x) <= 90):
		rot13String += rot13Upper(x)
	elif(ord(x) >= 97 and ord(x) <= 122):
		rot13String += rot13Lower(x)
	else:
		rot13String += x

# Τύπωσε το κωδικοποιημένο string 
print rot13String

# Τέλος προγράμματος
raw_input("Press enter to exit...")