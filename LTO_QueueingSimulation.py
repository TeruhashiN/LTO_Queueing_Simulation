import random
import time


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Percentage = (Number / Total) x 100

# Student Permit – 30 to 50  = 34% Yellow Card
# Renewal + Examination – 30 to 40; = 28% Blue Card
# NonPro + Examination – 25 to 35  = 24% Green Card
# Miscellaneous – 10 to 20 = 14% Orange Card

# total = 145
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# The average LTO applicants per day is around 95 - 145
applicants = random.randint(95, 145)

# Total Average of Applicant in seperate Licensing queueing
yellow_card = applicants * 0.34
blue_card = applicants * 0.28
green_card = applicants * 0.24
orange_card = applicants * 0.14


print("Total Student Permit Applicants: ", int(yellow_card))
print("Total Renewal Applicants: ", int(blue_card))
print("Total Non Professional License Applicants: ", int(green_card))
print("Total Mischellaneous Applicants: ", int(orange_card))
print("Total Applicants for the day: ", int(applicants))
print("")


def PlacePACD():
    total_time_minutes = 0
    total_time_hours = 0
    individual_times = []

    for _ in range(applicants):
        PACD_time_avg = random.randint(30, 60)
        PACD_total_minutes = PACD_time_avg / 60
        total_time_minutes += PACD_total_minutes
        individual_times.append(PACD_time_avg)

    PACD_total_time_hours = total_time_minutes / 60

    try:
        PACD_TimeConsume = PACD_total_time_hours / (2 + float(PACD))

        # Convert PACD_TimeConsume into hours and minutes
        hours = int(PACD_TimeConsume)
        minutes = int((PACD_TimeConsume - hours) * 60)

        print("Total PACD Time: {} hours and {} minutes".format(hours, minutes))

        # Print individual times
        for i, time_avg in enumerate(individual_times, 1):
            individual_seconds = time_avg
            individual_minutes = individual_seconds // 60
            individual_seconds = individual_seconds % 60

            #print each individual timeframe
            # print("Applicant {}: {} seconds ({} minutes and {} seconds)".format(i, time_avg, individual_minutes, individual_seconds))

    except ValueError:
        PACD_TimeConsume = PACD_total_time_hours / 2

        # Convert PACD_TimeConsume into hours and minutes
        hours = int(PACD_TimeConsume)
        minutes = int((PACD_TimeConsume - hours) * 60)

        print("Total PACD Time: {} hours and {} minutes".format(hours, minutes))

    except ZeroDivisionError:
        PACD_TimeConsume = PACD_total_time_hours / 2

        # Convert PACD_TimeConsume into hours and minutes
        hours = int(PACD_TimeConsume)
        minutes = int((PACD_TimeConsume - hours) * 60)

        print("Total PACD Time: {} hours and {} minutes".format(hours, minutes))


def PlacePortal():
    total_time_minutes = 0
    total_time_hours = 0
    individual_times = []

    for _ in range(applicants):
        PORTAL_time_avg = random.randint(60, 90)
        PORTAL_total_minutes = PORTAL_time_avg / 60
        total_time_minutes += PORTAL_total_minutes
        individual_times.append(PORTAL_time_avg)

    PORTAL_total_time_hours = total_time_minutes / 60

    try:
        Portal_TimeConsume = (PORTAL_total_time_hours / float(Portal))

        # Convert Portal_TimeConsume into hours and minutes
        hours = int(Portal_TimeConsume)
        minutes = int((Portal_TimeConsume - hours) * 60)

        print("Total Portal Time: {} hours and {} minutes".format(hours, minutes))

        # Print individual times
        for i, time_avg in enumerate(individual_times, 1):
            individual_seconds = time_avg
            individual_minutes = individual_seconds // 60
            individual_seconds = individual_seconds % 60


            #Print each individual TimeFrame
            # print("Applicant {}: {} seconds ({} minutes and {} seconds)".format(i, time_avg, individual_minutes,individual_seconds))

    except ValueError:
        Portal_TimeConsume = (PORTAL_total_time_hours / 1)

        # Convert Portal_TimeConsume into hours and minutes
        hours = int(Portal_TimeConsume)
        minutes = int((Portal_TimeConsume - hours) * 60)

        print("Total Portal Time: {} hours and {} minutes".format(hours, minutes))

    except ZeroDivisionError:
        Portal_TimeConsume = (PORTAL_total_time_hours / 1)

        # Convert Portal_TimeConsume into hours and minutes
        hours = int(Portal_TimeConsume)
        minutes = int((Portal_TimeConsume - hours) * 60)

        print("Total Portal Time: {} hours and {} minutes".format(hours, minutes))


def PlaceCashier():
    total_time_minutes = 0
    total_time_hours = 0
    individual_times = []

    for _ in range(applicants):
        CASHIER_time_avg = random.randint(40, 80)  #consume atleast 40secs to 1min and 20secs individual
        CASHIER_total_minutes = CASHIER_time_avg / 60
        total_time_minutes += CASHIER_total_minutes
        individual_times.append(CASHIER_time_avg)

    CASHIER_total_time_hours = total_time_minutes / 60


    try:
        Cashier_TimeConsume = (CASHIER_total_time_hours/ float(Cashier))

        # Convert Cashier_TimeConsume into hours and minutes
        hours = int(Cashier_TimeConsume)
        minutes = int((Cashier_TimeConsume - hours) * 60)

        print("Total Cashier Time: {} hours and {} minutes".format(hours, minutes))

        # Print individual times
        for i, time_avg in enumerate(individual_times, 1):
            individual_seconds = time_avg
            individual_minutes = individual_seconds // 60
            individual_seconds = individual_seconds % 60
            # print("Applicant {}: {} seconds ({} minutes and {} seconds)".format(i, time_avg, individual_minutes, individual_seconds))


    except ValueError:
        Cashier_TimeConsume = (CASHIER_total_time_hours / 1)

        # Convert Cashier_TimeConsume into hours and minutes
        hours = int(Cashier_TimeConsume)
        minutes = int((Cashier_TimeConsume - hours) * 60)

        print("Total Cashier Time: {} hours and {} minutes".format(hours, minutes))

    except ZeroDivisionError:
        Cashier_TimeConsume = (CASHIER_total_time_hours / 1)

        # Convert Cashier_TimeConsume into hours and minutes
        hours = int(Cashier_TimeConsume)
        minutes = int((Cashier_TimeConsume - hours) * 60)

        print("Total Cashier Time: {} hours and {} minutes".format(hours, minutes))


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
        total_blue_card_time += time_allocated / 7   # to be fixed

    # Generate random times for green card applicants and calculate the total time
    for _ in range(green_card_count):
        time_allocated = random.randint(min_time, max_time)
        total_green_card_time += time_allocated / 7    # to be fixed

    # Convert the total times from seconds to minutes
    total_both_card_time_minutes = (total_blue_card_time + total_green_card_time) / 60
    total_both_card_time_hours = total_both_card_time_minutes / 60


    try:
        ExaminationTimeConsume = total_both_card_time_hours / (7 + float(Computer))

        # Convert Examination_TimeConsume into hours and minutes
        hours = int(ExaminationTimeConsume)
        minutes = int((ExaminationTimeConsume - hours) * 60)

        print("Total Examation Time: {} hours and {} minutes".format(hours, minutes))

    except ValueError:
        ExaminationTimeConsume = total_both_card_time_hours / 7

        # Convert Examination_TimeConsume into hours and minutes
        hours = int(ExaminationTimeConsume)
        minutes = int((ExaminationTimeConsume - hours) * 60)

        print("Total Examation Time: {} hours and {} minutes".format(hours, minutes))

    except ZeroDivisionError:
        ExaminationTimeConsume = total_both_card_time_hours / 7

        # Convert Examination_TimeConsume into hours and minutes
        hours = int(ExaminationTimeConsume)
        minutes = int((ExaminationTimeConsume - hours) * 60)

        print("Total Examation Time: {} hours and {} minutes".format(hours, minutes))


# To be fixed Dapat sa random ppl first 7 ang makaka accomodate ng room



def PlaceBiometric():
    # Consume at least 40 seconds per person; however, there's a queuing
    # Formula Total Time in MINUTES = (Number of People) x (Time per Person in seconds) / 60
    # Total Time in HOURS = MINUTES / 60

    Biometric_total_minutes = applicants * 40 / 60
    Biometric_total_hours = Biometric_total_minutes / 60

    try:
        Biometric_TimeConsume = (Biometric_total_hours / float(Biometric))


        # Convert PACD_TimeConsume into hours and minutes
        hours = int(Biometric_TimeConsume)
        minutes = int((Biometric_TimeConsume - hours) * 60)

        print("Total Biometric Time: {} hours and {} minutes".format(hours, minutes))


    except ValueError:
        Biometric_TimeConsume = (Biometric_total_hours / 1)

        # Convert PACD_TimeConsume into hours and minutes
        hours = int(Biometric_TimeConsume)
        minutes = int((Biometric_TimeConsume - hours) * 60)

        print("Total Biometric Time: {} hours and {} minutes".format(hours, minutes))

    except ZeroDivisionError:
        Biometric_TimeConsume = (Biometric_total_hours / 1)

        # Convert PACD_TimeConsume into hours and minutes
        hours = int(Biometric_TimeConsume)
        minutes = int((Biometric_TimeConsume - hours) * 60)

        print("Total Biometric Time: {} hours and {} minutes".format(hours, minutes))

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
PlaceBiometric()


