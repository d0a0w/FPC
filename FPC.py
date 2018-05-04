import tkinter as fpc
import random
root = fpc.Tk()

bal = 10000
game = 0
result = ''


def checkstatus():
    global bal
    global result
    if bal > 0:
        if game == 1:
            luck = random.randint(1, 9)
            if int(luck) < 5:
                result = "Win"
                bal = bal * 2
                balance.configure(text=str(bal) + " Points")
            if int(luck) >= 5:
                result = "Loss"
                bal = bal // 2
                balance.configure(text=str(bal) + " Points")
        elif game == 2:
            luck = random.randint(1, 7)
            if luck <= 2:
                result = "Win"
                bal = bal * 3
                balance.configure(text=str(bal) + " Points")
            if luck > 2:
                result = "Loss"
                bal = bal // 3
                balance.configure(text=str(bal) + " Points")
        elif game == 3:
            luck = random.randint(1, 8)
            if luck == 1:
                result = "Win"
                bal = bal * 4
                balance.configure(text=str(bal) + " Points")
            if luck != 1:
                result = "Loss"
                bal = bal // 4
                balance.configure(text=str(bal) + " Points")
        elif game == 4:
            exit()
        turnout.configure(text="Previous result: " + result)
    else:
        turnout.configure(text="YOU LOSE!")
        if game == 4:
            exit()


def g1():
    global game
    game = 1
    checkstatus()


def g2():
    global game
    game = 2
    checkstatus()


def g3():
    global game
    game = 3
    checkstatus()


def g4():
    global game
    game = 4
    checkstatus()


balance = fpc.Label(root, text=str(bal) + " Points")
b1 = fpc.Button(root, text="Double, 4:5 odds", command=g1)
b2 = fpc.Button(root, text="Triple, 2:5 odds", command=g2)
b3 = fpc.Button(root, text="Quadruple, 1:7 odds", command=g3)
b4 = fpc.Button(root, text="End Game", command=g4)
turnout = fpc.Label(root, text="Previous result: " + result)
turnout.grid(row=4, column=5)
balance.grid(row=0, column=0)
b1.grid(row=3, column=1)
b2.grid(row=3, column=2)
b3.grid(row=3, column=3)
b4.grid(row=3, column=4)


root.mainloop()
