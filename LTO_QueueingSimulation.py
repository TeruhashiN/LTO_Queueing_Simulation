import random
import time


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Percentage = (Number / Total) x 100

# Student Permit – 30 to 50  = 20% Yellow Card
# Renewal + Examination – 80 to 100; = 40% Blue Card
# NonPro + Examination – 50 to 70  = 28% Green Card
# Miscellaneous – 20 to 30 = 12% Orange Card

# total = 250
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# The average LTO applicants per day is around 200 - 250
applicants = random.randint(200, 250)

# Total Average of Applicant in seperate Licensing queueing
yellow_card = applicants * 0.2
blue_card = applicants * 0.4
green_card = applicants * 0.28
orange_card = applicants * 0.12


print("Total Student Permit Applicants: ", int(yellow_card))
print("Total Renewal Applicants: ", int(blue_card))
print("Total Non Professional License Applicants: ", int(green_card))
print("Total Mischellaneous Applicants: ", int(orange_card))
print("Total Applicants for the day: ", int(applicants))
print("")


def PlacePACD():
    # Consume atleast 30 secs per person however there's a queueing
    # Formula Total Time in MINUTES = (Number of People) x (Time per Person in seconds) / 60
    # Total Time in HOURS = MINUTES / 60

    PACD_total_minutes = applicants * 30 / 60
    PACD_total_hours = PACD_total_minutes / 60

    PACD_TimeConsume = (PACD_total_hours / 2 + float(PACD))  #By adding more PACD it will divide the time depending on how many they set up
    print("Total PACD Time (in hours):", PACD_TimeConsume)



def PlacePortal():
    # Consume atleast 1 minute per person = 60 secs
    portal_total_minutes = applicants * 60 / 60
    portal_total_hours = portal_total_minutes / 60

    portal_TimeConsume = (portal_total_hours / float(Portal))
    print("Total Portal Time (in hours):", portal_TimeConsume)


def PlaceCashier():
    #consume atleast 1 minute per person = 60 secs
    Cashier_total_minutes = applicants * 60 / 60
    Cashier_total_hours = Cashier_total_minutes / 60

    Cashier_TimeConsume = (Cashier_total_hours / float(Cashier))
    print("Total Accounting Time (in hours):",Cashier_TimeConsume)


def PlaceComputer():
    # Define the range for time allocation (10 minutes to 1 hour in seconds)
    min_time = 10 * 60
    max_time = 60 * 60

    # Define the number of blue card and green card applicants
    blue_card_count = int(blue_card)
    green_card_count = int(green_card)

    # Initialize variables to store the total times for blue card and green card applicants
    total_blue_card_time = 0
    total_green_card_time = 0

    # Generate random times for blue card applicants and calculate the total time
    for _ in range(blue_card_count):
        time_allocated = random.randint(min_time, max_time)
        total_blue_card_time += time_allocated

    # Generate random times for green card applicants and calculate the total time
    for _ in range(green_card_count):
        time_allocated = random.randint(min_time, max_time)
        total_green_card_time += time_allocated

    # Convert the total times from seconds to minutes
    total_both_card_time_minutes = (total_blue_card_time + total_green_card_time) / 60
    total_both_card_time_hours = total_both_card_time_minutes /  60

    ExaminationTimeConsume = total_both_card_time_hours / 7 + float(Computer)

    print("Total Blue & Green Card Time (in hours):", ExaminationTimeConsume)









# Item to be added
PACD = input("Type the number of PACD to be added: ")
Portal = input("Type the number of Portal to be added: ")
Cashier = input("Type the number of Cashier to be added: ")
Computer = input("Type the number of Computer to be added: ")
Biometric = input("Type the number of Biometric to be added: ")


print("")

PlacePACD()
PlacePortal()
PlaceCashier()
PlaceComputer()



