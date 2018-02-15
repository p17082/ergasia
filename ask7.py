# coding=utf-8

from datetime import datetime, date, timedelta

# Συνάρτηση που επιστρέφει την διαφορά σε μέρες
# μεταξύ δύο ημερομηνιών
def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)


# Πληροφορίες για την σημερινή μέρα
currentDay = datetime.today().strftime("%a")
currentYear = datetime.today().year
currentMonth = datetime.today().month
currentDate = int(datetime.today().strftime("%d"))

# Μετρητής ημερών
numberOfDays = 0

# Το εύρος των ημερωμηνιών που κοιτάμε
start_date = date(int(currentYear), int(currentMonth), currentDate)
end_date = date(int(currentYear) + 10, int(currentMonth), currentDate)

for x in daterange(start_date, end_date):
	myDate = x
	# Debug purposes - All iterated days
	# print x
	if (myDate.strftime("%a") == currentDay and int(myDate.strftime("%d")) == currentDate):
			numberOfDays += 1
			# Debug purposes - All matching days
			# print str(numberOfDays) + " " + myDate.strftime("%A %B %Y")

print "Number of " + datetime.today().strftime("%A") + "s the next 10 years that match today's date: " + str(numberOfDays)

# Τέλος προγράμματος
raw_input("Press enter to exit....")