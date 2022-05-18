from tkinter import *


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)

# miles entry
miles_entry = Entry(width=30)
miles_entry.insert(END, string="0")
#Gets text in entry
print(miles_entry.get())
miles_entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)


#conversion component
equal_label = Label(text="is equal to:")
equal_label.grid(column=0, row=1)
kilometers_label = Label(text="0")
kilometers_label.grid(column=1, row=1)
km_label = Label(text="Km")
km_label.grid(column=2, row=1)





window.mainloop()