# 2023-05-09 CHEN, KE-RONG
# Gobang Game
from tkinter import *

window = Tk()
window.configure(bg="sky blue")
window.title("Gobang")  # window title
window.geometry("+400+100")  # window position

# ==========<board const variable>==========
GAME_COLUMN_SIZE = 15  # game column size
GAME_ROW_SIZE = 15  # game row size
CANVAS_LINE_OFFSET = 40  # game line offset
GAME_WHITE_SITE = 0  # game white side size
GAME_STAR_X = [3, 3, 11, 11, 7]  # game star point position x
GAME_STAR_Y = [3, 11, 3, 11, 7]  # game star point position y
GAME_PIECE_SIZE = 15  # game piece size
GAME_STAR_SIZE = 3  # game star circle size
GAME_CLICK_OFFSET = 10  # game click offset
GAME_PIECE_CHOSE = 0  # game piece chose number
GAME_BOUNDARY_OFFSET = 15  # game boundary offset
GAME_BOUNDARY_SIZE = 3  # game boundary size
piece_color = ["black", "white"]  # piece color

# ==========<global variable>==========
mouse_click_x = 0  # game mouse click x position
mouse_click_y = 0  # game mouse click y position
board = []  # game data
canvas = Canvas(window,
                bg="sandyBrown",  # background color
                width=(GAME_COLUMN_SIZE + 1) * CANVAS_LINE_OFFSET + GAME_WHITE_SITE,  # width size
                height=(GAME_ROW_SIZE + 1) * CANVAS_LINE_OFFSET)  # height size
# ==========<draw the checkerboard>==========
def drawBoardReset():
    global canvas
    canvas.delete("all")
    canvas.grid(row=0,  # game grid row position
                column=0,  # game grid column position
                rowspan=10)

    # ==========<draw board>==========
    for star_run in range(GAME_COLUMN_SIZE):
        # ==========<draw column line>==========
        canvas.create_line(CANVAS_LINE_OFFSET,  # start x position
                           CANVAS_LINE_OFFSET * star_run + CANVAS_LINE_OFFSET,  # start y position
                           CANVAS_LINE_OFFSET * GAME_COLUMN_SIZE,  # end x position
                           CANVAS_LINE_OFFSET * star_run + CANVAS_LINE_OFFSET)  # end y position
        # ==========<draw row line>==========
        canvas.create_line(CANVAS_LINE_OFFSET * star_run + CANVAS_LINE_OFFSET,  # start x position
                           CANVAS_LINE_OFFSET,  # start y position
                           CANVAS_LINE_OFFSET * star_run + CANVAS_LINE_OFFSET,  # end x position
                           CANVAS_LINE_OFFSET * GAME_COLUMN_SIZE)  # end y position

    # ==========<draw star>==========
    for star_run in range(len(GAME_STAR_X)):
        canvas.create_oval(CANVAS_LINE_OFFSET * GAME_STAR_X[star_run] + CANVAS_LINE_OFFSET - GAME_STAR_SIZE,
                           # start x position
                           CANVAS_LINE_OFFSET * GAME_STAR_Y[star_run] + CANVAS_LINE_OFFSET - GAME_STAR_SIZE,
                           # start y position
                           CANVAS_LINE_OFFSET * GAME_STAR_X[star_run] + CANVAS_LINE_OFFSET + GAME_STAR_SIZE,
                           # end x position
                           CANVAS_LINE_OFFSET * GAME_STAR_Y[star_run] + CANVAS_LINE_OFFSET + GAME_STAR_SIZE,
                           # end y position
                           fill="black")  # fill star color

    # ==========<draw column boundary line>==========
    for b in range(GAME_BOUNDARY_SIZE):
        canvas.create_line(CANVAS_LINE_OFFSET - GAME_BOUNDARY_OFFSET - 2,  # start x position
                           CANVAS_LINE_OFFSET - GAME_BOUNDARY_OFFSET - b,  # start y position
                           GAME_COLUMN_SIZE * CANVAS_LINE_OFFSET + GAME_BOUNDARY_OFFSET + 3,  # end x position
                           CANVAS_LINE_OFFSET - GAME_BOUNDARY_OFFSET - b)  # end y position
    for b in range(GAME_BOUNDARY_SIZE):
        canvas.create_line(CANVAS_LINE_OFFSET - GAME_BOUNDARY_OFFSET - 2,  # start x position
                           GAME_COLUMN_SIZE * CANVAS_LINE_OFFSET + GAME_BOUNDARY_OFFSET + b,  # start y position
                           GAME_COLUMN_SIZE * CANVAS_LINE_OFFSET + GAME_BOUNDARY_OFFSET + 3,  # end x position
                           GAME_COLUMN_SIZE * CANVAS_LINE_OFFSET + GAME_BOUNDARY_OFFSET + b)  # end y position

    # ==========<draw row boundary line>==========
    for b in range(GAME_BOUNDARY_SIZE):
        canvas.create_line(CANVAS_LINE_OFFSET - GAME_BOUNDARY_OFFSET - b,  # start y position
                           CANVAS_LINE_OFFSET - GAME_BOUNDARY_OFFSET,  # start x position
                           CANVAS_LINE_OFFSET - GAME_BOUNDARY_OFFSET - b,  # end y position
                           GAME_COLUMN_SIZE * CANVAS_LINE_OFFSET + GAME_BOUNDARY_OFFSET)  # end x position

    for b in range(GAME_BOUNDARY_SIZE):
        canvas.create_line(GAME_COLUMN_SIZE * CANVAS_LINE_OFFSET + GAME_BOUNDARY_OFFSET + b,  # start y position
                           CANVAS_LINE_OFFSET - GAME_BOUNDARY_OFFSET,  # start x position
                           GAME_COLUMN_SIZE * CANVAS_LINE_OFFSET + GAME_BOUNDARY_OFFSET + b, # end y position
                           GAME_COLUMN_SIZE * CANVAS_LINE_OFFSET + GAME_BOUNDARY_OFFSET)  # end x position


def boardDataReset():
    # ==========<board data>==========
    global board
    del board[:]
    global GAME_PIECE_CHOSE
    for y in range(GAME_ROW_SIZE):
        board.append([])
        for x in range(GAME_COLUMN_SIZE):
            board[y].append('-')
    GAME_PIECE_CHOSE = 0
    return


def mousePosition(event):
    # ==========<mouse click position>==========
    global mouse_click_y  # mouse click y position
    global mouse_click_x  # mouse click x position
    mouse_click_y = event.y  # change global y variable
    mouse_click_x = event.x  # change global x variable
    mouseJudge()
    return


def mouseJudge():
    # ==========<judge mouse click is ok>==========
    global mouse_click_y  # mouse click y position
    global mouse_click_x  # mouse click x position
    get_y_pos = (mouse_click_y + GAME_CLICK_OFFSET) // CANVAS_LINE_OFFSET
    get_x_pos = (mouse_click_x + GAME_CLICK_OFFSET) // CANVAS_LINE_OFFSET
    get_y_offset = abs(mouse_click_y - get_y_pos * CANVAS_LINE_OFFSET)
    get_x_offset = abs(mouse_click_x - get_x_pos * CANVAS_LINE_OFFSET)
    if get_y_offset <= GAME_CLICK_OFFSET and get_x_offset <= GAME_CLICK_OFFSET:
        if get_y_pos <= 0 or get_x_pos <= 0 or get_y_pos > GAME_ROW_SIZE or get_x_pos > GAME_COLUMN_SIZE:
            # print('click ok but out of range')
            return
        else:
            # print('click yes')
            putPiece(get_y_pos, get_x_pos)
            return
    else:
        # print('click not ok')
        return


def putPiece(get_y, get_x):
    global GAME_PIECE_CHOSE
    if board[get_y - 1][get_x - 1] == '-':
        board[get_y - 1][get_x - 1] = 'O'
        canvas.create_oval(get_x * CANVAS_LINE_OFFSET - GAME_PIECE_SIZE, get_y * CANVAS_LINE_OFFSET - GAME_PIECE_SIZE,
                           get_x * CANVAS_LINE_OFFSET + GAME_PIECE_SIZE, get_y * CANVAS_LINE_OFFSET + GAME_PIECE_SIZE,
                           fill=piece_color[GAME_PIECE_CHOSE], tags="piece")
        if GAME_PIECE_CHOSE == 0:
            GAME_PIECE_CHOSE = 1
        else:
            GAME_PIECE_CHOSE = 0
        return
    else:
        print('This position have other piece')
        return


canvas.bind("<Button-1>", mousePosition)  # bind left button click and find position


def main():
    drawBoardReset()
    boardDataReset()


button1 = Button(window,
                 text="Re-Start",
                 fg='black',
                 bg='pink',
                 width=15,
                 height=4,
                 command=main)

button1.grid(row=4,
             column=1)

if __name__ == '__main__':
    main()
window.mainloop()
