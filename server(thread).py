from tkinter import *
import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("localhost", 1234))
addr = ("localhost", 1234)

window = Tk()
window .title("Server(thread)")
window.geometry("300x400+400+100")


def sendMessage(pos):
    global s
    global addr
    s.sendto(pos.encode(), addr)


def receiveMessage():
    global s
    global addr
    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode("utf-8")
        if not data:
            print("client has exited!")
            break
        else:
            print(data)
    s.close()


def startNewThread():
    thread = threading.Thread(target=receiveMessage, args=(), daemon=True)
    thread.start()


def callClient():
    sendMessage("call-client")


button1 = Button(window, text="Call Client", font=("Arial", 10), command=callClient, width=20, height=5, anchor=CENTER)
button1.pack(expand=True)


startNewThread()

window .mainloop()

