from tkinter import *


window = Tk()
window.title("Mile to Km Converter")
#window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# miles entry
miles_entry = Entry(width=10)
miles_entry.insert(END, string="0")
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


def action():
    miles = float(miles_entry.get())
    kilometers = str(miles * 1.60934)
    kilometers_label.config(text=f"{kilometers}")


#button
button = Button(text="Calculate", command=action)
button.grid(column=1, row=2)



window.mainloop()