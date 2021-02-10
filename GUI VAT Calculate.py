# HW1_GUI.py
from tkinter import *
from tkinter import ttk

# Interface
GUI = Tk()
GUI.geometry('600x500')
GUI.title('Calculate price + 7% VAT')

# Config
FONT = ('Charter', 20)

# Label 1 Procuct Name
L1 = ttk.Label(GUI, text='Product Name', font=FONT,
               foreground='darkcyan').pack(pady=5)

# Entry 1 Product Name
v_pname = StringVar()  # กล่องเก็บข้อความ
E1 = ttk.Entry(GUI, textvariable=v_pname, font=FONT, width=15).pack()

# Label 2 Price
L2 = ttk.Label(GUI, text='Price', font=FONT,
               foreground='darkcyan').pack(pady=5)

# Entry 2 Price
v_price = StringVar()
E2 = ttk.Entry(GUI, textvariable=v_price, font=FONT, width=15).pack()

# Label 3 Quantity
L3 = ttk.Label(GUI, text='Quantity', font=FONT,
               foreground='darkcyan').pack(pady=5)

# Entry 3 Quantity
v_quantity = StringVar()
E3 = ttk.Entry(GUI, textvariable=v_quantity, font=FONT, width=15).pack()

# Calculate VAT function


def vat(event=None):
    # if you  don't need to bind enter no need to have event;(click button only)
    # event=None mean you can click on the button or enter to run function
    # if only have event mean you can't click button
    product = v_pname.get()
    price = int(v_price.get())
    quant = int(v_quantity.get())
    tprice = price * quant
    # result = price * quant * 1.07
    # v_result.set(result)
    # v_result.set('Price of goods with 7% VAT is {}'.format(result))
    vat7 = tprice * (7 / 107)  # 7 from 107 is 7% vat
    b4vat = tprice * (100 / 107)  # 100 from 107 is price not include vat
    # print('price before vat {: .2f}'.format(b4vat))
    v_result.set('Product: {} \nQuantity {} unit\nTotal price: {} NTD \nPrice before VAT: {: .2f} NTD\nVAT 7 percent: {: .2f} NTD'
                 .format(product, quant, tprice, b4vat, vat7))


# Button
B1 = ttk.Button(text='VAT Calculation',  command=vat)
B1.pack(pady=10, ipadx=10, ipady=5)

# Result Label
v_result = StringVar()
R1 = ttk.Label(GUI, textvariable=v_result, font=FONT,
               foreground='green').pack(pady=10)
v_result.set('[Show Result Here]')

GUI.bind('<Return>', vat)
GUI.mainloop()
