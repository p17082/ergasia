# coding=utf-8

myInt = int(raw_input("Enter a number: "))
numsInRoman = ""

# Αριθμοί και τα αντίστοιχα λατινικά γράμματα
ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')

# Για κάθε αριθμό έλεγξε πόσα γράμματα αντιστοιχούν
for i in range(len(ints)):
	count = int(myInt / ints[i])
	numsInRoman += nums[i] * count
	myInt -= ints[i] * count

# Τύπωσε τον τελικό λατινικό αριθμό
print numsInRoman

# Τέλος προγράμματος
raw_input("Press enter to exit....")