from tkinter import *

#Constants to use
# MILE=0
# KMS=1.60934*MILE


window = Tk()
window.title("MILES TO KM CONVERTOR")
window.config(padx=20, pady=20)

input=Entry(width=8)
input.grid(row=0, column=1)

miles=Label(text="MILE")
miles.grid(row=0, column=2)

km=Label(text="KMS")
km.grid(row=1, column=2)

is_equal=Label(text="is equal to")
is_equal.grid(row=1, column=0)

def button_click_operation():
    MILES =float(input.get())
    KMS = 1.60934 * MILES
    my_label.config(text=KMS,font=("Arial",10,"bold"))
    return my_label.grid(column=1, row=1)
my_label=Label(text=0,font=("Arial",10))
my_label.grid(column=1, row=1)
button=Button(text="Calculate",font=("Arial",10,"bold"),command=button_click_operation)
button.grid(column=1,row=2)










mainloop()