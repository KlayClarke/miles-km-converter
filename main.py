from tkinter import *

window = Tk()
window.title('Miles to Km Converter')
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# entry window

user_entry = Entry(width=10)
user_entry.grid(column=1, row=0)

# label to specify measurement for entry window

label_of_miles = Label(text='Miles')
label_of_miles.grid(column=2, row=0)

# label text 'is equal to'

is_equal_to = Label(text='is equal to')
is_equal_to.grid(column=0, row=1)

# label to display conversion answer

conversion_display = Label(text=0)
conversion_display.grid(column=1, row=1)

# label to specify measurement for conversion answer

label_of_km = Label(text='Km')
label_of_km.grid(column=2, row=1)


# function to convert user_input to KM

def conversion():
    user_input = int(user_entry.get())
    miles_km_conversion = (user_input * 1.609344)
    conversion_display.config(text=round(miles_km_conversion, 2))


# button to calculate conversion

calculate = Button(text='Calculate', command=conversion)
calculate.grid(column=1, row=2)

window.mainloop()
