def tester():
    print("you typed" + product.get())
    results.set(product.get())
from tkinter import *
from tkinter import ttk
if __name__=="__main__":

    root = Tk()

    
    product = StringVar(root)
    results = StringVar(root)
    results.set("first")


   


    frm = ttk.Frame(root, padding=100)
    frm.grid()
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    ttk.Button(frm, text="test", command=tester).grid(column =0, row=1)
    productEntry=ttk.Entry(frm,textvariable=product).grid(column=1,row=3)
    resultLabel = ttk.Label(frm, textvariable=results).grid(column=0,row=4)

  
    root.mainloop()


