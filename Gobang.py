# 2023-05-09 CHEN, KE-RONG
# Gobang Game
from tkinter import *

window = Tk()
window.title("Gobang")                          # window title
window.configure(bg="skyblue")                  # window background
window.geometry("+400+100")                     # window position

# ==========<board const variable>==========
GAME_COLUMN_SIZE = 15                           # game column size
GAME_ROW_SIZE = 15                              # game row size
CANVAS_LINE_OFFSET = 40                         # game line offset
GAME_WHITE_SITE = 200                           # game white side size
GAME_STAR_X = [3,  3, 11, 11, 7]                # game star point position x
GAME_STAR_Y = [3, 11,  3, 11, 7]                # game star point position y
GAME_STAR_SIZE = 3                              # game star circle size
# ==========<draw the checkerboard>==========
canvas = Canvas(window,                                                                 # Tk()
                bg="sandyBrown",                                                        # background color
                width=(GAME_COLUMN_SIZE + 1) * CANVAS_LINE_OFFSET + GAME_WHITE_SITE,    # width size
                height=(GAME_ROW_SIZE + 1) * CANVAS_LINE_OFFSET)                        # height size

canvas.grid(row=0,                                                     # game grid row position
            column=0,                                                  # game grid column position
            rowspan=10)

for x in range(GAME_COLUMN_SIZE):
    # ==========<draw column line>==========
    canvas.create_line(CANVAS_LINE_OFFSET,                              # start x position
                       CANVAS_LINE_OFFSET * x + CANVAS_LINE_OFFSET,     # start y position
                       CANVAS_LINE_OFFSET * GAME_COLUMN_SIZE,           # end x position
                       CANVAS_LINE_OFFSET * x + CANVAS_LINE_OFFSET)     # end y position
    # ==========<draw row line>==========
    canvas.create_line(CANVAS_LINE_OFFSET * x + CANVAS_LINE_OFFSET,     # start x position
                       CANVAS_LINE_OFFSET,                              # start y position
                       CANVAS_LINE_OFFSET * x + CANVAS_LINE_OFFSET,     # end x position
                       CANVAS_LINE_OFFSET * GAME_COLUMN_SIZE)           # end y position

# ==========<draw star>==========
for t in range(len(GAME_STAR_X)):
    canvas.create_oval(CANVAS_LINE_OFFSET * GAME_STAR_X[t] + CANVAS_LINE_OFFSET - GAME_STAR_SIZE,
                       CANVAS_LINE_OFFSET * GAME_STAR_Y[t] + CANVAS_LINE_OFFSET - GAME_STAR_SIZE,
                       CANVAS_LINE_OFFSET * GAME_STAR_X[t] + CANVAS_LINE_OFFSET + GAME_STAR_SIZE,
                       CANVAS_LINE_OFFSET * GAME_STAR_Y[t] + CANVAS_LINE_OFFSET + GAME_STAR_SIZE,
                       fill="black")


window.mainloop()
