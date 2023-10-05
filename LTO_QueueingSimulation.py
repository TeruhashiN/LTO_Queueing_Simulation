import random
import time


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Percentage = (Number / Total) x 100

# Student Permit – 30 to 50  = 20%
# Renewal – 80 to 100; = 40%
# Examination – 50 to 70  = 28%
# Miscellaneous – 20 to 30 = 12%

# total = 250
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# The average LTO applicants per day is around 200 - 250
applicants = random.randint(200, 250)

def PlacePACD():
    # Consume atleast 30 secs per person however there's a queueing
    # Formula Total Time in MINUTES = (Number of People) x (Time per Person in seconds) / 60
    # Total Time in HOURS = MINUTES / 60

    PACD_total_minutes = applicants * 30 / 60
    PACD_total_hours = PACD_total_minutes / 60

    PACD_TimeConsume = (PACD_total_hours / float(PACD))  #By adding more PACD it will divide the time depending on how many they set up
    print(PACD_TimeConsume)



def PlacePortal():
    # Consume atleast 1 minute and 30 secs per person = 90 secs
    portal_total_minutes = applicants * 90 / 60
    portal_total_hours = portal_total_minutes / 60

    portal_TimeConsume = (portal_total_hours / float(Portal))
    print(portal_TimeConsume)


def PlaceCashier():
    #consume atleast 1 minute per person = 60 secs
    Cashier_total_minutes = applicants * 60 / 60
    Cashier_total_hours = Cashier_total_minutes / 60

    Cashier_TimeConsume = (Cashier_total_hours / float(Cashier))
    print(Cashier_TimeConsume)












# Item to be added
PACD = input("Type the number of PACD to be added: ")
Portal = input("Type the number of Portal to be added: ")
Cashier = input("Type the number of Cashier to be added: ")
Computer = input("Type the number of Computer to be added: ")
Biometric = input("Type the number of Biometric to be added: ")




PlacePACD()
PlacePortal()
PlaceCashier()



