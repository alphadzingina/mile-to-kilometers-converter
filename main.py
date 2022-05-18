from tkinter import *


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)

# miles entry
entry = Entry(width=30)
entry.insert(END, string="0")
#Gets text in entry
print(entry.get())
entry.pack()




window.mainloop()