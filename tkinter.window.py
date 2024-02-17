import tkinter
window = tkinter.Tk()
button = tkinter.Button(window, text="Do not press this button.", width=40)

button.pack(pady=20, padx=40)
clickCount = 0

def onClick(event):
    global clickCount
    clickCount = clickCount + 1
    if clickCount == 1:
        button.configure(text="Seriously? Do. Not. Press. It.")
    elif clickCount == 2:
        button.configure(text="Gah! Next time, no more button.")
    elif clickCount == 3:
        button.configure(text="YOUR ARE ANGRY ME!!!")
    elif clickCount == 4:
        button.configure(text="HaHaHa, You S.T.U.P.I.D.")
    else:
        button.pack_forget()

button.bind("<ButtonRelease-1>", onClick)
window.mainloop()

