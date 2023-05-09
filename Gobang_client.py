# 2023-05-09 CHEN, KE-RONG
# Gobang Game
from tkinter import *
from tkinter.messagebox import *
import socket
import threading

window = Tk()
window.configure(bg="sky blue")
window.title("Gobang Client")  # window title
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
GAME_BOUNDARY_OFFSET = 15  # game boundary offset
GAME_BOUNDARY_SIZE = 3  # game boundary size
PIECE_COLOR = ["black", "white"]  # piece color
HOST = "localhost"
PORT = 8888
# ==========<global variable>==========
mouse_click_x = 0  # game mouse click x position
mouse_click_y = 0  # game mouse click y position
board = []  # game data
game_piece_chose = 0  # game piece chose number
game_winner = -1  # winner color
server_turn = 1
text_var = StringVar()
canvas = Canvas(window,
                bg="sandyBrown",  # background color
                width=(GAME_COLUMN_SIZE + 1) * CANVAS_LINE_OFFSET + GAME_WHITE_SITE,  # width size
                height=(GAME_ROW_SIZE + 1) * CANVAS_LINE_OFFSET)  # height size


# ==========<send message>==========
def sendMessage(pos):
    # send data to address
    s.sendto(pos.encode('utf-8'), (HOST, PORT))


# ==========<receive client message>==========
def receiveMessage():
    global s
    while True:
        data = s.recv(1024).decode("utf-8")
        receive_text = data.split('|')
        if not data:
            print("Server has exited!")
            break
        elif receive_text[0] == "exit":
            print("Opponent exited!")
        elif receive_text[0] == "over":
            print("Opponent wins!")
            showinfo(title="Info", message=data.split("|")[1])
        elif receive_text[0] == "move":
            print("Received:", data)
            take = receive_text[1].split(',')
            new_y = int(take[0])
            new_x = int(take[1])
            print(take[0], take[1])
            drawOtherPiece(new_y, new_x)
    s.close()


# ==========<draw other piece>==========
def drawOtherPiece(get_y, get_x):
    global server_turn
    canvas.create_oval(get_x * CANVAS_LINE_OFFSET - GAME_PIECE_SIZE, get_y * CANVAS_LINE_OFFSET - GAME_PIECE_SIZE,
                       get_x * CANVAS_LINE_OFFSET + GAME_PIECE_SIZE, get_y * CANVAS_LINE_OFFSET + GAME_PIECE_SIZE,
                       fill=PIECE_COLOR[game_piece_chose], tags="piece")
    if server_turn == 1:
        server_turn = 2
    else:
        server_turn = 1


def startNewThread():
    thread=threading.Thread(target=receiveMessage, args=())
    thread.start()


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


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
                           GAME_COLUMN_SIZE * CANVAS_LINE_OFFSET + GAME_BOUNDARY_OFFSET + b,  # end y position
                           GAME_COLUMN_SIZE * CANVAS_LINE_OFFSET + GAME_BOUNDARY_OFFSET)  # end x position


def boardDataReset():
    # ==========<board data>==========
    global board
    global text_var
    global game_piece_chose
    global game_winner
    global server_turn

    del board[:]
    server_turn = 1
    game_piece_chose = 0
    game_winner = -1
    text_var.set(PIECE_COLOR[game_piece_chose] + "\'s turn")

    for y in range(GAME_ROW_SIZE):
        board.append([])
        for x in range(GAME_COLUMN_SIZE):
            board[y].append('-')
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


def checkVictory(get_y, get_x):
    global game_winner
    column_cnt_w = 0
    column_cnt_b = 0
    for x in range(get_x - 4, get_x + 5):
        if 0 <= x < GAME_COLUMN_SIZE and board[get_y][x] == 'X':
            column_cnt_b += 1
            column_cnt_w = 0
        elif 0 <= x < GAME_COLUMN_SIZE and board[get_y][x] == 'O':
            column_cnt_w += 1
            column_cnt_b = 0
        else:
            column_cnt_w = 0
            column_cnt_b = 0
        if column_cnt_w >= 5:
            game_winner = 1
            return
        if column_cnt_b >= 5:
            game_winner = 0
            return

    row_cnt_w = 0
    row_cnt_b = 0
    for y in range(get_y - 4, get_y + 5):
        if 0 <= y < GAME_ROW_SIZE and board[y][get_x] == 'X':
            row_cnt_b += 1
            row_cnt_w = 0
        elif 0 <= y < GAME_ROW_SIZE and board[y][get_x] == 'O':
            row_cnt_w += 1
            row_cnt_b = 0
        else:
            row_cnt_w = 0
            row_cnt_b = 0
        if row_cnt_w >= 5:
            game_winner = 1
            return
        if row_cnt_b >= 5:
            game_winner = 0
            return

    slopeL_w = 0
    slopeL_b = 0
    for t in range(-4, 5):
        if 0 <= get_y + t < GAME_ROW_SIZE and 0 <= get_x + t < GAME_COLUMN_SIZE and \
                board[get_y + t][get_x + t] == 'X':
            slopeL_b += 1
            slopeL_w = 0
        elif 0 <= get_y + t < GAME_ROW_SIZE and 0 <= get_x + t < GAME_COLUMN_SIZE and \
                board[get_y + t][get_x + t] == 'O':
            slopeL_w += 1
            slopeL_b = 0
        else:
            slopeL_w = 0
            slopeL_b = 0
        if slopeL_w >= 5:
            game_winner = 1
            return
        if slopeL_b >= 5:
            game_winner = 0
            return

    slopeR_w = 0
    slopeR_b = 0
    for t in range(-4, 5):
        if 0 <= get_y + t < GAME_ROW_SIZE and 0 <= get_x + (-t) < GAME_COLUMN_SIZE and \
                board[get_y + t][get_x + (-t)] == 'X':
            slopeR_b += 1
            slopeR_w = 0
        elif 0 <= get_y + t < GAME_ROW_SIZE and 0 <= get_x + (-t) < GAME_COLUMN_SIZE and \
                board[get_y + t][get_x + (-t)] == 'O':
            slopeR_w += 1
            slopeR_b = 0
        else:
            slopeR_w = 0
            slopeR_b = 0
        if slopeR_w >= 5:
            game_winner = 1
            return
        if slopeR_b >= 5:
            game_winner = 0
            return


def putPiece(get_y, get_x):
    global game_piece_chose
    global text_var
    global server_turn
    if server_turn == 1:
        showinfo(title="Notice", message="Not your turn yet.")
        return
    if board[get_y - 1][get_x - 1] == '-':
        canvas.create_oval(get_x * CANVAS_LINE_OFFSET - GAME_PIECE_SIZE, get_y * CANVAS_LINE_OFFSET - GAME_PIECE_SIZE,
                           get_x * CANVAS_LINE_OFFSET + GAME_PIECE_SIZE, get_y * CANVAS_LINE_OFFSET + GAME_PIECE_SIZE,
                           fill=PIECE_COLOR[game_piece_chose], tags="piece")
        if game_piece_chose == 0:
            board[get_y - 1][get_x - 1] = 'X'
            game_piece_chose = 1
        else:
            board[get_y - 1][get_x - 1] = 'O'
            game_piece_chose = 0
        pos = str(get_y - 1) + "," + str(get_x - 1)
        sendMessage("move|" + pos)
        print("server go", pos)
        checkVictory(get_y - 1, get_x - 1)

        if server_turn == 1:
            server_turn = 2
        else:
            server_turn = 1

        if game_winner == -1:
            text_var.set(PIECE_COLOR[game_piece_chose] + "\'s turn")
        else:
            text_var.set(PIECE_COLOR[game_winner] + "\'s winner")
        return
    else:
        # print('This position have other piece')
        return


canvas.bind("<Button-1>", mousePosition)  # bind left button click and find position


def main():
    drawBoardReset()
    boardDataReset()
    # ==========<Start a thread to receive messages from clients>=========
    return


button1 = Button(window,
                 text="Re-Start",
                 fg='black',
                 bg='pink',
                 width=15,
                 height=4,
                 command=main)

button1.grid(row=4,
             column=1)

text_var.set(PIECE_COLOR[game_piece_chose] + "\'s turn")
text_label = Label(window,
                   textvariable=text_var,
                   font=('Helvetica bold', 26),
                   bg="sky blue",
                   )

text_label.grid(row=2,
                column=1)


if __name__ == '__main__':
    main()
    sendMessage('join|')
    startNewThread()


window.mainloop()
