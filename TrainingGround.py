import random
import time
import calendar
from tkinter import Tk, Label, Button, Entry, LabelFrame, font, PhotoImage

from PIL import ImageTk, Image
import os


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Console Mode
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
        PACD_hours = int(PACD_TimeConsume)
        PACD_minutes = int((PACD_TimeConsume - PACD_hours) * 60)

        print(PACD_hours, PACD_minutes)
        totalPACDTime = "Total PACD Time: {} hours and {} minutes".format(PACD_hours, PACD_minutes)
        print(totalPACDTime)

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

    return total_time_minutes, individual_times

def PlacePortal():
    Portal_total_time_minutes = 0
    Portal_total_time_hours = 0
    Portal_individual_times = []

    for _ in range(applicants):
        Portal_time_avg = random.randint(60, 90)
        Portal_total_minutes = Portal_time_avg / 60
        Portal_total_time_minutes += Portal_total_minutes
        Portal_individual_times.append(Portal_time_avg)

    Portal_total_time_hours = Portal_total_time_minutes / 60

    try:
        Portal_TimeConsume = (Portal_total_time_hours / float(Portal))

        # Convert Portal_TimeConsume into hours and minutes
        Portal_hours = int(Portal_TimeConsume)
        Portal_minutes = int((Portal_TimeConsume - Portal_hours) * 60)

        print(Portal_hours, Portal_minutes)
        totalPortalTime = "Total Portal Time: {} hours and {} minutes".format(Portal_hours, Portal_minutes)
        print(totalPortalTime)

        # Print individual times
        for Portal_i, Portal_time_avg in enumerate(Portal_individual_times, 1):
            Portal_individual_seconds = Portal_time_avg
            Portal_individual_minutes = Portal_individual_seconds // 60
            Portal_individual_seconds = Portal_individual_seconds % 60


            #Print each individual TimeFrame


            # print("Portal Applicant {}: {} seconds ({} minutes and {} seconds)".format(Portal_i, Portal_time_avg, Portal_individual_minutes,  Portal_individual_seconds))



    except ValueError:
        Portal_TimeConsume = (Portal_total_time_hours / 1)

        # Convert Portal_TimeConsume into hours and minutes
        hours = int(Portal_TimeConsume)
        minutes = int((Portal_TimeConsume - hours) * 60)

        print("Total Portal Time: {} hours and {} minutes".format(hours, minutes))

    except ZeroDivisionError:
        Portal_TimeConsume = (Portal_total_time_hours / 1)

        # Convert Portal_TimeConsume into hours and minutes
        hours = int(Portal_TimeConsume)
        minutes = int((Portal_TimeConsume - hours) * 60)

        print("Total Portal Time: {} hours and {} minutes".format(hours, minutes))

    return Portal_total_time_minutes, Portal_individual_times
def PlaceCashier():
    Cashier_total_time_minutes = 0
    Cashier_total_time_hours = 0
    Cashier_individual_times = []

    for _ in range(applicants):
        Cashier_time_avg = random.randint(40, 80)  #consume atleast 40secs to 1min and 20secs individual
        Cashier_total_minutes = Cashier_time_avg / 60
        Cashier_total_time_minutes += Cashier_total_minutes
        Cashier_individual_times.append(Cashier_time_avg)

    Cashier_total_time_hours = Cashier_total_time_minutes / 60


    try:
        Cashier_TimeConsume = (Cashier_total_time_hours/ float(Cashier))

        # Convert Cashier_TimeConsume into hours and minutes
        Cashier_hours = int(Cashier_TimeConsume)
        Cashier_minutes = int((Cashier_TimeConsume - Cashier_hours) * 60)

        totalCashierTime = "Total Cashier Time: {} hours and {} minutes".format(Cashier_hours, Cashier_minutes)
        print(totalCashierTime)

        # Print individual times
        for Cashier_i, Cashier_time_avg in enumerate(Cashier_individual_times, 1):
            Cashier_individual_seconds = Cashier_time_avg
            Cashier_individual_minutes = Cashier_individual_seconds // 60
            Cashier_individual_seconds = Cashier_individual_seconds % 60
            # print("Applicant {}: {} seconds ({} minutes and {} seconds)".format(Cashier_i, Cashier_time_avg, Cashier_individual_minutes, Cashier_individual_seconds))


    except ValueError:
        Cashier_TimeConsume = (Cashier_total_time_hours / 1)

        # Convert Cashier_TimeConsume into hours and minutes
        hours = int(Cashier_TimeConsume)
        minutes = int((Cashier_TimeConsume - hours) * 60)

        print("Total Cashier Time: {} hours and {} minutes".format(hours, minutes))

    except ZeroDivisionError:
        Cashier_TimeConsume = (Cashier_total_time_hours / 1)

        # Convert Cashier_TimeConsume into hours and minutes
        hours = int(Cashier_TimeConsume)
        minutes = int((Cashier_TimeConsume - hours) * 60)

        print("Total Cashier Time: {} hours and {} minutes".format(hours, minutes))

    return Cashier_total_time_minutes, Cashier_individual_times


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
    blue_card_individual_times = []
    green_card_individual_times = []

    # Generate random times for blue card applicants and calculate the total time
    for i in range(blue_card_count):
        time_allocated = random.randint(min_time, max_time)
        total_blue_card_time += time_allocated / 7  # to be fixed
        blue_card_individual_times.append(time_allocated)

    # Generate random times for green card applicants and calculate the total time
    for i in range(green_card_count):
        time_allocated = random.randint(min_time, max_time)
        total_green_card_time += time_allocated / 7  # to be fixed
        green_card_individual_times.append(time_allocated)

    # Convert the total times from seconds to minutes
    total_both_card_time_minutes = (total_blue_card_time + total_green_card_time) / 60
    total_both_card_time_hours = total_both_card_time_minutes / 60

    try:
        ExaminationTimeConsume = total_both_card_time_hours / (7 + float(Computer))

        # Convert Examination_TimeConsume into hours and minutes
        Exam_hours = int(ExaminationTimeConsume)
        Exam_minutes = int((ExaminationTimeConsume - Exam_hours) * 60)

        totalExamtime = "Total Examination Time: {} hours and {} minutes".format(Exam_hours, Exam_minutes)
        print(totalExamtime)

        # Print individual times for blue card applicants
        for i, time_allocated in enumerate(blue_card_individual_times, 1):
            minutes = int(time_allocated / 60)
            seconds = int(time_allocated % 60)
            # print("Blue Card Applicant {}: {} seconds ({} minutes and {} seconds)".format(i, time_allocated, minutes, seconds))

        # Print individual times for green card applicants
        for i, time_allocated in enumerate(green_card_individual_times, 1):
            minutes = int(time_allocated / 60)
            seconds = int(time_allocated % 60)
            # print("Green Card Applicant {}: {} seconds ({} minutes and {} seconds)".format(i, time_allocated, minutes, seconds))

    except ValueError:
        ExaminationTimeConsume = total_both_card_time_hours / 7

        # Convert Examination_TimeConsume into hours and minutes
        hours = int(ExaminationTimeConsume)
        minutes = int((ExaminationTimeConsume - hours) * 60)

        print("Total Examination Time: {} hours and {} minutes".format(hours, minutes))

    except ZeroDivisionError:
        ExaminationTimeConsume = total_both_card_time_hours / 7

        # Convert Examination_TimeConsume into hours and minutes
        hours = int(ExaminationTimeConsume)
        minutes = int((ExaminationTimeConsume - hours) * 60)

        print("Total Examination Time: {} hours and {} minutes".format(hours, minutes))

    return total_both_card_time_minutes, blue_card_individual_times + green_card_individual_times



def PlaceBiometric():
    # Consume at least 40 seconds per person; however, there's a queuing
    # Formula Total Time in MINUTES = (Number of People) x (Time per Person in seconds) / 60
    # Total Time in HOURS = MINUTES / 60

    Biometric_total_time_minutes = 0
    Biometric_total_time_hours = 0
    Biometric_individual_times = []

    for _ in range(applicants):
        Biometric_time_avg = random.randint(40, 80)
        Biometric_total_minutes = Biometric_time_avg / 60
        Biometric_total_time_minutes += Biometric_total_minutes
        Biometric_individual_times.append(Biometric_time_avg)

    Biometric_total_time_hours = Biometric_total_time_minutes / 60


    try:

        Biometric_TimeConsume = (Biometric_total_time_hours / float(Biometric))


        # Convert PACD_TimeConsume into hours and minutes
        Biometric_hours = int(Biometric_TimeConsume)
        Biometric_minutes = int((Biometric_TimeConsume - Biometric_hours) * 60)

        totalBiometrictime = "Total Biometric Time: {} hours and {} minutes".format(Biometric_hours, Biometric_minutes)
        print(totalBiometrictime)

        # Print individual times
        for Biometric_i, Biometric_time_avg in enumerate(Biometric_individual_times, 1):
            Biometric_individual_seconds = Biometric_time_avg
            Biometric_individual_minutes = Biometric_individual_seconds // 60
            Biometric_individual_seconds = Biometric_individual_seconds % 60

            # print each individual timeframe
            # print("Applicant {}: {} seconds ({} minutes and {} seconds)".format(i, time_avg, individual_minutes, individual_seconds))



    except ValueError:
        Biometric_TimeConsume = (Biometric_total_time_hours / 1)

        # Convert PACD_TimeConsume into hours and minutes
        hours = int(Biometric_TimeConsume)
        minutes = int((Biometric_TimeConsume - hours) * 60)

        print("Total Biometric Time: {} hours and {} minutes".format(hours, minutes))

    except ZeroDivisionError:
        Biometric_TimeConsume = (Biometric_total_time_hours / 1)

        # Convert PACD_TimeConsume into hours and minutes
        hours = int(Biometric_TimeConsume)
        minutes = int((Biometric_TimeConsume - hours) * 60)

        print("Total Biometric Time: {} hours and {} minutes".format(hours, minutes))

    return Biometric_total_time_minutes, Biometric_individual_times




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

