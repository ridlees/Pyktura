# -*- coding: UTF-8 -*-
'''created by Martin Kodada
An easy python Script to keep my own invoices in check for future projects.

This is the main script that handles UI and runs other scripts.
'''

import QR_code 
import Invoice_body

#QR_code.CreateQR("0","0","0.00","CZK","") test that import works

from tkinter import *
 
window = Tk()
#TODO some graphical layout
#TODO add place to input info about the invoice (see https://www.fakturaonline.cz/vzory-faktur/faktura-danovy-doklad-jsem-platce-dph)
window.title("Invoice Generator")
lbl = Label(window, text="Create invoice")
lbl.grid(column=0, row=0)
lbl = Label(window, text="count")
lbl.grid(column=1, row=0)
lbl = Label(window, text="Description")
lbl.grid(column=2, row=0)
lbl = Label(window, text="VAT/TAX")
lbl.grid(column=3, row=0)
lbl = Label(window, text="price")
lbl.grid(column=4, row=0)
lbl = Label(window, text="TOTAL")
lbl.grid(column=5, row=0)
count = Entry(window,width=10)
count.grid(column=1, row=1)
description= Entry(window,width=10)
description.grid(column=2, row=1)
tax= Entry(window,width=10)
tax.grid(column=3, row=1)
price = Entry(window,width=10)
price.grid(column=4, row=1)
total = Label(window, text="TOTAL price")
total.grid(column=5, row=1)
def clicked():
    price_for_one = int(price.get())/100 * int(tax.get()) + int(price.get())
    total_price_for_row = price_for_one * int(count.get())
    total.configure(text= total_price_for_row)
    QR_code.CreateQR("0","0",total_price_for_row,"CZK","")
btn = Button(window, text="Click Me", command=clicked)
#TODO add a new row with the previous details
btn.grid(column=0, row=1)

window.mainloop()
