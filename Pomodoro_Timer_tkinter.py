from tkinter import *
import math
import pygame

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
PURPLE = "#8236CB"
DEEP_RED = "#BE0000"
FONT_NAME = "Courier"
WORK_MIN = 1 / 4
SHORT_BREAK_MIN = 1 / 2
LONG_BREAK_MIN = 2
reps = 0
CHECK = "✔"
timer = None
pygame.init()


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    windows.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    Timer_label.config(text="Timer", fg=DEEP_RED)
    check.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 2 != 0:
        Timer_label.config(text="WORK", fg=YELLOW)
        count_down(work_sec)
        pygame.mixer.music.load("Twin-bell-alarm-clock.mp3")
        pygame.mixer.music.play()

    if reps % 2 == 0:
        Timer_label.config(text="BREAK", fg=PINK)
        count_down(short_break_sec)
        pygame.mixer.music.load('mixkit-police-whistle-614.mp3')
        pygame.mixer.music.play()

    if reps == 8:
        count_down(long_break_sec)
        Timer_label.config(text="BREAK ", fg=RED)
        pygame.mixer.music.load("alarm-clock-01.mp3")
        pygame.mixer.music.play()
        reps = 0


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global reps
    count_minute = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_sec}")
    if count > 0:
        global timer
        timer = windows.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += CHECK
            check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title("Pomodoro")
windows.config(padx=200, pady=100, bg=GREEN)

canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

Timer_label = Label(text="Timer", fg=DEEP_RED, bg=GREEN, font=("Times new roman", 45, "bold"))
Timer_label.grid(column=1, row=0)

start_button = Button(text="Start", font=("Courier", 10, "bold"), command=start_timer)
start_button.config(padx=0, pady=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=("Courier", 10, "bold"), command=reset_timer)
reset_button.config(padx=0, pady=0)
reset_button.grid(column=2, row=2)

check = Label(fg=PURPLE, bg=GREEN, highlightthickness=0, font=20)
check.grid(column=1, row=3)

windows.mainloop()
