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


# Item to be added
PACD = input("Type the number of PACD to be added: ")
Portal = input("Type the number of Portal to be added: ")


print("")


PlacePACD()
PlacePortal()

