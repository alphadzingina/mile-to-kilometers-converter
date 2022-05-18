from tkinter import *


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)

# miles entry
miles_entry = Entry(width=30)
miles_entry.insert(END, string="0")
#Gets text in entry
print(miles_entry.get())
miles_entry.pack()


miles_label = Label(text="Miles")
miles_label.pack()




window.mainloop()