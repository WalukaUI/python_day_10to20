import tkinter

window = tkinter.Tk()
window.title("Program GUI")
window.minsize(800, 700)

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "italic"))
my_label.pack()
my_label["text"] = "new text"

#Button

def button_clicked():
    val = input.get()
    my_label["text"] = val
    print("clicked")


button = tkinter.Button(text="clickme", command=button_clicked)
button.pack()


#Entry/Input

input = tkinter.Entry(background="red", cursor="hand2")
input.pack()



window.mainloop()





