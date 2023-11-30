import random
import time
import calendar
from tkinter import Tk, Label, Button, Entry, LabelFrame, font, PhotoImage, Scrollbar, Listbox, Toplevel, messagebox
from pygame import mixer
import sys
from PIL import ImageTk, Image
import os

# Global variable to store the history results
history_results = []
Portal_history_results = []
Cashier_history_results = []
Computer_history_results = []
Biometric_history_results = []



# #Music Play
# mixer.init()
# mixer.music.load('MusicBackground/music_background.mp3')
# mixer.music.play()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Guide
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
yellow_card = int(applicants) * 0.34
blue_card = int(applicants) * 0.28
green_card = int(applicants) * 0.24
orange_card = int(applicants) * 0.14

print(applicants)


# This will show the error problem and effects
today_problem = random.randint(1,100)



# Information Widget
class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20

        self.tooltip = Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")

        label = Label(self.tooltip, text=self.text, background="#ffffe0", relief="solid", borderwidth=1)
        label.pack(ipadx=1)

    def hide_tooltip(self, event):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

def PlacePACD():
    global PACD_history_result, PACD_hours, PACD_minutes
    total_time_minutes = 0
    total_time_hours = 0
    individual_times = []
    PACD_result = PACD_entry.get()

    for _ in range(applicants):
        PACD_time_avg = random.randint(30, 60)
        PACD_total_minutes = PACD_time_avg / 60
        total_time_minutes += PACD_total_minutes
        individual_times.append(PACD_time_avg)

    PACD_total_time_hours = total_time_minutes / 60

    try:
        PACD_TimeConsume = PACD_total_time_hours / (2 + float(PACD_result))

        # Convert PACD_TimeConsume into hours and minutes
        PACD_hours = int(PACD_TimeConsume)
        PACD_minutes = int((PACD_TimeConsume - PACD_hours) * 60)

        print("Total PACD Time: {} hours and {} minutes".format(PACD_hours, PACD_minutes))

        # Print individual times
        for i, time_avg in enumerate(individual_times, 1):
            individual_seconds = time_avg
            individual_minutes = individual_seconds // 60
            individual_seconds = individual_seconds % 60

            #print each individual timeframe
            PACD_history_result = "PACD Applicant {}: {} seconds ({} minutes and {} seconds)".format(i, time_avg, individual_minutes, individual_seconds)
            # print(PACD_history_result)
            history_results.append(PACD_history_result)

    except ValueError:
        PACD_TimeConsume = PACD_total_time_hours / 2

        # Convert PACD_TimeConsume into hours and minutes
        PACD_hours = int(PACD_TimeConsume)
        PACD_minutes = int((PACD_TimeConsume - PACD_hours) * 60)

        print("Total PACD Time: {} hours and {} minutes".format(PACD_hours, PACD_minutes))

        # Print individual times
        for i, time_avg in enumerate(individual_times, 1):
            individual_seconds = time_avg
            individual_minutes = individual_seconds // 60
            individual_seconds = individual_seconds % 60

            # print each individual timeframe
            PACD_history_result = "PACD Applicant {}: {} seconds ({} minutes and {} seconds)".format(i, time_avg,
                                                                                                     individual_minutes,
                                                                                                     individual_seconds)
            # print(PACD_history_result)
            history_results.append(PACD_history_result)

    except ZeroDivisionError:
        PACD_TimeConsume = PACD_total_time_hours / 2

        # Convert PACD_TimeConsume into hours and minutes
        PACD_hours = int(PACD_TimeConsume)
        PACD_minutes = int((PACD_TimeConsume - PACD_hours) * 60)

        print("Total PACD Time: {} hours and {} minutes".format(PACD_hours, PACD_minutes))

        # Print individual times
        for i, time_avg in enumerate(individual_times, 1):
            individual_seconds = time_avg
            individual_minutes = individual_seconds // 60
            individual_seconds = individual_seconds % 60

            # print each individual timeframe
            PACD_history_result = "PACD Applicant {}: {} seconds ({} minutes and {} seconds)".format(i, time_avg,
                                                                                                     individual_minutes,
                                                                                                     individual_seconds)
            # print(PACD_history_result)
            history_results.append(PACD_history_result)

def PlacePortal():
    global Portal_history_result, Portal_hours, Portal_minutes
    Portal_total_time_minutes = 0
    Portal_total_time_hours = 0
    Portal_individual_times = []
    Portal_result = Portal_entry.get()

    for _ in range(applicants):
        Portal_time_avg = random.randint(60, 90)
        Portal_total_minutes = Portal_time_avg / 60
        Portal_total_time_minutes += Portal_total_minutes
        Portal_individual_times.append(Portal_time_avg)

    Portal_total_time_hours = Portal_total_time_minutes / 60

    try:
        Portal_TimeConsume = (Portal_total_time_hours / float(Portal_result))

        # Convert Portal_TimeConsume into hours and minutes
        Portal_hours = int(Portal_TimeConsume)
        Portal_minutes = int((Portal_TimeConsume - Portal_hours) * 60)

        print("Total Portal Time: {} hours and {} minutes".format(Portal_hours, Portal_minutes))

        # Print individual times
        for Portal_i, Portal_time_avg in enumerate(Portal_individual_times, 1):
            Portal_individual_seconds = Portal_time_avg
            Portal_individual_minutes = Portal_individual_seconds // 60
            Portal_individual_seconds = Portal_individual_seconds % 60


            #Print each individual TimeFrame


            Portal_history_result = "Portal Applicant {}: {} seconds ({} minutes and {} seconds)".format(Portal_i, Portal_time_avg, Portal_individual_minutes,  Portal_individual_seconds)
            # print(Portal_history_result)
            Portal_history_results.append(Portal_history_result)



    except ValueError:
        Portal_TimeConsume = (Portal_total_time_hours / 1)

        # Convert Portal_TimeConsume into hours and minutes
        Portal_hours = int(Portal_TimeConsume)
        Portal_minutes = int((Portal_TimeConsume - Portal_hours) * 60)

        print("Total Portal Time: {} hours and {} minutes".format(Portal_hours, Portal_minutes))
        # Print individual times
        for Portal_i, Portal_time_avg in enumerate(Portal_individual_times, 1):
            Portal_individual_seconds = Portal_time_avg
            Portal_individual_minutes = Portal_individual_seconds // 60
            Portal_individual_seconds = Portal_individual_seconds % 60

            # Print each individual TimeFrame

            Portal_history_result = "Portal Applicant {}: {} seconds ({} minutes and {} seconds)".format(Portal_i,Portal_time_avg, Portal_individual_minutes,Portal_individual_seconds)
            # print(Portal_history_result)
            Portal_history_results.append(Portal_history_result)

    except ZeroDivisionError:
        Portal_TimeConsume = (Portal_total_time_hours / 1)

        # Convert Portal_TimeConsume into hours and minutes
        Portal_hours = int(Portal_TimeConsume)
        Portal_minutes = int((Portal_TimeConsume - Portal_hours) * 60)

        print("Total Portal Time: {} hours and {} minutes".format(Portal_hours, Portal_minutes))

        # Print individual times
        for Portal_i, Portal_time_avg in enumerate(Portal_individual_times, 1):
            Portal_individual_seconds = Portal_time_avg
            Portal_individual_minutes = Portal_individual_seconds // 60
            Portal_individual_seconds = Portal_individual_seconds % 60

            # Print each individual TimeFrame

            Portal_history_result = "Portal Applicant {}: {} seconds ({} minutes and {} seconds)".format(Portal_i,Portal_time_avg,Portal_individual_minutes,Portal_individual_seconds)
            # print(Portal_history_result)
            Portal_history_results.append(Portal_history_result)

def PlaceCashier():
    global Cashier_hours, Cashier_minutes
    Cashier_total_time_minutes = 0
    Cashier_total_time_hours = 0
    Cashier_individual_times = []
    Cashier_result = Cashier_entry.get()

    for _ in range(applicants):
        Cashier_time_avg = random.randint(40, 80)  #consume atleast 40secs to 1min and 20secs individual
        Cashier_total_minutes = Cashier_time_avg / 60
        Cashier_total_time_minutes += Cashier_total_minutes
        Cashier_individual_times.append(Cashier_time_avg)

    Cashier_total_time_hours = Cashier_total_time_minutes / 60


    try:
        Cashier_TimeConsume = (Cashier_total_time_hours/ float(Cashier_result))

        # Convert Cashier_TimeConsume into hours and minutes
        Cashier_hours = int(Cashier_TimeConsume)
        Cashier_minutes = int((Cashier_TimeConsume - Cashier_hours) * 60)

        print("Total Cashier Time: {} hours and {} minutes".format(Cashier_hours, Cashier_minutes))

        # Print individual times
        for Cashier_i, Cashier_time_avg in enumerate(Cashier_individual_times, 1):
            Cashier_individual_seconds = Cashier_time_avg
            Cashier_individual_minutes = Cashier_individual_seconds // 60
            Cashier_individual_seconds = Cashier_individual_seconds % 60
            Cashier_history_result = "Cashier Applicant {}: {} seconds ({} minutes and {} seconds)".format(Cashier_i, Cashier_time_avg, Cashier_individual_minutes, Cashier_individual_seconds)
            Cashier_history_results.append(Cashier_history_result)

    except ValueError:
        Cashier_TimeConsume = (Cashier_total_time_hours / 1)

        # Convert Cashier_TimeConsume into hours and minutes
        Cashier_hours = int(Cashier_TimeConsume)
        Cashier_minutes = int((Cashier_TimeConsume - Cashier_hours) * 60)

        print("Total Cashier Time: {} hours and {} minutes".format(Cashier_hours, Cashier_minutes))

        # Print individual times
        for Cashier_i, Cashier_time_avg in enumerate(Cashier_individual_times, 1):
            Cashier_individual_seconds = Cashier_time_avg
            Cashier_individual_minutes = Cashier_individual_seconds // 60
            Cashier_individual_seconds = Cashier_individual_seconds % 60
            Cashier_history_result = "Cashier Applicant {}: {} seconds ({} minutes and {} seconds)".format(Cashier_i,
                                                                                                           Cashier_time_avg,
                                                                                                           Cashier_individual_minutes,
                                                                                                           Cashier_individual_seconds)
            Cashier_history_results.append(Cashier_history_result)

    except ZeroDivisionError:
        Cashier_TimeConsume = (Cashier_total_time_hours / 1)

        # Convert Cashier_TimeConsume into hours and minutes
        Cashier_hours = int(Cashier_TimeConsume)
        Cashier_minutes = int((Cashier_TimeConsume - Cashier_hours) * 60)

        print("Total Cashier Time: {} hours and {} minutes".format(Cashier_hours, Cashier_minutes))

        # Print individual times
        for Cashier_i, Cashier_time_avg in enumerate(Cashier_individual_times, 1):
            Cashier_individual_seconds = Cashier_time_avg
            Cashier_individual_minutes = Cashier_individual_seconds // 60
            Cashier_individual_seconds = Cashier_individual_seconds % 60
            Cashier_history_result = "Cashier Applicant {}: {} seconds ({} minutes and {} seconds)".format(Cashier_i,
                                                                                                           Cashier_time_avg,
                                                                                                           Cashier_individual_minutes,
                                                                                                           Cashier_individual_seconds)
            Cashier_history_results.append(Cashier_history_result)

def PlaceComputer():
    global Exam_hours, Exam_minutes
    Computer_result = Computer_entry.get()
    # Define the range for time allocation (10 minutes to 1 hour in seconds)
    min_time = 10 * 60
    max_time = 60 * 60

    # Define the number of blue card and green card applicants
    blue_card_count = int(blue_card)
    green_card_count = int(green_card)

    # Initialize variables to store the total times for blue card and green card applicants
    total_blue_card_time = 0
    total_green_card_time = 0

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
        ExaminationTimeConsume = total_both_card_time_hours / (7 + float(Computer_result))

        # Convert Examination_TimeConsume into hours and minutes
        Exam_hours = int(ExaminationTimeConsume)
        Exam_minutes = int((ExaminationTimeConsume - Exam_hours) * 60)

        print("Total Examation Time: {} hours and {} minutes".format(Exam_hours, Exam_minutes))

        # Print individual times for blue card applicants
        for i, time_allocated in enumerate(blue_card_individual_times, 1):
            minutes = int(time_allocated / 60)
            seconds = int(time_allocated % 60)
            Computer_history_result = "Renewal License Examination {}: {} seconds ({} minutes and {} seconds)".format(i, time_allocated, minutes,seconds)

            Computer_history_results.append(Computer_history_result)

        # Print individual times for green card applicants
        for i, time_allocated in enumerate(green_card_individual_times, 1):
            minutes = int(time_allocated / 60)
            seconds = int(time_allocated % 60)
            Computer_history_result = "Non-Professional License Examination {}: {} seconds ({} minutes and {} seconds)".format(i, time_allocated, minutes,seconds)
            Computer_history_results.append(Computer_history_result)




    except ValueError:
        ExaminationTimeConsume = total_both_card_time_hours / 7

        # Convert Examination_TimeConsume into hours and minutes
        Exam_hours = int(ExaminationTimeConsume)
        Exam_minutes = int((ExaminationTimeConsume - Exam_hours) * 60)

        print("Total Examation Time: {} hours and {} minutes".format(Exam_hours, Exam_minutes))

        # Print individual times for blue card applicants
        for i, time_allocated in enumerate(blue_card_individual_times, 1):
            minutes = int(time_allocated / 60)
            seconds = int(time_allocated % 60)
            Computer_history_result = "Renewal License Examination {}: {} seconds ({} minutes and {} seconds)".format(i,
                                                                                                                      time_allocated,
                                                                                                                      minutes,
                                                                                                                      seconds)

            Computer_history_results.append(Computer_history_result)

        # Print individual times for green card applicants
        for i, time_allocated in enumerate(green_card_individual_times, 1):
            minutes = int(time_allocated / 60)
            seconds = int(time_allocated % 60)
            Computer_history_result = "Non-Professional License Examination {}: {} seconds ({} minutes and {} seconds)".format(
                i, time_allocated, minutes, seconds)
            Computer_history_results.append(Computer_history_result)

    except ZeroDivisionError:
        ExaminationTimeConsume = total_both_card_time_hours / 7

        # Convert Examination_TimeConsume into hours and minutes
        Exam_hours = int(ExaminationTimeConsume)
        Exam_minutes = int((ExaminationTimeConsume - Exam_hours) * 60)

        print("Total Examation Time: {} hours and {} minutes".format(Exam_hours, Exam_minutes))

        # Print individual times for blue card applicants
        for i, time_allocated in enumerate(blue_card_individual_times, 1):
            minutes = int(time_allocated / 60)
            seconds = int(time_allocated % 60)
            Computer_history_result = "Renewal License Examination {}: {} seconds ({} minutes and {} seconds)".format(i,
                                                                                                                      time_allocated,
                                                                                                                      minutes,
                                                                                                                      seconds)

            Computer_history_results.append(Computer_history_result)

        # Print individual times for green card applicants
        for i, time_allocated in enumerate(green_card_individual_times, 1):
            minutes = int(time_allocated / 60)
            seconds = int(time_allocated % 60)
            Computer_history_result = "Non-Professional License Examination {}: {} seconds ({} minutes and {} seconds)".format(
                i, time_allocated, minutes, seconds)
            Computer_history_results.append(Computer_history_result)


# To be fixed Dapat sa random ppl first 7 ang makaka accomodate ng room


def PlaceBiometric():
    global Biometric_hours, Biometric_minutes
    # Consume at least 40 seconds per person; however, there's a queuing
    # Formula Total Time in MINUTES = (Number of People) x (Time per Person in seconds) / 60
    # Total Time in HOURS = MINUTES / 60

    Biometric_total_time_minutes = 0
    Biometric_total_time_hours = 0
    Biometric_individual_times = []
    Biometric_result = Biometric_entry.get()

    for _ in range(applicants):
        Biometric_time_avg = random.randint(40, 80)
        Biometric_total_minutes = Biometric_time_avg / 60
        Biometric_total_time_minutes += Biometric_total_minutes
        Biometric_individual_times.append(Biometric_time_avg)

    Biometric_total_time_hours = Biometric_total_time_minutes / 60


    try:

        Biometric_TimeConsume = (Biometric_total_time_hours / float(Biometric_result))


        # Convert PACD_TimeConsume into hours and minutes
        Biometric_hours = int(Biometric_TimeConsume)
        Biometric_minutes = int((Biometric_TimeConsume - Biometric_hours) * 60)

        print("Total Biometric Time: {} hours and {} minutes".format(Biometric_hours, Biometric_minutes))

        # Print individual times
        for Biometric_i, Biometric_time_avg in enumerate(Biometric_individual_times, 1):
            Biometric_individual_seconds = Biometric_time_avg
            Biometric_individual_minutes = Biometric_individual_seconds // 60
            Biometric_individual_seconds = Biometric_individual_seconds % 60

            # print each individual timeframe
            Biometric_history_result = "Biometric Applicant {}: {} seconds ({} minutes and {} seconds)".format(Biometric_i, Biometric_time_avg, Biometric_individual_minutes, Biometric_individual_seconds)
            Biometric_history_results.append(Biometric_history_result)



    except ValueError:
        Biometric_TimeConsume = (Biometric_total_time_hours / 1)

        # Convert Biometric into hours and minutes
        Biometric_hours = int(Biometric_TimeConsume)
        Biometric_minutes = int((Biometric_TimeConsume - Biometric_hours) * 60)

        print("Total Biometric Time: {} hours and {} minutes".format(Biometric_hours, Biometric_minutes))

        # Print individual times
        for Biometric_i, Biometric_time_avg in enumerate(Biometric_individual_times, 1):
            Biometric_individual_seconds = Biometric_time_avg
            Biometric_individual_minutes = Biometric_individual_seconds // 60
            Biometric_individual_seconds = Biometric_individual_seconds % 60

            # print each individual timeframe
            Biometric_history_result = "Biometric Applicant {}: {} seconds ({} minutes and {} seconds)".format(
                Biometric_i, Biometric_time_avg, Biometric_individual_minutes, Biometric_individual_seconds)
            Biometric_history_results.append(Biometric_history_result)

    except ZeroDivisionError:
        Biometric_TimeConsume = (Biometric_total_time_hours / 1)

        # Convert PACD_TimeConsume into hours and minutes
        Biometric_hours = int(Biometric_TimeConsume)
        Biometric_minutes = int((Biometric_TimeConsume - Biometric_hours) * 60)

        print("Total Biometric Time: {} hours and {} minutes".format(Biometric_hours, Biometric_minutes))

        # Print individual times
        for Biometric_i, Biometric_time_avg in enumerate(Biometric_individual_times, 1):
            Biometric_individual_seconds = Biometric_time_avg
            Biometric_individual_minutes = Biometric_individual_seconds // 60
            Biometric_individual_seconds = Biometric_individual_seconds % 60

            # print each individual timeframe
            Biometric_history_result = "Biometric Applicant {}: {} seconds ({} minutes and {} seconds)".format(
                Biometric_i, Biometric_time_avg, Biometric_individual_minutes, Biometric_individual_seconds)
            Biometric_history_results.append(Biometric_history_result)

def guide_butt():
    # Direct to INSTRUCTION GUI
    print("Button clicked!")
    root.destroy()
    InstructionMode()


def goToSimulation_butt():
    # Direct to Simulation Mode
    print("Button clicked to Simulation Mode")
    ins.destroy()
    Simulation_Mode()

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2 - 40

    window.geometry(f"{width}x{height}+{x}+{y}")


# GUI Mode
def MAINGUIMODE():
    global root

    def on_exit():
        root.destroy()
        sys.exit()

    root = Tk()
    root.title("LTO Licensing Queueing System Simulation")
    root.iconbitmap('LTO Image/LTO Logo.ico')
    root.geometry("1374x751")
    root.resizable(False, False)
    center_window(root, 1374, 751)

    img = ImageTk.PhotoImage(Image.open("LTO Image/LTO_background.png"))  # LTO Background
    panel = Label(root, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")

    image = Image.open("LTO Image/start_btn.png")
    image = image.resize((185, 90))  # Remove the ANTIALIAS filter
    photo = ImageTk.PhotoImage(image)

    button = Button(panel, image=photo, command=guide_butt)
    button.place(relx=0.52, rely=0.54, anchor="center")

    alphatest = Label(panel, text="Keima Test 1.10",font=("Montserrat", 12, "italic"), bg='white', fg="#440d31")
    alphatest.place(x=1250,y=710)

    # Bind the window closing event to the on_closing function
    root.protocol("WM_DELETE_WINDOW", on_exit)
    root.mainloop()


def InstructionMode():
    global ins

    def on_exit():
        ins.destroy()
        sys.exit()

    ins = Tk()
    ins.title("LTO Licensing Queueing System Simulation")
    ins.geometry("1093x800")
    ins.iconbitmap('LTO Image/LTO Logo.ico')
    ins.resizable(False, False)
    center_window(ins, 1093, 780)

    ins_img = ImageTk.PhotoImage(Image.open("LTO Image/LTO_Instruction.png"))  # LTO Instruction Background
    panel = Label(ins, image=ins_img)
    panel.pack(side="bottom", fill="both", expand="yes")

    skip_button = Button(ins, command=goToSimulation_butt, text="Start", width=20)
    skip_button.place(relx=0.45, rely=0.98, anchor="w")

    # Bind the window closing event to the on_closing function
    ins.protocol("WM_DELETE_WINDOW", on_exit)

    ins.mainloop()


def Simulation_Mode():
    global PACD_entry, Portal_entry, Cashier_entry, Computer_entry, Biometric_entry, Simulation_Button, img, simulate_pacd, simulate_cashier, simulate_biometric, simulate_exam, simulate_portal
    def simulateButtonEnter(event):
        Simulation_Button.configure(bg="#35aefa")  # Change the background color when the mouse enters

    def simulateButtonLeave(event):
        Simulation_Button.configure(bg="SystemButtonFace")

    def resultEnter(event):
        SimulationResultButton.configure(bg="#35aefa")  # Change the background color when the mouse enters

    def resultLeave(event):
        SimulationResultButton.configure(bg="SystemButtonFace")

    def historyEnter(event):
        HistoryButton.configure(bg="#35aefa")  # Change the background color when the mouse enters

    def historyLeave(event):
        HistoryButton.configure(bg="SystemButtonFace")

    def showResults():
        Simulation_Button.configure(state='disabled')  # Disable the Simulation_Button
        PACD_entry.configure(state='disabled')
        Portal_entry.configure(state='disabled')
        Cashier_entry.configure(state='disabled')
        Computer_entry.configure(state='disabled')
        Biometric_entry.configure(state='disabled')

        SimulationResultButton.grid(row=0, column=0, ipadx=84, padx=14, pady=40, sticky='nsew')
        title_text2.destroy()
        # write result code here

    def PACD_entry_focus_in(event):
        if PACD_entry.get() == "Enter number":
            PACD_entry.delete(0, 'end')
            PACD_entry.config(fg="Black")


    def PACD_entry_focus_out(event):
        pacd_input = PACD_entry.get()
        if pacd_input == "":
            PACD_entry.insert(0, "Enter number")
            PACD_entry.config(fg="gray")

        elif not pacd_input.isdigit():
            messagebox.showinfo("Input Error", "Please input a number for PACD")
            PACD_entry.delete(0, 'end')
            PACD_entry.insert(0, "Enter number")
            PACD_entry.config(fg="gray")

    def Portal_entry_focus_in(event):
        if Portal_entry.get() == "Enter number":
            Portal_entry.delete(0, 'end')
            Portal_entry.config(fg="Black")

    def Portal_entry_focus_out(event):
        Portal_input = Portal_entry.get()
        if Portal_input == "":
            Portal_entry.insert(0, "Enter number")
            Portal_entry.config(fg="gray")
        elif not Portal_input.isdigit():
            messagebox.showinfo("Input Error", "Please input a number for Portal")
            Portal_entry.delete(0, 'end')
            Portal_entry.insert(0, 'Enter number')
            Portal_entry.config(fg="gray")

    def Cashier_entry_focus_in(event):
        if Cashier_entry.get() == "Enter number":
            Cashier_entry.delete(0, 'end')
            Cashier_entry.config(fg="Black")

    def Cashier_entry_focus_out(event):
        Cashier_input = Cashier_entry.get()
        if Cashier_input == "":
            Cashier_entry.insert(0, "Enter number")
            Cashier_entry.config(fg="gray")

        elif not Cashier_input.isdigit():
            messagebox.showinfo("Input Error", "Please input a number for Cashier")
            Cashier_entry.delete(0, 'end')
            Cashier_entry.insert(0, 'Enter number')
            Cashier_entry.config(fg="gray")

    def Computer_entry_focus_in(event):
        if Computer_entry.get() == "Enter number":
            Computer_entry.delete(0, 'end')
            Computer_entry.config(fg="Black")

    def Computer_entry_focus_out(event):
        Computer_input = Computer_entry.get()
        if Computer_input == "":
            Computer_entry.insert(0, "Enter number")
            Computer_entry.config(fg="gray")

        elif not Computer_input.isdigit():
            messagebox.showinfo("Input Error", "Please input a number for Computer")
            Computer_entry.delete(0, 'end')
            Computer_entry.insert(0, 'Enter number')
            Computer_entry.config(fg="gray")


    def Biometric_entry_focus_in(event):
        if Biometric_entry.get() == "Enter number":
            Biometric_entry.delete(0, 'end')
            Biometric_entry.config(fg="Black")

    def Biometric_entry_focus_out(event):
        Biometric_input = Biometric_entry.get()
        if Biometric_input == "":
            Biometric_entry.insert(0, "Enter number")
            Biometric_entry.config(fg="gray")

        elif not Biometric_input.isdigit():
            messagebox.showinfo("Input Error", "Please input a number for Biometric")
            Biometric_entry.delete(0, 'end')
            Biometric_entry.insert(0, 'Enter number')
            Biometric_entry.config(fg="gray")

    def show_info():
        messagebox.showinfo("Information",
                            "Public Assistance Complaint Desk(PACD) currently have 2 LTO Worker that handle your documents."
                            "By checking the documents, they are the one who will give you the Color card based on your designated.")

    def Portal_show_info():
        messagebox.showinfo("Information","There are currently 1 Portal in the LTO Daet.")

    def Cashier_show_info():
        messagebox.showinfo("Information","There are currently 1 Cashier in the LTO Daet.")

    def Computer_show_info():
        messagebox.showinfo("Information","There are currently 7 Computers in the Examination Room")

    def Biometric_show_info():
        messagebox.showinfo("Information","There are 1 Biometric in LTO Daet.")

    def restart_program():
        global applicants, yellow_card, blue_card, green_card, orange_card, today_problem
        result = messagebox.askyesno("Restart", "Do you really want to restart the program?")
        if result:
            applicants = random.randint(95, 145)
            yellow_card = int(applicants) * 0.34
            blue_card = int(applicants) * 0.28
            green_card = int(applicants) * 0.24
            orange_card = int(applicants) * 0.14
            today_problem = random.randint(1,100)

            sim.destroy()
            time.sleep(1)
            Simulation_Mode()
            print("Restarting the program")

            # Right now, the only problem is that I can't reset the History

    def configresult():
        simulate_pacd.config(text=f"+ {int(PACD_entry.get())}", font=("Montserrat", 13, "italic"))
        simulate_cashier.config(text=f"+ {int(Cashier_entry.get())}", font=("Montserrat", 13, "italic"))
        simulate_biometric.config(text=f"+ {int(Biometric_entry.get())}", font=("Montserrat", 13, "italic"))
        simulate_portal.config(text=f"+ {int(Portal_entry.get())}", font=("Montserrat", 13, "italic"))
        simulate_exam.config(text=f"+ {int(Computer_entry.get())}", font=("Montserrat", 13, "italic"))

    def on_exit_click():
        sim.destroy()
        sys.exit()

    sim = Tk()
    sim.title("LTO Licensing Queueing System Simulation")
    sim.iconbitmap('LTO Image/LTO Logo.ico')
    sim.geometry("1374x751")
    sim.resizable(False, False)
    sim.configure(bg="lightblue")
    center_window(sim, 1374, 751)


    # background image
    img = ImageTk.PhotoImage(Image.open("LTO Image/lto_simbg.png"))  # LTO Background
    panel = Label(sim, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")

    alphatest = Label(panel, text="Keima Test 1.10", font=("Montserrat", 12, "italic"), bg='white', fg="#440d31")
    alphatest.place(x=1215, y=710)

    # font
    mont_normal = font.Font(family='Montserrat', size=12, weight='normal')
    mont_bold = font.Font(family='Montserrat', size=12, weight='bold')
    mont_Large = font.Font(family='Montserrat', size=20, weight='bold')

    # Frame
    frame_width = 400
    frame_height = 500
    first_frame = LabelFrame(sim, bg="#e9e9e9")  # Set bd for sizing
    first_frame.place(x=50, y=30, width=frame_width, height=frame_height)
    first_frame.columnconfigure(0, minsize=350, weight=1)
    first_frame.rowconfigure(0, weight=1)


    simage_path = 'LTO Image/restart.png'
    simg = PhotoImage(file=simage_path)

    restart_button = Button(first_frame, text="Restart", image=simg, command=restart_program, width=30, height=30)
    restart_button.place(x=5, y=5)

    # Text Label
    title_text = Label(first_frame, text="LTO SIMULATION", font=mont_Large, bg="#e9e9e9")
    title_text.grid(row=0, column=0, padx=5, pady=20)

    # PACD Station
    PACD_label = Label(first_frame, text="PACD", font=mont_bold, bg="#e9e9e9")
    PACD_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')

    # Label Icon Question
    PACD_info_label = Label(first_frame, text="ⓘ", font=("Arial", 12), cursor="question_arrow", bg='#e9e9e9')
    PACD_info_label.grid(row=1, column=0, padx=110, pady=10, sticky='w')
    ToolTip(PACD_info_label, "Click for information")
    PACD_info_label.bind("<Button-1>", lambda event: show_info())

    PACD_entry = Entry(first_frame, font=mont_normal, bd=5)
    PACD_entry.grid(row=1, column=0, ipadx=25, padx=10, pady=10, sticky='ne')
    PACD_entry.insert(0, 'Enter number')
    PACD_entry.bind("<FocusIn>", PACD_entry_focus_in)
    PACD_entry.bind("<FocusOut>", PACD_entry_focus_out)


    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Portal Station
    Portal_label = Label(first_frame, text="PORTAL", font=mont_bold, bg="#e9e9e9")
    Portal_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')

    # Label Icon Question
    Portal_info_label = Label(first_frame, text="ⓘ", font=("Arial", 12), cursor="question_arrow", bg='#e9e9e9')
    Portal_info_label.grid(row=2, column=0, padx=110, pady=10, sticky='w')
    ToolTip(Portal_info_label, "Click for information")
    Portal_info_label.bind("<Button-1>", lambda event: Portal_show_info())

    Portal_entry = Entry(first_frame, bd=5, font=mont_normal)
    Portal_entry.grid(row=2, column=0, ipadx=25, padx=10, pady=10, sticky='ne')
    Portal_entry.insert(0, 'Enter number')
    Portal_entry.bind("<FocusIn>", Portal_entry_focus_in)
    Portal_entry.bind("<FocusOut>", Portal_entry_focus_out)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Cashier Station
    Cashier_label = Label(first_frame, text="CASHIER", font=mont_bold, bg="#e9e9e9")
    Cashier_label.grid(row=3, column=0, padx=10, pady=10, sticky='w')

    # Label Icon Question
    Cashier_info_label = Label(first_frame, text="ⓘ", font=("Arial", 12), cursor="question_arrow", bg='#e9e9e9')
    Cashier_info_label.grid(row=3, column=0, padx=110, pady=10, sticky='w')
    ToolTip(Cashier_info_label, "Click for information")
    Cashier_info_label.bind("<Button-1>", lambda event: Cashier_show_info())

    Cashier_entry = Entry(first_frame, bd=5, font=mont_normal)
    Cashier_entry.grid(row=3, column=0, ipadx=25, padx=10, pady=10, sticky='ne')
    Cashier_entry.insert(0, 'Enter number')
    Cashier_entry.bind("<FocusIn>", Cashier_entry_focus_in)
    Cashier_entry.bind("<FocusOut>", Cashier_entry_focus_out)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Examination Station
    Computer_label = Label(first_frame, text="COMPUTER", font=mont_bold, bg="#e9e9e9")
    Computer_label.grid(row=4, column=0, padx=10, pady=10, sticky='w')

    # Label Icon Question
    Computer_info_label = Label(first_frame, text="ⓘ", font=("Arial", 12), cursor="question_arrow", bg='#e9e9e9')
    Computer_info_label.grid(row=4, column=0, padx=110, pady=10, sticky='w')
    ToolTip(Computer_info_label, "Click for information")
    Computer_info_label.bind("<Button-1>", lambda event: Computer_show_info())

    Computer_entry = Entry(first_frame, bd=5, font=mont_normal)
    Computer_entry.grid(row=4, column=0, ipadx=25, padx=10, pady=10, sticky='ne')
    Computer_entry.insert(0, 'Enter number')
    Computer_entry.bind("<FocusIn>", Computer_entry_focus_in)
    Computer_entry.bind("<FocusOut>", Computer_entry_focus_out)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Biometric Station
    Biometric_label = Label(first_frame, text="BIOMETRIC", font=mont_bold, bg='#e9e9e9')
    Biometric_label.grid(row=5, column=0, padx=10, pady=10, sticky='w')

    # Label Icon Question
    Biometric_info_label = Label(first_frame, text="ⓘ", font=("Arial", 12), cursor="question_arrow", bg='#e9e9e9')
    Biometric_info_label.grid(row=5, column=0, padx=110, pady=10, sticky='w')
    ToolTip(Biometric_info_label, "Click for information")
    Biometric_info_label.bind("<Button-1>", lambda event: Biometric_show_info())

    Biometric_entry = Entry(first_frame, bd=5, font=mont_normal)
    Biometric_entry.grid(row=5, column=0, ipadx=25, padx=10, pady=10, sticky='ne')
    Biometric_entry.insert(0, 'Enter number')
    Biometric_entry.bind("<FocusIn>", Biometric_entry_focus_in)
    Biometric_entry.bind("<FocusOut>", Biometric_entry_focus_out)

    Simulation_Button = Button(first_frame, text="SIMULATE", fg="#000000", font=mont_bold, width=10, height=2, bd=5,
    command=lambda: (showResults(), PlacePACD(), PlacePortal(), PlaceCashier(), PlaceComputer(), PlaceBiometric(), configresult()))

    Simulation_Button.bind("<Enter>", simulateButtonEnter)
    Simulation_Button.bind("<Leave>", simulateButtonLeave)
    Simulation_Button.grid(row=6, column=0, ipadx=90, padx=10, pady=40, sticky='nsew')

    # Frame2
    frame2_width = 400
    frame2_height = 150
    first2_frame = LabelFrame(sim, bg="#e9e9e9")  # Set bd for sizing
    first2_frame.place(x=50, y=550, width=frame2_width, height=frame2_height)
    first2_frame.columnconfigure(0, minsize=350, weight=1)
    first2_frame.rowconfigure(20, weight=1)

    # Simulation Animation Frame
    sec_frameWidth = 850
    sec_frameHeight = 670
    sec_frame = LabelFrame(sim)
    sec_frame.place(x=480, y=30, width=sec_frameWidth, height=sec_frameHeight)

    animation_img = ImageTk.PhotoImage(Image.open("LTO Image/LTO_simulation_bg.png"))  # LTO Background
    panel = Label(sec_frame, image=animation_img)
    panel.pack(side="bottom", fill="both", expand="yes")

    # Title for results
    title_text2 = Label(first2_frame, text="Click simulate to generate results", font=mont_bold, bg="#e9e9e9")
    title_text2.grid(row=0, column=0, padx=5, pady=20)

    # Button for results (hidden until simulate is clicked)
    SimulationResultButton = Button(first2_frame, command=simulation_result,text="View Results", fg="black", font=mont_bold)
    SimulationResultButton.bind("<Enter>", resultEnter)
    SimulationResultButton.bind("<Leave>", resultLeave)

    HistoryButton = Button(first2_frame, command=showHistory, text="History", fg="black",font=mont_bold, width=36)
    HistoryButton.bind("<Enter>", historyEnter)
    HistoryButton.bind("<Leave>", historyLeave)
    HistoryButton.place(x=12,y=100)

    # Gonna make label for each station
    simulate_pacd = Label(sec_frame, text="", bg="#ffffff")
    simulate_pacd.place(x=300, y=425)

    simulate_cashier = Label(sec_frame, text="", bg="#ffffff")
    simulate_cashier.place(x=800, y=300)

    simulate_biometric = Label(sec_frame, text="", bg="#ffffff")
    simulate_biometric.place(x=800, y=100)

    simulate_portal = Label(sec_frame, text="", bg="#ffffff")
    simulate_portal.place(x=800, y=500)

    simulate_exam = Label(sec_frame, text="", bg="#ffffff")
    simulate_exam.place(x=480, y=16)

    # Load the transparent image
    walking_image = Image.open("Walking/0000.png")
    walking_ppl = ImageTk.PhotoImage(walking_image)

    # Create a Label widget to display the transparent image
    walking_simulate = Label(sec_frame, image=walking_ppl, bg='white')  # Set the background color to white
    walking_simulate.place(x=1, y=433)





    # Register the on_exit_click function to handle window closing
    sim.protocol("WM_DELETE_WINDOW", on_exit_click)
    sim.mainloop()


def simulation_result():
    global total_applicants_label, student_permit_label, NonPro_Label,RenewLicense_Label, \
        Miscellaneous_Label, AddedStationLabel, ProblemEncounter_Label, RejectedApplicants_Label, \
    FailedExaminees_Label, avgStudent_Permit_Label, avgNonPro_Label, avgRenewal_Label, avgMisc_label, LTO_worktime


    simresult = Tk()
    simresult.title("Simulation Results")
    simresult.geometry("1200x800")
    simresult.iconbitmap('LTO Image/LTO Logo.ico')
    simresult.resizable(False, False)
    center_window(simresult, 1200, 600)

    def on_closing():
        simresult.destroy()
        sys.exit()

    # Title Frame
    TFrame_width = 1200
    TFrame_height = 50
    TFrame = LabelFrame(simresult, bd=5)  # Set bd for sizing
    TFrame.place(x=0, y=0, width=TFrame_width, height=TFrame_height)
    TFrame.columnconfigure(0, minsize=350, weight=1)
    TFrame.rowconfigure(20, weight=1)

    #Result Frame
    ResultFrame_width = 1200
    ResultFrame_height = 750
    ResultFrame = LabelFrame(simresult, bd=5, bg='#FFFFFF')
    ResultFrame.place(x=0, y=50, width=ResultFrame_width, height=ResultFrame_height)
    TFrame.columnconfigure(0, minsize=500, weight=1)
    TFrame.rowconfigure(20, weight=1)

    # Text Label
    title_text = "LTO Licensing Queueing\nSimulation Result"
    title_ = Label(TFrame, text=title_text, font=("Montserrat", 13, "bold"), bg='white', fg='#092974')
    title_.grid(row=0, column=0, padx=0, pady=0, sticky='nsew')


    student_permit_label = Label(simresult, text="Student Permit Applicants: ", font=("Montserrat", 11, "italic"), bg='white', fg='#440d31')
    student_permit_label.place(x=30, y=120)

    NonPro_Label = Label(simresult, text="Non-Pro License Applicants: ", font=("Montserrat", 11, "italic"),bg='white', fg='#440d31')
    NonPro_Label.place(x=30, y=170)

    RenewLicense_Label = Label(simresult, text="Renew License Applicants: ", font=("Montserrat", 15, "italic"),bg='white', fg='#440d31')
    RenewLicense_Label.place(x=30, y=220)

    Miscellaneous_Label = Label(simresult, text="Miscellaneous Applicants: ", font=("Montserrat", 15, "italic"),bg='white', fg='#440d31')
    Miscellaneous_Label.place(x=30, y=270)

    total_applicants_label = Label(simresult, text="Total Applicants: ", font=("Montserrat", 15, "italic"),bg='white', fg='#440d31')
    total_applicants_label.place(x=30, y=370)

    LTO_worktime = Label(simresult, text="LTO Working total time consume: ", font=("Montserrat", 15, "italic"), bg='white', fg="#440d31")
    LTO_worktime.place(x=30, y=490)

    ProblemEncounter_Label = Label(simresult, text="Problem Encounter: ", font=("Montserrat", 15, "italic"), bg='white', fg="#440d31")
    ProblemEncounter_Label.place(x=700, y=490)

    # Next Row
    AddedStationLabel = Label(simresult, text="Added Station: ", font=("Montserrat", 15, "italic"), bg='white', fg="#440d31")
    AddedStationLabel.place(x=400, y=120)

    FailedExaminees_Label = Label(simresult, text="Failed Examinees: ", font=("Montserrat", 15, "italic"), bg='white',fg="#440d31")
    FailedExaminees_Label.place(x=400, y=170)


    #Third Row
    IndividualAverage_Label = Label(simresult, text="Individual Average Time ",  font=("Montserrat", 15, "italic"), bg='white', fg="#440d31")
    IndividualAverage_Label.place(x=750, y=70)

    avgStudent_Permit_Label = Label(simresult, text="Student permit: ",  font=("Montserrat", 12, "italic"), bg='white', fg="#440d31")
    avgStudent_Permit_Label.place(x=770, y=120)

    avgNonPro_Label = Label(simresult, text="Non-Pro License: ",  font=("Montserrat", 12, "italic"), bg='white', fg="#440d31")
    avgNonPro_Label.place(x=770, y=170)

    avgRenewal_Label = Label(simresult, text="Renewal License: ",  font=("Montserrat", 12, "italic"), bg='white', fg="#440d31")
    avgRenewal_Label.place(x=770, y=220)

    avgMisc_label = Label(simresult, text="Miscellaneous: ",  font=("Montserrat", 12, "italic"), bg='white', fg="#440d31")
    avgMisc_label.place(x=770, y=270)

    # This will make the ApplicantResult Run
    ApplicantResult()


    simresult.mainloop()


def ApplicantResult():
    # This upper one is for the total working hour time
    global overall_hours, overall_minutes, total_minutes_result, combined_hours, total_minutes_equivalent,\
        simulate_pacd, simulate_cashier, simulate_biometric, simulate_exam, simulate_portal

    overall_hours = PACD_hours + Portal_hours + Cashier_hours + Exam_hours + Biometric_hours  # Combination of all Hours Total
    overall_minutes = (PACD_minutes + Portal_minutes + Cashier_minutes + Exam_minutes + Biometric_minutes)  # combination of all Minutes total
    total_minutes_result = overall_minutes / 60  # result in getting an HOUR by using int
    combined_hours = overall_hours + int(total_minutes_result)  # Combination of all HOURS
    total_minutes_equivalent = abs((int(total_minutes_result) * 60) - overall_minutes)  # getting the right amount of minutes
    print("Overall Hours: ", combined_hours)
    print("Over all Minutes: ", overall_minutes)  # overall minutes
    print(total_minutes_equivalent)
    workinghour_result = "{} hours and {} minutes".format(combined_hours, total_minutes_equivalent)
    print(workinghour_result)


    # Student Permit Formula # yellow card for student
    stud_overall_hours = PACD_hours + Portal_hours + Cashier_hours + Biometric_hours
    stud_overall_minutes = PACD_minutes + Portal_minutes + Cashier_minutes + Biometric_minutes
    stud_total_minutes_result = stud_overall_minutes / 60 # it will be getting the minutes
    combined_stud_hours = stud_overall_hours + int(stud_total_minutes_result) #combination of all hours
    stud_computation_hours = combined_stud_hours * 60

    total_stud_minutes_equivalent = abs((int(stud_total_minutes_result) * 60) - stud_overall_minutes) # getting the right amount of minutes

    sum_min_and_hour = (stud_computation_hours + total_stud_minutes_equivalent)  # combining minute and hour into a number form
    getting_initial_stud = sum_min_and_hour / yellow_card  # dividing it into a total student permit applicants

    stud_min_int = int(getting_initial_stud)  # getting the integer minutes
    stud_sec_int = (getting_initial_stud - stud_min_int) * 60  # multiplying by 60 to get the seconds


    print("This is the average of student process: ", sum_min_and_hour / yellow_card)

    stud_avg_result = "{} minutes & {} seconds".format(stud_min_int, int(stud_sec_int))
    print(stud_avg_result)

    #Non Pro Permit Formula # green card for student
    examination_avg_time = random.randint(10, 60)  # 10mins to 1 hour
    nonpro_overall_hours = PACD_hours + Portal_hours + Cashier_hours + Exam_hours + Biometric_hours
    nonpro_overall_minutes = PACD_minutes + Portal_minutes + Cashier_minutes + Exam_minutes + Biometric_minutes



    nonpro_total_minutes_result = nonpro_overall_minutes / 60  # it will be getting the minutes
    combined_nonpro_hours = nonpro_overall_hours + int(nonpro_total_minutes_result)  # combination of all hours
    nonpro_computation_hours = combined_nonpro_hours * 60

    total_nonpro_minutes_equivalent = abs((int(nonpro_total_minutes_result) * 60) - nonpro_overall_minutes)  # getting the right amount of minutes

    nonpro_sum_min_and_hour = (nonpro_computation_hours + total_nonpro_minutes_equivalent)  # combining minute and hour into a number form
    getting_initial_nonpro = nonpro_sum_min_and_hour / green_card  # dividing it into a total non pro applicants


    nonpro_min_int = int(getting_initial_nonpro)  # getting the integer minutes
    nonpro_sec_int = (getting_initial_nonpro - nonpro_min_int) * 60  # multiplying by 60 to get the seconds



    print("This is the average of Non professional process: ", nonpro_sum_min_and_hour / green_card)

    nonpro_avg_result = "{} hours {} minutes & {} seconds".format(1, int(nonpro_min_int),int(nonpro_sec_int))
    print(nonpro_avg_result)


    # Miscellaneous Formula # Orange card for misc
    misc_overall_hours = PACD_hours + Portal_hours + Cashier_hours + Biometric_hours
    misc_overall_minutes = PACD_minutes + Portal_minutes + Cashier_minutes + Biometric_minutes
    misc_total_minutes_result = misc_overall_minutes / 60  # it will be getting the minutes
    combined_misc_hours = misc_overall_hours + int(misc_total_minutes_result)  # combination of all hours
    misc_computation_hours = combined_misc_hours * 60

    total_misc_minutes_equivalent = abs(
        (int(misc_total_minutes_result) * 60) - misc_overall_minutes)  # getting the right amount of minutes

    misc_sum_min_and_hour = (
                misc_computation_hours + total_misc_minutes_equivalent)  # combining minute and hour into a number form
    getting_initial_misc = misc_sum_min_and_hour / orange_card  # dividing it into a total student permit applicants

    misc_min_int = int(getting_initial_misc)  # getting the integer minutes
    misc_sec_int = (getting_initial_misc - misc_min_int) * 60  # multiplying by 60 to get the seconds

    print("This is the average of misc process: ", misc_sum_min_and_hour / orange_card)

    misc_avg_result = "{} minutes & {} seconds".format(misc_min_int, int(misc_sec_int))
    print(misc_avg_result)

    failedExaminers = ((blue_card + green_card) * 0.3)
    print("Failed Examiners",int(failedExaminers))




    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    student_permit_label.config(text=f"Student Permit Applicants: {int(yellow_card)}", font=("Montserrat", 15, "italic"), bg='white',fg='#440d31')
    NonPro_Label.config(text=f"Non-Pro License Applicants: {int(blue_card)}", font=("Montserrat", 15, "italic"), bg='white',fg='#440d31')
    RenewLicense_Label.config(text=f"Renew License Applicants: {int(green_card)}", font=("Montserrat", 15, "italic"), bg='white',fg='#440d31')
    Miscellaneous_Label.config(text=f"Miscellaneous Applicants: {int(orange_card)}", font=("Montserrat", 15, "italic"), bg='white',fg='#440d31')
    total_applicants_label.config(text=f"Total Applicants: {int(yellow_card) + int(blue_card) + int(green_card) + int(orange_card)}", font=("Montserrat", 15, "italic"),bg='white', fg='#440d31')

    try:
        AddedStationLabel.config(text=f"Added Station: {int(PACD_entry.get()) + int(Portal_entry.get()) + int(Cashier_entry.get()) + int(Computer_entry.get()) + int(Biometric_entry.get())}" \
            , font=("Montserrat", 15, "italic"), bg='white', fg='#440d31')
    except ValueError:
        AddedStationLabel.config(text=f"Added Station: None", font=("Montserrat", 15, "italic"), bg='white', fg='#440d31')

    LTO_worktime.config(text=f"LTO total time consumed: {workinghour_result}", font=("Montserrat", 15, "italic"), bg='white',fg='#440d31')

    avgStudent_Permit_Label.config(text=f"Student permit: {stud_avg_result}",  font=("Montserrat", 10, "bold"), bg='white', fg="#440d31")
    avgNonPro_Label.config(text=f"Non-Pro License: {nonpro_avg_result}", font=("Montserrat", 10, "bold"), bg='white',fg="#440d31")
    avgRenewal_Label.config(text=f"Renewal License: {nonpro_avg_result}", font=("Montserrat", 10, "bold"), bg='white',fg="#440d31")
    avgMisc_label.config(text=f"Miscellaneous: {misc_avg_result}",  font=("Montserrat", 10, "bold"), bg='white', fg="#440d31")

    FailedExaminees_Label.config(text=f"Failed Examiners: {int(failedExaminers)}", font=("Montserrat", 15, "italic"), bg='white',fg='#440d31')




    if today_problem == 3:
        problem_result = "Internet Connection Problem"
        ProblemEncounter_Label.config(text=f"Problem Encounter: {problem_result}", font=("Montserrat", 15, "italic"),bg='white', fg='#440d31')
        # THis will add 1 hour to time into the system

        # You can also update a label here if needed
        # For example: status_label.config(text="Internet Connection Problem. Service Delayed.")
    else:
        problem_result = "None"
        ProblemEncounter_Label.config(text=f"Problem Encounter: {problem_result}", font=("Montserrat", 15, "italic"),bg='white', fg='#440d31')
        # You can also update a label here if needed
        # For example: status_label.config(text="No issues today.")


def on_scroll(*args):
    # Function to handle scrolling events
    # You can perform actions based on the scroll position here
    pass

def showHistory():
    historyResult = Tk()
    historyResult.title("Simulation History")
    historyResult.iconbitmap('LTO Image/LTO Logo.ico')
    historyResult.geometry("1000x600")
    historyResult.resizable(False, False)
    center_window(historyResult, 1000, 600)

    # Title Frame
    FFrame_width = 1000
    FFrame_height = 50
    FFrame = LabelFrame(historyResult, bd=5)  # Set bd for sizing
    FFrame.place(x=0, y=0, width=FFrame_width, height=FFrame_height)
    FFrame.columnconfigure(0, minsize=350, weight=1)
    FFrame.rowconfigure(20, weight=1)

    # Result Frame
    HistoryResultFrame_width = 1000
    HistoryResultFrame_height = 550
    HistoryResultFrame = LabelFrame(historyResult, bd=5, bg='#FFFFFF')
    HistoryResultFrame.place(x=0, y=50, width=HistoryResultFrame_width, height=HistoryResultFrame_height)
    FFrame.columnconfigure(0, minsize=500, weight=1)
    FFrame.rowconfigure(20, weight=1)

    # Text Label
    historytitle_text = "LTO Licensing Queueing\nApplicant History"
    historytitle_ = Label(FFrame, text=historytitle_text, font=("Montserrat", 13, "bold"), bg='white', fg='#AF5FD7')
    historytitle_.grid(row=0, column=0, padx=0, pady=0, sticky='nsew')

    # Create a vertical scrollbar
    scrollbar = Scrollbar(HistoryResultFrame, orient="vertical", command=on_scroll, width=20, relief="flat")

    # Create a widget (e.g., Listbox or Text) that you want to attach the scrollbar to
    listbox = Listbox(HistoryResultFrame, yscrollcommand=scrollbar.set)

    # Concatenate the two lists
    all_history_results = history_results + Portal_history_results + Computer_history_results + Cashier_history_results + Biometric_history_results
    # Add items to the listbox
    for result in all_history_results:
        listbox.insert("end", result)

    # Pack the widgets
    listbox.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Set the scrollbar to operate on the listbox
    scrollbar.config(command=listbox.yview)


# MAINGUIMODE()
Simulation_Mode()


