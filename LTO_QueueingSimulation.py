import random
import time
import calendar
from tkinter import Tk, Label, Button, Entry, LabelFrame, font, PhotoImage, Scrollbar, Listbox
from pygame import mixer

from PIL import ImageTk, Image
import os

# Global variable to store the history results
history_results = []
Portal_history_results = []


#Music Play
mixer.init()
mixer.music.load('MusicBackground/music_background.mp3')
mixer.music.play()


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
yellow_card = applicants * 0.34
blue_card = applicants * 0.28
green_card = applicants * 0.24
orange_card = applicants * 0.14


def PlacePACD():
    global PACD_history_result
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
        hours = int(PACD_TimeConsume)
        minutes = int((PACD_TimeConsume - hours) * 60)

        print("Total PACD Time: {} hours and {} minutes".format(hours, minutes))

        # Print individual times
        for i, time_avg in enumerate(individual_times, 1):
            individual_seconds = time_avg
            individual_minutes = individual_seconds // 60
            individual_seconds = individual_seconds % 60

            #print each individual timeframe
            PACD_history_result = "PACD Applicant {}: {} seconds ({} minutes and {} seconds)".format(i, time_avg, individual_minutes, individual_seconds)
            print(PACD_history_result)
            history_results.append(PACD_history_result)

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
    global Portal_history_result
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
        hours = int(Portal_TimeConsume)
        minutes = int((Portal_TimeConsume - hours) * 60)

        print("Total Portal Time: {} hours and {} minutes".format(hours, minutes))

        # Print individual times
        for Portal_i, Portal_time_avg in enumerate(Portal_individual_times, 1):
            Portal_individual_seconds = Portal_time_avg
            Portal_individual_minutes = Portal_individual_seconds // 60
            Portal_individual_seconds = Portal_individual_seconds % 60


            #Print each individual TimeFrame


            Portal_history_result = "Portal Applicant {}: {} seconds ({} minutes and {} seconds)".format(Portal_i, Portal_time_avg, Portal_individual_minutes,  Portal_individual_seconds)
            print(Portal_history_result)
            Portal_history_results.append(Portal_history_result)



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

def PlaceCashier():
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
        hours = int(Cashier_TimeConsume)
        minutes = int((Cashier_TimeConsume - hours) * 60)

        print("Total Cashier Time: {} hours and {} minutes".format(hours, minutes))

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

def PlaceComputer():
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
        ExaminationTimeConsume = total_both_card_time_hours / (7 + float(Computer_result))

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
        hours = int(Biometric_TimeConsume)
        minutes = int((Biometric_TimeConsume - hours) * 60)

        print("Total Biometric Time: {} hours and {} minutes".format(hours, minutes))

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
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")

# GUI Mode
def MAINGUIMODE():
    global root
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
    root.mainloop()


def InstructionMode():
    global ins
    ins = Tk()
    ins.title("LTO Licensing Queueing System Simulation")
    ins.geometry("1093x800")
    ins.iconbitmap('LTO Image/LTO Logo.ico')
    ins.resizable(False, False)
    center_window(ins, 1093, 800)

    ins_img = ImageTk.PhotoImage(Image.open("LTO Image/LTO_Instruction.png"))  # LTO Instruction Background
    panel = Label(ins, image=ins_img)
    panel.pack(side="bottom", fill="both", expand="yes")

    skip_button = Button(ins, command=goToSimulation_butt, text="Start", width=20)
    skip_button.place(relx=0.45, rely=0.98, anchor="w")

    ins.mainloop()


def Simulation_Mode():
    global PACD_entry, Portal_entry, Cashier_entry, Computer_entry, Biometric_entry, Simulation_Button
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
        SimulationResultButton.grid(row=0, column=0, ipadx=84, padx=14, pady=40, sticky='nsew')
        title_text2.destroy()
        # write result code here

    def PACD_entry_focus_in(event):
        if PACD_entry.get() == "Enter number":
            PACD_entry.delete(0, 'end')
            PACD_entry.config(fg="Black")

    def PACD_entry_focus_out(event):
        if PACD_entry.get() == "":
            PACD_entry.insert(0, "Enter number")
            PACD_entry.config(fg="gray")

    def Portal_entry_focus_in(event):
        if Portal_entry.get() == "Enter number":
            Portal_entry.delete(0, 'end')
            Portal_entry.config(fg="Black")

    def Portal_entry_focus_out(event):
        if Portal_entry.get() == "":
            Portal_entry.insert(0, "Enter number")
            Portal_entry.config(fg="gray")

    def Cashier_entry_focus_in(event):
        if Cashier_entry.get() == "Enter number":
            Cashier_entry.delete(0, 'end')
            Cashier_entry.config(fg="Black")

    def Cashier_entry_focus_out(event):
        if Cashier_entry.get() == "":
            Cashier_entry.insert(0, "Enter number")
            Cashier_entry.config(fg="gray")

    def Computer_entry_focus_in(event):
        if Computer_entry.get() == "Enter number":
            Computer_entry.delete(0, 'end')
            Computer_entry.config(fg="Black")

    def Computer_entry_focus_out(event):
        if Computer_entry.get() == "":
            Computer_entry.insert(0, "Enter number")
            Computer_entry.config(fg="gray")

    def Biometric_entry_focus_in(event):
        if Biometric_entry.get() == "Enter number":
            Biometric_entry.delete(0, 'end')
            Biometric_entry.config(fg="Black")

    def Biometric_entry_focus_out(event):
        if Biometric_entry.get() == "":
            Biometric_entry.insert(0, "Enter number")
            Biometric_entry.config(fg="gray")



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

    # Text Label
    title_text = Label(first_frame, text="LTO SIMULATION", font=mont_Large, bg="#e9e9e9")
    title_text.grid(row=0, column=0, padx=5, pady=20)

    # PACD Station
    PACD_label = Label(first_frame, text="PACD", font=mont_bold, bg="#e9e9e9")
    PACD_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')

    PACD_entry = Entry(first_frame, font=mont_normal, bd=5)
    PACD_entry.grid(row=1, column=0, ipadx=25, padx=10, pady=10, sticky='ne')
    PACD_entry.insert(0, 'Enter number')
    PACD_entry.bind("<FocusIn>", PACD_entry_focus_in)
    PACD_entry.bind("<FocusOut>", PACD_entry_focus_out)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Portal Station
    Portal_label = Label(first_frame, text="PORTAL", font=mont_bold, bg="#e9e9e9")
    Portal_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')

    Portal_entry = Entry(first_frame, bd=5, font=mont_normal)
    Portal_entry.grid(row=2, column=0, ipadx=25, padx=10, pady=10, sticky='ne')
    Portal_entry.insert(0, 'Enter number')
    Portal_entry.bind("<FocusIn>", Portal_entry_focus_in)
    Portal_entry.bind("<FocusOut>", Portal_entry_focus_out)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Cashier Station
    Cashier_label = Label(first_frame, text="CASHIER", font=mont_bold, bg="#e9e9e9")
    Cashier_label.grid(row=3, column=0, padx=10, pady=10, sticky='w')

    Cashier_entry = Entry(first_frame, bd=5, font=mont_normal)
    Cashier_entry.grid(row=3, column=0, ipadx=25, padx=10, pady=10, sticky='ne')
    Cashier_entry.insert(0, 'Enter number')
    Cashier_entry.bind("<FocusIn>", Cashier_entry_focus_in)
    Cashier_entry.bind("<FocusOut>", Cashier_entry_focus_out)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Examination Station
    Computer_label = Label(first_frame, text="COMPUTER", font=mont_bold, bg="#e9e9e9")
    Computer_label.grid(row=4, column=0, padx=10, pady=10, sticky='w')

    Computer_entry = Entry(first_frame, bd=5, font=mont_normal)
    Computer_entry.grid(row=4, column=0, ipadx=25, padx=10, pady=10, sticky='ne')
    Computer_entry.insert(0, 'Enter number')
    Computer_entry.bind("<FocusIn>", Computer_entry_focus_in)
    Computer_entry.bind("<FocusOut>", Computer_entry_focus_out)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Biometric Station
    Biometric_label = Label(first_frame, text="BIOMETRIC", font=mont_bold, bg='#e9e9e9')
    Biometric_label.grid(row=5, column=0, padx=10, pady=10, sticky='w')

    Biometric_entry = Entry(first_frame, bd=5, font=mont_normal)
    Biometric_entry.grid(row=5, column=0, ipadx=25, padx=10, pady=10, sticky='ne')
    Biometric_entry.insert(0, 'Enter number')
    Biometric_entry.bind("<FocusIn>", Biometric_entry_focus_in)
    Biometric_entry.bind("<FocusOut>", Biometric_entry_focus_out)

    Simulation_Button = Button(first_frame, text="SIMULATE", fg="#000000", font=mont_bold, width=10, height=2, bd=5,
    command=lambda: (showResults(), PlacePACD(), PlacePortal(), PlaceCashier(), PlaceComputer(), PlaceBiometric()))

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

    sim.mainloop()

def simulation_result():
    global total_applicants_label, student_permit_label, NonPro_Label,RenewLicense_Label, Miscellaneous_Label
    simresult = Tk()
    simresult.title("Simulation Results")
    simresult.geometry("1000x800")
    simresult.iconbitmap('LTO Image/LTO Logo.ico')
    simresult.resizable(False, False)
    center_window(simresult, 1000, 600)

    # Title Frame
    TFrame_width = 1000
    TFrame_height = 50
    TFrame = LabelFrame(simresult, bd=5)  # Set bd for sizing
    TFrame.place(x=0, y=0, width=TFrame_width, height=TFrame_height)
    TFrame.columnconfigure(0, minsize=350, weight=1)
    TFrame.rowconfigure(20, weight=1)

    #Result Frame
    ResultFrame_width = 1000
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
    student_permit_label.place(x=30, y=70)

    NonPro_Label = Label(simresult, text="Non-Pro License Applicants: ", font=("Montserrat", 11, "italic"),bg='white', fg='#440d31')
    NonPro_Label.place(x=30, y=120)

    RenewLicense_Label = Label(simresult, text="Renew License Applicants: ", font=("Montserrat", 11, "italic"),bg='white', fg='#440d31')
    RenewLicense_Label.place(x=30, y=170)

    Miscellaneous_Label = Label(simresult, text="Miscellaneous Applicants: ", font=("Montserrat", 11, "italic"),bg='white', fg='#440d31')
    Miscellaneous_Label.place(x=30, y=220)

    total_applicants_label = Label(simresult, text="Total Applicants: ", font=("Montserrat", 11, "italic"),bg='white', fg='#440d31')
    total_applicants_label.place(x=30, y=290)

    # This will make the ApplicantResult Run
    ApplicantResult()


    simresult.mainloop()


def ApplicantResult():
    # Gonna fix it later

    student_permit_label.config(text=f"Student Permit Applicants: {int(yellow_card)}", font=("Montserrat", 15, "italic"), bg='white',fg='#440d31')
    NonPro_Label.config(text=f"Non-Pro License Applicants: {int(blue_card)}", font=("Montserrat", 15, "italic"), bg='white',fg='#440d31')
    RenewLicense_Label.config(text=f"Renew License Applicants: {int(green_card)}", font=("Montserrat", 15, "italic"), bg='white',fg='#440d31')
    Miscellaneous_Label.config(text=f"Miscellaneous Applicants: {int(orange_card)}", font=("Montserrat", 15, "italic"), bg='white',fg='#440d31')
    total_applicants_label.config(text=f"Total Applicants: {applicants}", font=("Montserrat", 15, "italic"),bg='white', fg='#440d31')

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
    HistoryResultFrame_height = 750
    HistoryResultFrame = LabelFrame(historyResult, bd=5, bg='#FFFFFF')
    HistoryResultFrame.place(x=0, y=50, width=HistoryResultFrame_width, height=HistoryResultFrame_height)
    FFrame.columnconfigure(0, minsize=500, weight=1)
    FFrame.rowconfigure(20, weight=1)

    # Text Label
    historytitle_text = "LTO Licensing Queueing\nApplicant History"
    historytitle_ = Label(FFrame, text=historytitle_text, font=("Montserrat", 13, "bold"), bg='white', fg='#AF5FD7')
    historytitle_.grid(row=0, column=0, padx=0, pady=0, sticky='nsew')

    # Create a vertical scrollbar
    scrollbar = Scrollbar(HistoryResultFrame, orient="vertical", command=on_scroll)

    # Create a widget (e.g., Listbox or Text) that you want to attach the scrollbar to
    listbox = Listbox(HistoryResultFrame, yscrollcommand=scrollbar.set)

    # Concatenate the two lists
    all_history_results = history_results + Portal_history_results

    # Add items to the listbox
    for result in all_history_results:
        listbox.insert("end", result)

    # Pack the widgets
    listbox.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Set the scrollbar to operate on the listbox
    scrollbar.config(command=listbox.yview)


# simulation_result()
Simulation_Mode()
# MAINGUIMODE()



