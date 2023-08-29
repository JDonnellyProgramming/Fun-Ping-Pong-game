import tkinter as tk
import math
import random
import time
import pygame as pg
import keyboard

root = tk.Tk()
pg.init()
root.geometry('1000x800')
root.title('Ping Pong')
root.config(bg='red')
root.iconbitmap(r"C:\Users\josep\Downloads\Untitled-Notebook.pdf")
root.resizable(False, False)

label1 = tk.Label(root, bg='white', width=3, height=6)
label1.place(x=0, y=400)
label2 = tk.Label(root, bg='white', width=3, height=6)
label2.place(x=980, y=400)
y_pos = 400
ball_label = tk.Label(root, bg='black', width=2, height=1)
ball_label.place(x=500, y=y_pos)

ball_speed_x = 10
ball_speed_y = 10

new_x2 = 500
new_y2 = 400
new_x = 0
new_y = 400
new_x1 = 980
new_y1 = 400
score1 = 0
score2 = 0

def ball_movement():
    global new_x2, new_y2
    global ball_speed_x
    global ball_speed_y
    x = ball_label.winfo_x()
    y = ball_label.winfo_y()
    if new_x2 <= 0:
        new_x2 = 500
        new_y2 = 400
        ball_speed_x *= random.choice((-1, 1))
        ball_speed_y *= random.choice((-1, 1))
        player2_score()
    if new_x2 >= 980:
        new_x2 = 500
        new_y2 = 400
        ball_speed_x *= random.choice((-1, 1))
        ball_speed_y *= random.choice((-1, 1))
        player1_score()
    if new_y2 <= 0:
        ball_speed_y = -(ball_speed_y)
    if new_y2 >= 780:
        ball_speed_y = -(ball_speed_y)
    if (new_x2 <= 30) and (-70<(new_y2-new_y)<70):
        ball_speed_x = -(ball_speed_x)
        print('hit player 1')
    if (new_x2 >= 950) and (-70<(new_y2-new_y1)<70):
        ball_speed_x = -(ball_speed_x)
        print('hit player 2')
    new_x2 += ball_speed_x
    new_y2 += ball_speed_y
    ball_label.place(x=new_x2, y=new_y2)
    root.after(30, ball_movement)

ball_movement()
def player1_up():
    global new_x, new_y
    x = label1.winfo_x()
    y = label1.winfo_y()
    new_x = x
    new_y = y - 60
    label1.place(x=new_x, y=new_y)
def player1_down():
    global new_x, new_y
    x = label1.winfo_x()
    y = label1.winfo_y()
    new_x = x
    new_y = y + 60
    label1.place(x=new_x, y=new_y)
def player2_up():
    global new_x1, new_y1
    x = label2.winfo_x()
    y = label2.winfo_y()
    new_x1 = x
    new_y1 = y - 60
    label2.place(x=new_x1, y=new_y1)
def player2_down():
    global new_x1, new_y1
    x = label2.winfo_x()
    y = label2.winfo_y()
    new_x1 = x
    new_y1 = y + 60
    label2.place(x=new_x1, y=new_y1)
def controller():
        if keyboard.is_pressed('w') or keyboard.is_pressed('W'):
            player1_up()
        if keyboard.is_pressed('s') or keyboard.is_pressed('S'):
            player1_down()
        if keyboard.is_pressed('o') or keyboard.is_pressed('O'):
            player2_up()
        if keyboard.is_pressed('l') or keyboard.is_pressed('L'):
            player2_down()
        root.after(100, controller)
def player1_score():
    global score1
    score1 += 1
    label3 = tk.Label(root, text=f'Player1: {score1}')
    label3.place(x=200, y=40)
def player2_score():
    global score2
    score2 += 1
    label4 = tk.Label(root, text=f'Player2: {score2}')
    label4.place(x=800, y=40)

def decide_winner():
    new_window = tk.Tk()
    root.destroy()
    if score1 > score2:
        label4 = tk.Label(new_window, text='Player 1 wins')
        label4.pack()
    if score2 > score1:
        label4 = tk.Label(new_window, text='Player 2 wins')
        label4.pack()
    else:
        label4 = tk.Label(new_window, text='A draw')
        label4.pack()
controller()
root.after(120000, decide_winner)

root.mainloop()
