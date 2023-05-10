from tkinter import *
import socket
import threading
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = "localhost"
port = 1234


window = Tk()
window .title("Client(thread)")
window.geometry("300x400+400+100")


def sendMessage(pos):
    global s
    s.sendto(pos.encode(), (host, port))


def receiveMessage():
    global s
    while True:
        data = s.recv(1024).decode("utf-8")
        if not data:
            print("server has exited!")
            break
        else:
            print(data)
    s.close()


def startNewThread():
    thread = threading.Thread(target=receiveMessage, args=(), daemon=True)
    thread.start()


def callServer():
    sendMessage("call-server")


button1 = Button(window, text="Call Server", font=("Arial", 10), command=callServer, width=20, height=5, anchor=CENTER)
button1.pack(expand=True)

sendMessage("connect-to-server")

startNewThread()

window.mainloop()
