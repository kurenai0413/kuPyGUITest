
from tkinter import *

mainWnd = Tk()
mainWnd.title("kuTkinterTest");

#w1 = tkGui.Label(mainWnd, image=logo).pack(side="right")

logo = PhotoImage(file="tt.png")
description = "Tkinter simple test."

imgLabel = Label(mainWnd, image = logo).pack(side="right")
txtLabel = Label(mainWnd, text = description, padx = 10).pack(side="left")

mainWnd.mainloop()