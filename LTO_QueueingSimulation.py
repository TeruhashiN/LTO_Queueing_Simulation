import random
import time
import calendar
from tkinter import Tk, Label, Button, Entry, LabelFrame, font, PhotoImage

from PIL import ImageTk, Image
import os

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
    ins.resizable(False, False)
    center_window(ins, 1093, 800)

    ins_img = ImageTk.PhotoImage(Image.open("LTO Image/LTO_Instruction.png"))  # LTO Instruction Background
    panel = Label(ins, image=ins_img)
    panel.pack(side="bottom", fill="both", expand="yes")

    skip_button = Button(ins, command=goToSimulation_butt, text="Start", width=20)
    skip_button.place(relx=0.45, rely=0.98, anchor="w")

    ins.mainloop()


def Simulation_Mode():
    global PACD_entry, Portal_entry, Cashier_entry, Computer_entry, Biometric_entry
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
        SimulationResultButton.grid(row=0, column=0, ipadx=84, padx=14, pady=40, sticky='nsew')
        title_text2.destroy()
        # write result code here

    sim = Tk()
    sim.title("LTO Licensing Queueing System Simulation")
    sim.geometry("1374x751")
    sim.resizable(False, False)
    sim.configure(bg="lightblue")
    center_window(sim, 1374, 751)

    # background image
    # img = ImageTk.PhotoImage(Image.open("LTO Image/lto_simbg.png"))  # LTO Background
    # panel = Label(sim, image=img)
    # panel.pack(side="bottom", fill="both", expand="yes")

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

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Portal Station
    Portal_label = Label(first_frame, text="PORTAL", font=mont_bold, bg="#e9e9e9")
    Portal_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')

    Portal_entry = Entry(first_frame, bd=5, font=mont_normal)
    Portal_entry.grid(row=2, column=0, ipadx=25, padx=10, pady=10, sticky='ne')

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Cashier Station
    Cashier_label = Label(first_frame, text="CASHIER", font=mont_bold, bg="#e9e9e9")
    Cashier_label.grid(row=3, column=0, padx=10, pady=10, sticky='w')

    Cashier_entry = Entry(first_frame, bd=5, font=mont_normal)
    Cashier_entry.grid(row=3, column=0, ipadx=25, padx=10, pady=10, sticky='ne')

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Examination Station
    Computer_label = Label(first_frame, text="COMPUTER", font=mont_bold, bg="#e9e9e9")
    Computer_label.grid(row=4, column=0, padx=10, pady=10, sticky='w')

    Computer_entry = Entry(first_frame, bd=5, font=mont_normal)
    Computer_entry.grid(row=4, column=0, ipadx=25, padx=10, pady=10, sticky='ne')

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Biometric Station
    Biometric_label = Label(first_frame, text="BIOMETRIC", font=mont_bold, bg='#e9e9e9')
    Biometric_label.grid(row=5, column=0, padx=10, pady=10, sticky='w')

    Biometric_entry = Entry(first_frame, bd=5, font=mont_normal)
    Biometric_entry.grid(row=5, column=0, ipadx=25, padx=10, pady=10, sticky='ne')

    Simulation_Button = Button(first_frame, text="SIMULATE", fg="#000000", font=mont_bold, width=10, height=2, bd=5,command=showResults)
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
    simresult = Tk()
    simresult.title("Simulation Results")
    simresult.geometry("1000x800")
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



    simresult.mainloop()

def showHistory():
    historyResult = Tk()
    historyResult.title("Simulation History")
    historyResult.geometry("1000x600")
    historyResult.resizable(False, False)
    center_window(historyResult, 1000, 600)


Simulation_Mode()


