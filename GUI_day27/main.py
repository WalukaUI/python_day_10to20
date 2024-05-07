import tkinter

window = tkinter.Tk()
window.title("Program GUI")
window.minsize(800, 700)


my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "italic"))
my_label.pack(side="left")





window.mainloop()

